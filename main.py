import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import keyboards as kb
from config import ADMINS
from states import Form, Feedback
from loader import dp, bot, _
from lang import LANGS, LANG_STORAGE, Localization
from aiogram.types import ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(_("Salom <b>{user}</b>").format(user=message.from_user.full_name),
     reply_markup=kb.mainmenu)

@dp.message_handler(text="🇺🇿UZ|🇷🇺RU|🇬🇧ENG")
async def send_welcome(message: types.Message):
    await message.answer("🇺🇿 Tilni tanlang\n🇷🇺 Выберите язык\n🇬🇧Select a language", reply_markup=kb.til)

@dp.callback_query_handler(text=["🇷🇺 Русский", "🇬🇧 English", "🇺🇿 O'zbekcha"])
async def lang(query: types.CallbackQuery):
    if query.data in LANGS.keys():
        lang = LANGS.get(query.data)
    LANG_STORAGE[query.from_user.id] = lang
    await query.answer(text=_("Til o'zgardi ✅", locale=lang), show_alert=True)
    await query.message.delete()
    await query.message.answer(_("Boshlash uchun /start bosing", locale=lang), reply_markup=kb.mainmenu)

@dp.message_handler(text_startswith=_("💬 Adminga xabar qoldirish"), state='*')
async def start_feed(msg: types.Message):
    await msg.reply(_("Adminga o'z fikr mulohazalaringizni yuboring.\nAlbatta iltimosingiz ko'rib chiqiladi!"), reply_markup=kb.Main)
    await Feedback.feed.set()

@dp.message_handler(state='*', text_startswith=[_('🔙 Orqaga')])
@dp.message_handler(Text(equals=('cancel'), ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
  
    await message.reply(_('Bosh sahifa'), reply_markup=kb.mainmenu)

@dp.message_handler(state=Feedback.feed)
async def end_feed(msg: types.Message, state=FSMContext):
    feed = msg.text
    await bot.send_message(chat_id=1166663829, text=f"<b>{msg.from_user.full_name}:</b>\n<em>{feed}</em>")
    await state.finish()
    await msg.answer(_("Fikr mulohazangiz uchun tashakkur!"), reply_markup=kb.mainmenu)

@dp.message_handler(text=_("👤 Biz haqimizda"))
async def sahifa(message: types.Message):
    if message.text == "👤 Biz haqimizda":
        await message.answer("Bu yerda Kompaniyangiz haqida ma'lumot yoziladi!", reply_markup=kb.mainmenu)

@dp.message_handler(text_startswith=_('📝 Ariza qoldirish'), state=None)
async def start(msg: types.Message):
    await msg.answer(_("Ish turini tanlang:"), reply_markup=kb.ish)
    await Form.ish.set()

@dp.message_handler(lambda message: message.text not in ["🔙 Orqaga", "Менеджер", "Бухгалтер", "Инженер", "Руководитель проекта", "Accountant", "Manager", "Engineer", "Project manager", "Meneger", "Buxgalter", "Injiner", "Loyiha boshqaruvchisi"], state=Form.ish)
async def ish_invalid(message: types.Message, state: FSMContext):
    return await message.reply(_("Knopkadan tanlang!"))

@dp.message_handler(lambda message: message.text in ["Менеджер", "Бухгалтер", "Инженер", "Руководитель проекта", "Accountant", "Manager", "Engineer", "Project manager", "Meneger", "Buxgalter", "Injiner", "Loyiha boshqaruvchisi"], state=Form.ish)
async def ish_state(message: types.Message, state: FSMContext):
    ish=message.text
    await state.update_data({'ish':ish})
    await message.answer(_("Ism, familiyangizni kiriting:"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(state='*', text_startswith=[_('🔙 Orqaga')])
@dp.message_handler(Text(equals=('cancel'), ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
  
    await message.reply(_('Ariza bekor qilindi!'), reply_markup=kb.mainmenu)

@dp.message_handler(state=Form.ism)
async def ism_state(msg: types.Message, state:FSMContext):
    ism=msg.text
    await state.update_data({'ism':ism})
    await msg.answer(_("Oldingi ish-faoliyatingiz haqida qisqacha yozing:"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(state=Form.firma)
async def firma_state(msg: types.Message, state:FSMContext):
    firma=msg.text
    await state.update_data({'firma':firma})
    await msg.answer(_("Telefon raqamingizni to'liq kiriting:\nMisol uchun: +9989********"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(lambda message: not len(message.text) == 13, state=Form.tel)
async def tel_invalid(message: types.Message):
    return await message.reply(_("Telefon raqam noto'g'ri kiritildi!"))

@dp.message_handler(lambda message: message.text, state=Form.tel)
async def tel(msg: types.Message, state:FSMContext):
    tel=msg.text
    count = 0
    await state.update_data({'tel':tel})
    data = await state.get_data()
    count += 1

    xabar = (f"<b>№: {count}</b>\n"
            f"<b>Ishlamoqchi:</b>  <code>{data['ish']}</code>\n"
            f"<b>Ism, familyasi:</b>  <code>{data['ism']}</code>\n"
            f"<b>Oldingi ishlagan joyi:</b>  <code>{data['firma']}</code>\n"
            f"<b>Telefon raqami:</b>  <code>{data['tel']}</code>\n")
    await bot.send_message(chat_id=-1001615759658, text=xabar)
    await msg.answer(_("✅ Arizangiz qabul qilindi. Tez orada aloqaga chiqiladi."), reply_markup=kb.mainmenu)
    await msg.reply("Arizangiz @Ariza_test kanaliga yuborildi!")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
