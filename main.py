import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import keyboards as kb
from states import Form
from loader import dp, bot, _
from lang import LANGS, LANG_STORAGE, Localization
from language import lang_text
from aiogram.types import ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(_("Welcome to the bot Official of the Tashkent Regional Department of the Chamber of Commerce and Industry"),
     reply_markup=kb.mainmenu)

@dp.message_handler(commands="lang")
async def cmd_lang(message: types.Message, locale):
    await message.answer(_("Your language: <i>{language}</i>").format(language=locale))

@dp.message_handler(text="🇺🇿UZ|🇷🇺RU|🇬🇧ENG")
async def send_welcome(message: types.Message):
    await message.answer("🇺🇿 Тилни танланг\n🇷🇺 Выберите язык\n🇬🇧Select a language", reply_markup=kb.til)

@dp.callback_query_handler(text=["🇷🇺 Русский", "🇬🇧 English", "🇺🇿 O'zbekcha"])
async def lang(query: types.CallbackQuery):
    if query.data in LANGS.keys():
        lang = LANGS.get(query.data)
    LANG_STORAGE[query.from_user.id] = lang
    await query.answer(text=_("Language adjusted ✅", locale=lang), show_alert=True)
    await query.message.delete()
    await query.message.answer(_("Click restart /start", locale=lang), reply_markup=kb.mainmenu)


@dp.message_handler(text=["👤 Биз ҳақимизда","👤 О нас", "👤 About us"])
async def sahifa(message: types.Message):
    if message.text == "👤 Биз ҳақимизда":
        await message.answer(lang_text[0], reply_markup=kb.mainmenu)
    elif message.text == "👤 О нас":
        await message.answer(lang_text[5], reply_markup=kb.mainmenu)
    elif message.text == "👤 About us":
        await message.answer(lang_text[10], reply_markup=kb.mainmenu)

@dp.message_handler(text_startswith=_('✅ Types of services'), state=None)
async def start(msg: types.Message):
    await msg.answer(_("Select the type of work:"), reply_markup=kb.ish)
    await Form.ish.set()

@dp.message_handler(lambda message: message.text not in ["✅ Types of services", "Export assistance", "Exhibition", "Preparation of a business plan", "Legal issues", "✅ Виды услуг", "Продвижение экспорта", "Выставки", "Бизнес-план", "Юридические проблемы", "✅ Хизмат турлари", "Юридик масалалар", "Экспортга кўмаклашиш", "Кўргазма", "Бизнес режа тайёрлаш"], state=Form.ish)
async def ish_invalid(message: types.Message, state: FSMContext):
    if message.text == _("🔙 Back"):
        await state.finish()
        await message.answer(_("Home page"), reply_markup=kb.mainmenu)
    else:
        return await message.reply(_("Choose from the buttons!"))

@dp.message_handler(state='*', text_startswith=[_('🔙 Back')])
@dp.message_handler(Text(equals=('cancel'), ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
  
    await message.reply(_('Application canceled!'), reply_markup=kb.mainmenu)

@dp.message_handler(state=Form.ish)
async def ish(msg: types.Message, state:FSMContext):
    ish=msg.text
    if ish == "Экспортга кўмаклашиш":
        await msg.reply_photo("https://t.me/rasmlarpalata/56")
        await msg.answer(lang_text[1])
    elif ish == "Продвижение экспорта":
        await msg.reply_photo("https://t.me/rasmlarpalata/46")
        await msg.answer(lang_text[6])
    elif ish == "Export assistance":
        await msg.reply_photo("https://t.me/rasmlarpalata/49")
        await msg.answer(lang_text[11])

    if ish == "Кўргазма":
        await msg.reply_photo("https://t.me/rasmlarpalata/56")
        await msg.answer(lang_text[2])
    elif ish == "Выставки":
        await msg.reply_photo("https://t.me/rasmlarpalata/42")
        await msg.answer(lang_text[7])
    elif ish == "Exhibition":
        await msg.reply_photo("https://t.me/rasmlarpalata/33")
        await msg.answer(lang_text[12])
    
    if ish == "Бизнес режа тайёрлаш":
        await msg.reply_photo("https://t.me/rasmlarpalata/37")
        await msg.answer(lang_text[3])
    elif ish == "Бизнес-план":
        await msg.reply_photo("https://t.me/rasmlarpalata/44")
        await msg.answer(lang_text[8])
    elif ish == "Preparation of a business plan":
        await msg.reply_photo("https://t.me/rasmlarpalata/53")
        await msg.answer(lang_text[13])

    if ish == "Юридик масалалар":
        await msg.reply_photo("https://t.me/rasmlarpalata/39")
        await msg.answer(lang_text[4])
    elif ish == "Юридические проблемы":
        await msg.reply_photo("https://t.me/rasmlarpalata/45")
        await msg.answer(lang_text[9])
    elif ish == "Legal issues":
        await msg.reply_photo("https://t.me/rasmlarpalata/51")
        await msg.answer(lang_text[14])

    await state.update_data({'ish':ish})
    await msg.answer(_("Do you want to leave an application?"), reply_markup=kb.ariza)
    await Form.next()

@dp.message_handler(state=Form.ar)
async def ar(msg: types.Message, state:FSMContext):
    ar=msg.text
    if ar == _("📝 Leave an application"):
        await msg.answer(_("Enter your name:"), reply_markup=kb.Main)
        await Form.next()

@dp.message_handler(state=Form.ism)
async def ism(msg: types.Message, state:FSMContext):
    ism=msg.text
    await state.update_data({'ism':ism})
    await msg.answer(_("Enter the full name of your company:"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(state=Form.firma)
async def firma(msg: types.Message, state:FSMContext):
    firma=msg.text
    await state.update_data({'firma':firma})
    await msg.answer(_("Enter the (STIR)INN number:"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(lambda message: not len(message.text) == 9, state=Form.inn)
async def inn_invalid(message: types.Message):
    return await message.reply(_("(STIR)INN number entered incorrectly!"))

@dp.message_handler(lambda message: message.text.isdigit(), state=Form.inn)
async def inn(msg: types.Message, state:FSMContext):
    inn=msg.text
    await state.update_data({'inn':inn})
    await msg.answer(_("Enter your full phone number: For example: +9989********"), reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(lambda message: not len(message.text) == 13, state=Form.tel)
async def tel_invalid(message: types.Message):
    return await message.reply(_("Phone number entered incorrectly! Please enter the full number"))

count = 0
@dp.message_handler(lambda message: message.text, state=Form.tel)
async def tel(msg: types.Message, state:FSMContext):
    tel=msg.text
    global count
    #await state.update_data(tel=int(msg.text))
    await state.update_data({'tel':tel})
    data = await state.get_data()
    count += 1

    xabar = (f"<b>№: {count}</b>\n"
            f"<b>Хизмат тури:</b> <code>{data['ish']}</code>\n"
            f"<b>Исми:</b> <code>{data['ism']}</code>\n"
            f"<b>Фирма номи:</b> <code>{data['firma']}</code>\n"
            f"<b>Инн рақами:</b> <code>{data['inn']}</code>\n"
            f"<b>Телефон рақами:</b> <code>{data['tel']}</code>\n")
    await bot.send_message(chat_id=-1001616703745, text=xabar)
    await msg.answer(_("✅ Your application has been accepted and will be contacted shortly"), reply_markup=kb.mainmenu)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
