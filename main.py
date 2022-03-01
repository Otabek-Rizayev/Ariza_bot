import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import keyboards as kb
from states import Form

API_TOKEN = '5156800116:AAFmF0RALm3ZYCGqHhWsYnnJvJSDXZXEyhM'
#1603763305:AAEajpRkbOIXODmaVTB90HLBYseaMWAlCzo
#5156800116:AAFmF0RALm3ZYCGqHhWsYnnJvJSDXZXEyhM
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Савдо-Саноат палатаси Тошкент вилояти Худудий бошқармасига хуш келибсиз", reply_markup=kb.mainmenu)

@dp.message_handler(text_startswith='✅ Хизмат турлари', state=None)
async def start(msg: types.Message):
    await msg.answer("Иш турини танланг:", reply_markup=kb.ish)
    
    await Form.ish.set()
        

@dp.message_handler(lambda message: message.text not in ["✅ Хизмат турлари", "Юридик масалалар", "Экспортга кўмаклашиш", "Кўргазма", "Бизнес режа тайёрлаш"], state=Form.ish)
async def ish_invalid(message: types.Message, state: FSMContext):
    if message.text == "🔙 Орқага":
        await state.finish()
        await message.answer("Бош саҳифа", reply_markup=kb.mainmenu)
    else:
        return await message.reply("Кнопкадан танланг!")

@dp.message_handler(state='*', text_startswith='🔙 Орқага')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Ариза бекор қилинди!', reply_markup=kb.mainmenu)

@dp.message_handler(state=Form.ish)
async def ish(msg: types.Message, state:FSMContext):
    ish=msg.text
    if ish == "Юридик масалалар":
        try:
            await msg.reply_photo("https://t.me/rasmlarpalata/22")
        except:
            await msg.answer("Rasm o'chirib tashlangan...")
        await msg.answer("Тадбиркорлик субъектлари ҳуқуқларини ҳимоя қилиш сектори қуйидаги асосий йўналишлар бўйича фаолияти юритилишида бошчилик қилади:\n\n"
                                "💥Давлат хизматларини кўрсатувчи ваколатли органлар билан  ҳуқуқни ҳимоя қилувчи ва назорат қилувчи органлар билан ўзаро ҳамкорлик қилади;\n\n"
                                "💥Тадбиркорлик субъектларининг ҳуқуқлари ва қонуний манфаатлари ишончли муҳофазасининг кафолатларини кучайтириш, хусусий мулк ва тадбиркорликнинг устуворлик роли ва дахлсизлигини таъминлаш.\n\n"
                                "💥Давлат органларининг ваколатли шахслари қарорлари, ҳаракати ёки ҳаракатсизлиги устидан шикоятлар бўйича тадбиркорлик субъектлари номидан суд жараёнларида иштирок этиш, шунингдек, шикоят аризалари билан бир қаторда апелляция, кассация шикоятлари, аризалар, жумладан назорат тартибида рад этиш тўғрисидаги хатларни тақдим этиш:\n\n"
                                "💥Палата аъзоларининг қонуний манфаатларини ҳимоя қилиш юзасидан ўрнатилган тартибда судларга даъво ариза  киритиш:\n\n"
                                "💥Тадбиркорлик субъектларининг ўзаро низоларини судгача келишув йўли билан ҳал этиш:\n\n"
                                "💥Соҳага доир масалалар бўйича жисмоний ва юридик шахсларнинг вакилларини шахсан қабул қилиш:\n\n"
                                "💥Ўз фаолият йўналишларидан келиб чиқиб, давлат ва нодавлат органлар билан самарали ҳамкорликни ташкил этиш ва улар билан тадбиркорлик субъектларининг ҳуқуқларини ҳимоя қилиш нуқтаи назардан муносабатга киришиш;\n\n"
                                "Тадбиркорлик субъектлари ҳуқуқларини ҳимоя қилиш секторининг  2021 йилда кўрсатилган хизматлари ҳақида қисқача маълумотлар:\n\n"
                                "💥Тадбиркорлик субектларини химоя қилиш юзасидан судларга пудрат шартномаси  бўйича қаноатлантирилган даъво аризалар сони - 7500\n\n"
                                "💥Давлат солиқ органлари қарорларини хақиқий эмас деб топиш бўйича қаноатлантирилган  шикоят аризалар сони- 110\n\n"
                                "💥Ҳоким қарорини хақиқи емас деб топиш бўйича киритилган ва  қаноатлантирилган  шикоят аризалар сони - 124\n\n"
                                "💥Фермер хўжаликларини контрактация шартномаси бўйича қаноатлантирилган аризалар сони - 4000\n\n"
                                "💥Давлат органлари хати-харакатлари бўйича киритилган аризалар сони - 167\n\n"
                                "💥Олди соти шартномаси  бўйича  қариздорликни ундириш юзасидан даъво аризалар сони - 7000\n\n"
                                "💥Бузиб ташланган биноларни компенсация мажбуриятини юклаш бўйича  критилган аризалар - 130\n\n"
                                "💥Лизинг шартномаси бўйича қарздорликни ундириш критилган даво аризалар сони  - 9000\n\n"
                                "💥Аренда шартномаси бўйича киритилган мурожаатлар сони- 10.000\n\n"
                                "💥Маҳсулот етказиб бериш бўйича киритилган даъво аризалар сони - 18.000\n\n"
                                "Ва бошқа мурожат хатлари\n\n"
                                "мурожат учун тел: ( 95 ) 202-16-16")
    if ish == "Экспортга кўмаклашиш":
        try:
            await msg.reply_photo("https://t.me/rasmlarpalata/25")
        except:
            await msg.reply("Rasm o'chirib tashlangan...")
        await msg.answer("💥Экспортга кўмаклашиш ва инвестициялар жалб қилиш сектори\n"
                            "💥 Палата Ижро этувчи қўмитасининг Маҳаллий маҳсулот, иш ва хизматларни экспорт қилишга кўмаклашиш.бизнес-форумлар, савдо-саноат кўргазмалари ва ярмаркаларини ташкил этиш ва уларда маҳаллий тадбиркорлик субъектларининг кенг иштирокини таъминлаш;\n\n"
                            "💥маҳаллий корхоналар маҳсулотларининг ташқи бозорларга чиқарилишини таъминлаш, - тадбиркорлик субъектларига ишончли ҳамкорлар, янги бозорларни излаш ва ишлаб чиқарилган маҳсулотларни ташқи бозорларга йўналтириш;\n\n"
                            "💥бизнес-форумлар, кўргазмалар ва ярмаркаларни ташкил этиш ва уларда маҳаллий тадбиркорлик субъектларининг кенг иштирокини таъминлаш;\n\n"
                            "💥маҳаллий корхоналар маҳсулотларининг ташқи бозорларга чиқарилишини таъминлаш, миллий брендларни хорижда фаол илгари суриш\n\n"
                            "💥тадбиркорлик субъектларига ишончли ҳамкорлар, янги бозорларни излаш ва ишлаб чиқарилган маҳсулотларни ташқи бозорларга йўналтириш;\n\n"
                            "Экспортга кўмаклашиш ва инвестициялар жалб қилиш секторининг  2021 йилда кўрсатилган хизматлари ҳақида қисқача маълумот:\n\n"
                            "💥Палата кўмагида амалга оширилган экспорт суммаси 13.000.000$💵\n\n"
                            "💥Палата кўмагида экспорт амалга оширилган мамлакатлар сони - 34 давлат🌏\n\n"
                            "💥Миллий брендлар бўйича ўтказилган кўргазма ва ярмаркалар сони - 5🧑🏻‍💻\n\n"
                            "💥Экспорт фаолиятини кўллаб-кувватлаш бўйича ўтказилган тадбирлар сони - 21🎫\n\n"
                            "💥Стандартлаштириш ва сертификациялаш  сохасида муаммоларини хал этишга кўмаклашилган  тадбирлар сони -21🏢🧾📑\n\n"
                            "💥Палата кўмагида махсулотларини экспорт қилган тадбиркорлик субьектларини сони-26 🧑🏻‍💻🌍\n\n"
                            "💥Асбоб-ускуналар излаш ва уларни харид қилишга кўмаклашиш ва шартнома тузишга ёрдамлашиш бўйича тадбиркорлар сони - 833 🤝🌍\n\n")
    if ish == "Бизнес режа тайёрлаш":
        try:
            await msg.reply_photo("https://t.me/rasmlarpalata/28")
        except:
            await msg.reply("Rasm o'chirib tashlangan...")
        await msg.answer("📊Хусусий тадбиркорликни ривожлантиришнинг самарали йўналишларини аниқлаш мақсадида ички ва ташқи бозорни мунтазам ўрганиб бориш; 📈💵💸\n\n"
                             "🧑🏻‍💻Халқаро ва Палата тизими иш фаолиятида фойдаланиш учун ички бозордаги нархлар шаклланиши юзасидан маркетинг тадқиқотлари ўтказиш бўйича методик қўлланмалар ишлаб чиқиш;🌍📈💸\n\n"
                             "🇺🇿🌍Республика ҳудудида ва хорижда маҳаллий ва хорижий ҳамкорлар билан биргаликда махаллий тадбиркорларни тайёрлаш ва қайта тайёрлаш мақсадида маркетинг тадқиқотлари масалалари юзасидан ўқув курслари ва семинарлар ташкил этиш ҳамда уларни ўтказишда"
                             "марказ фаолиятида фойдаланиш учун ички бозордаги нархлар шаклланиши юзасидан маркетинг тадқиқотлари ўтказиш бўйича методик қўлланмалар ишлаб чиқишда кўмаклашиш, ҳамда бизнес-план тайёрлаб беришда қатнашиш каби хизматларни кўрсатади.👩🏻‍💻🤝🧑🏽‍💻📈\n\n"
                             "Бизнес план тайёрлашга кўмаклашиш секторининг 2021 йил давомида кўрсатган хизматлари хақида қисқача маълумотлар:\n\n"
                             "👩🏻‍💻📈Бизнес-режалар лойиҳаларини тайёрлаб бериш хизматлари - 3000 та 🧾\n\n"
                             "👩🏻‍💼📑Бепул хизмат кўрсатишлар  турлари бўйича - 5839 та\n\n"
                             "👩🏻‍💼🥇Пуллик хизматлар кўрсатишлар турлари  бўйича - 715 та\n\n"
                             "🏢🧾Ер майдонлари ва бино-иншоотлар, жумладан бўш турган объектлардан фойдаланиш бўйича маълумотлар бериш - 70 та\n\n"
                             "💵💸Инвестицияни жалб этиш, технологик машина, ускуналардан фойдаланишда кўмаклашиш - 210 та🚛🪝\n\n"
                             "🏚Ишлаб чиқариш объектлари, жумладан, саноат зоналаридан фойдаланишда кўмаклашиш - 57 та 📑\n\n"
                             "🕵🏻‍♂️🤝👩🏻‍💼📑Низоларни судгача (медиация), ҳакамлик ва арбитраж муҳокамалари орқали ҳал қилишга кўмаклашиш - 96\n\n"
                             "📑📈📊“YERELEKTRON” ва “E-IJRO-AUKSION” электрон автоматлаштирилган тизимларидан фойдаланишда маслаҳат ва маълумот бериш - 35")

    
    #await msg.answer("Ариза қолдиришни истайсизми?", reply_markup=kb.ariza)
    await state.update_data({'ish':ish})
    await msg.answer("Исмингизни киритинг:", reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(state=Form.ism)
async def ism(msg: types.Message, state:FSMContext):
    ism=msg.text
    await state.update_data({'ism':ism})

    await msg.answer("Фирмангизни тўлик номини киритинг:", reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(state=Form.firma)
async def firma(msg: types.Message, state:FSMContext):
    firma=msg.text
    await state.update_data({'firma':firma})

    await msg.answer("(STIR)ИНН рақамини киритинг:", reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(lambda message: not len(message.text) == 9, state=Form.inn)
async def inn_invalid(message: types.Message):
    return await message.reply("(STIR)ИНН рақами нотўғри киритилди!\n")

@dp.message_handler(lambda message: message.text.isdigit(), state=Form.inn)
async def inn(msg: types.Message, state:FSMContext):
    inn=msg.text
    await state.update_data({'inn':inn})

    await msg.answer("Телефон рақамингизни киритинг:", reply_markup=kb.Main)
    await Form.next()

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.tel)
async def tel_invalid(message: types.Message):
    return await message.reply("Телефон рақами нотўғри киритилди!")

@dp.message_handler(lambda message: message.text.isdigit(), state=Form.tel)
async def tel(msg: types.Message, state:FSMContext):
    tel=msg.text
    #await state.update_data(tel=int(msg.text))
    await state.update_data({'tel':tel})
    data = await state.get_data()
    xabar = f"Хизмат тури: {data['ish']}\n"\
            f"Исми: {data['ism']}\n"\
            f"Фирма номи: {data['firma']}\n"\
            f"Инн рақами: {data['inn']}\n"\
            f"Телефон рақами: {data['tel']}\n"
    await bot.send_message(chat_id=-1001746692435, text=f"{xabar}")
    await msg.answer("✅ Аризангиз қабул қилинди, тез орада алоқага чиқилади", reply_markup=kb.mainmenu)
    await state.finish()


@dp.message_handler()
async def uzb(message: types.Message):
    if message.text == "✅ Хизмат турлари":
        await message.answer("Хизмат турларини танланг!", reply_markup=kb.ish)
    if message.text == "🔙 Орқага":
        await message.reply("Бош саҳифа", reply_markup=kb.mainmenu)
    if message.text == "👤 Биз ҳақимизда":
        await message.reply("🇺🇿Узбекистон Республикаси Савдо-саноат палатаси Узбекистон Републикаси  Адлия Вазирлигида 1998 йил 28 декабр 353-сон билан руйхатга олинган ва кайта ташкил қилинган\n\n"
                            "Палата куйидаги максадларда тузилади:📑\n\n"
                            "тадбиркорликни янада ривожлантириш учун кулай шарт-шароит яратиш;\n📈бизнес-мухитни такомиллаштириш;\n"
                            "республика тадбиркорларининг хорижий хамкорлар билан ишбилармонлик алокаларини мустахкамлаш👩🏻‍💻🧑🏻‍💻"
                            "махаллий товарлар ва хизматларни ташки бозорларга олиб чикиш;\nтайёр ракобатбардош махсулотлар ишлаб чикарилишини таъминлаш учун янги корхоналарни ташкил этиш, мавжуд ишлаб чикаришларни техник кайта жихозлаш ва замонавийлаштириш учун республикага чет эл сармоясини кенг жалб этиш💸;🏢💵\n"
                            "Узбекистон Республикаси иктисодий тараккиётига, унинг жахон хужалик тизимига уйгунлашишига, Узбекистон тадбиркорларининг бошка мамлакат тадбиркорлари билан савдо-сотик ва илмий-техник алокаларини Урнатишга кумаклашиш;🌍💵💰\n"
                            "Палата аъзоларини бирлаштириш ва куллаб-кувватлаш;\nтадбиркорлик субъектлари — Палата аъзоларининг манфаатларини ифода этиш ва хукукларини химоя килиш;\nбозор инфратузилмасининг яхлит тизимини шакллантириш.🧑🏻‍💻🤝👩🏻‍💻📑🧾"
                            "Тадбиркорларнинг хуқуқларини химоя қилиш сохасида тадбиркорлик субьектларини, айниқса ўз фаолиятини йўлга кўйиш даврида уларни кўллаб - кувватлашнинг самарали тизимини яратиш, уларнинг хуқуқлари ва конуний манфаатлари ишончли мухофазасининг кафолатларини кучайтириш, жадал ривожланишига хар томонлама кўмак бериш, хусусий мулк ва тадбиркорликнинг устуворлик роли ва дахлсизлигини таъминлаш, республикамиз туманлари ва шахарларида ахолини тадбиркорлик фаолиятига  кенг жалб қилиш.🧑🏻‍💻💵"
                            "тадбиркорлик фаолиятига кумаклашиш сохасида тадбиркорлик объектларига бизнесни ташкил этиш,🏢💸 юритиш ва янада ривожлантиришда амалий ёрдам курсатиш,🧑🏽‍💻📈 давлат органлари ва бозор инфратузилмаси субъектлари хизматларидан фойдаланиш бўйича имкониятлар ва шароитлар яратиш, маслахат ёрдами ва ахборот таъминотини такдим этишда куйидагилар оркали кўмаклашиш\n\n"
                            "🇺🇿Ўзбекистон Савдо-Саноат палатаси\n"
                            "🧑🏻‍💻Тошкент вилояти худудий бошқармаси\n"
                            "🏢Манзил:Тошкент шахар, Яккасарой тумани\n"
                            "Ш.Руставели кўч. 22-уй ИНДЕКС 10070\n"
                            "📑STIR: 201 806 983   OKED 94110\n"
                            "📞Тел: 95 202-16-16 Юридик сектор🕵🏻‍♂️🕵🏻\n"
                            "📞Тел:95 202-21-21 Қабул хона👩🏻‍💼", reply_markup=kb.mainmenu)
    if message.text == "🇺🇿Узб-Uzb/🇷🇺Рус-Rus":
        await message.reply("Язык изменился")
        await message.answer("Добро пожаловать в Ташкентское региональное отделение Торгово-промышленной палаты", reply_markup=kb.mainmenu2)
        

    if message.text == "✅ Виды услуг":
        await message.answer("Выбор типов услуг.", reply_markup=kb.ish2)
    if message.text == "🔙 Назад":
        await message.reply("Домашняя страница",reply_markup=kb.mainmenu2)
    if message.text == "👤 О нас":
        await message.reply("Ўзбекистон Савдо-Саноат палатаси"
                            " Тошкент вилояти худудий бошқармаси.\n"
                            "Манзил:Тошкент шахар, Яккасарой тумани\n"
                            "Ш.Руставели кўч. 22-уй ИНДЕКС 10070\n"
                            "STIR: 201 806 983   OKED 94110\n"
                            "Тел: 95 202-16-16 Юридик сектор\n"
                            "Тел:95 202-21-21 Қабул хона",reply_markup=kb.mainmenu2)
    if message.text == "🇷🇺Рус-Rus/🇺🇿Узб-Uzb":
        await message.reply("Тил ўзгарди", reply_markup=kb.mainmenu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
