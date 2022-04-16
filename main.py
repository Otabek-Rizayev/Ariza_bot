import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ParseMode
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import keyboards as kb
from states import Form
from loader import dp, bot, _, __
from lang import LANGS, LANG_STORAGE, Localization
from language import lang_text

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(_("Савдо-Саноат палатаси Тошкент вилояти Худудий бошқармасининг расмий ботига хуш келибсиз",
        ).format(user=message.from_user.full_name), reply_markup=kb.mainmenu)

@dp.message_handler(commands="lang")
async def cmd_lang(message: types.Message):
    await message.answer(_("Сизнинг тилингиз: <i>{language}</i>").format(language=locale))

@dp.message_handler(commands=['set'])
async def cmd_setlang(message: types.Message):
    lang = message.get_args()
    if not lang:
        return await message.answer(_("Тилни танланг.\nМисол учун: /setlang en"))
    if lang not in LANGS:
        return await message.answer(_("Бу тил мавжуд эмас!"))

    LANG_STORAGE[message.from_user.id] = lang
    await message.answer(_("Тил созланди", locale=lang))

@dp.message_handler(text=["👤 Биз ҳақимизда","👤 О нас", "👤 About us"])
async def sahifa(message: types.Message):
    if message.text == "👤 Биз ҳақимизда":
        await message.answer(lang_text[1], reply_markup=kb.mainmenu)
    elif message.text == "👤 О нас":
        await message.answer(lang_text[5], reply_markup=kb.mainmenu)
    elif message.text == "👤 About us":
        await message.answer(lang_text[10], reply_markup=kb.mainmenu)

@dp.message_handler(text_startswith=_('✅ Хизмат турлари'), state=None)
async def start(msg: types.Message):
    await msg.answer(_("Иш турини танланг:"), reply_markup=kb.ish)
    await Form.ish.set()

@dp.message_handler(lambda message: message.text not in ["✅ Types of services", "Export assistance", "Exhibition", "Preparation of a business plan", "Legal issues", "✅ Виды услуг", "Продвижение экспорта", "Выставки", "Бизнес-план", "Юридические проблемы", "✅ Хизмат турлари", "Юридик масалалар", "Экспортга кўмаклашиш", "Кўргазма", "Бизнес режа тайёрлаш"], state=Form.ish)
async def ish_invalid(message: types.Message, state: FSMContext):
    if message.text == _("🔙 Орқага"):
        await state.finish()
        await message.answer(_("Бош саҳифа"), reply_markup=kb.mainmenu)
    else:
        return await message.reply(_("Кнопкадан танланг!"))

@dp.message_handler(state='*', text_startswith=[_('🔙 Орқага')])
@dp.message_handler(Text(equals=('cancel'), ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
  
    await message.reply(_('Ариза бекор қилинди!'), reply_markup=kb.mainmenu)

@dp.message_handler(state=Form.ish)
async def ish(msg: types.Message, state:FSMContext):
    ish=msg.text
    if ish == "Экспортга кўмаклашиш":
        await msg.reply_photo("https://t.me/rasmlarpalata/31")
        await msg.answer(lang_text[1])
    elif ish == "Продвижение экспорта":
        await msg.reply_photo("https://t.me/rasmlarpalata/31")
        await msg.answer(lang_text[6])
    elif ish == "Export assistance":
        await msg.reply_photo("https://t.me/rasmlarpalata/31")
        await msg.answer(lang_text[11])

    if ish == "Кўргазма":
        await msg.reply_photo("https://t.me/rasmlarpalata/33")
        await msg.answer(lang_text[2])
    elif ish == "Выставки":
        await msg.reply_photo("https://t.me/rasmlarpalata/33")
        await msg.answer(lang_text[7])
    elif ish == "Exhibition":
        await msg.reply_photo("https://t.me/rasmlarpalata/33")
        await msg.answer(lang_text[12])
    
    if ish == "Бизнес режа тайёрлаш":
        await msg.reply_photo("https://t.me/rasmlarpalata/37")
        await msg.answer(lang_text[3])
    elif ish == "Бизнес-план":
        await msg.reply_photo("https://t.me/rasmlarpalata/37")
        await msg.answer(lang_text[8])
    elif ish == "Preparation of a business plan":
        await msg.reply_photo("https://t.me/rasmlarpalata/37")
        await msg.answer(lang_text[13])

    if ish == "Юридик масалалар":
        await msg.reply_photo("https://t.me/rasmlarpalata/35")
        await msg.answer(lang_text[4])
    elif ish == "Юридические проблемы":
        await msg.reply_photo("https://t.me/rasmlarpalata/35")
        await msg.answer(lang_text[9])
    elif ish == "Legal issues":
        await msg.reply_photo("https://t.me/rasmlarpalata/35")
        await msg.answer(lang_text[14])

    await state.update_data({'ish':ish})
    await msg.answer(_("Ариза қолдиришни истайсизми?"), reply_markup=kb.ariza)
    await Form.next()

@dp.message_handler(state=Form.ar)
async def ar(msg: types.Message, state:FSMContext):
    ar=msg.text
    if ar == _("📝 Ариза қолдириш"):
        await msg.answer(_("Исмингизни киритинг:"), reply_markup=kb.Main)
        await Form.next()

@dp.message_handler(state=Form.ism)
async def ism(msg: types.Message, state:FSMContext):
    ism=msg.text
    await state.update_data({'ism':ism})
    await msg.answer(_("Фирмангизни тўлик номини киритинг:"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(state=Form.firma)
async def firma(msg: types.Message, state:FSMContext):
    firma=msg.text
    await state.update_data({'firma':firma})
    await msg.answer(_("(STIR)ИНН рақамини киритинг:"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(lambda message: not len(message.text) == 9, state=Form.inn)
async def inn_invalid(message: types.Message):
    return await message.reply(_("(STIR)ИНН рақами нотўғри киритилди!"))

@dp.message_handler(lambda message: message.text.isdigit(), state=Form.inn)
async def inn(msg: types.Message, state:FSMContext):
    inn=msg.text
    await state.update_data({'inn':inn})
    await msg.answer(_("Телефон рақамингизни тўлиқ киритинг: Мисол учун: +9989********"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(lambda message: not len(message.text) == 13, state=Form.tel)
async def tel_invalid(message: types.Message):
    return await message.reply(_("Телефон рақами нотўғри киритилди! Илтимос рақамни тўлиқ киритинг"))

count = 0
@dp.message_handler(lambda message: message.text, state=Form.tel)
async def tel(msg: types.Message, state:FSMContext):
    tel=msg.text
    global count
    #await state.update_data(tel=int(msg.text))
    await state.update_data({'tel':tel})
    data = await state.get_data()
    count += 1

    xabar = (f"№: <b>{count}</b>\n"
            f"Хизмат тури: <b>{data['ish']}</b>\n"
            f"Исми: <b>{data['ism']}</b>\n"
            f"Фирма номи: <b>{data['firma']}</b>\n"
            f"Инн рақами: <b>{data['inn']}</b>\n"
            f"Телефон рақами: <b>{data['tel']}</b>\n")
    await bot.send_message(chat_id=-1001746692435, text=xabar)
    await msg.answer(_("✅ Аризангиз қабул қилинди, тез орада алоқага чиқилади"), reply_markup=kb.mainmenu)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
