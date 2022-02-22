import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import keyboards as kb
API_TOKEN = '5156800116:AAFmF0RALm3ZYCGqHhWsYnnJvJSDXZXEyhM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#storage = MemoryStorage()
#dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Савдо-Саноат палатаси Тошкент вилояти Худудий бошқармасига хуш келибсз", reply_markup=kb.mainmenu)


@dp.message_handler()
async def uzb(message: types.Message):
    if message.text == "✅ Xizmat turlari":
        await message.answer("Xizmat turlarini tanlang.", reply_markup=kb.ish)
    if message.text == "🔙 Orqaga":
        await message.reply("Bosh sahifa",reply_markup=kb.mainmenu)
    if message.text == "👤 Biz haqimizda":
        await message.reply("Ўзбекистон Савдо-Саноат палатаси"
                            " Тошкент вилояти худудий бошқармаси.\n"
                            "Манзил:Тошкент шахар, Яккасарой тумани\n"
                            "Ш.Руставели кўч. 22-уй ИНДЕКС 10070\n"
                            "STIR: 201 806 983   OKED 94110\n"
                            "Тел: 95 202-16-16 Юридик сектор\n"
                            "Тел:95 202-21-21 Қабул хона",reply_markup=kb.Main)
    if message.text == "🇺🇿Узб-Uzb/🇷🇺Рус-Rus":
        await message.reply("Язык изменился")
        await message.answer("Добро пожаловать в Ташкентское региональное отделение Торгово-промышленной палаты", reply_markup=kb.mainmenu2)
        

    if message.text == "✅ Виды услуг":
        await message.answer("Выбор типов услуг.", reply_markup=kb.ish2)
    if message.text == "🔙 Назад":
        await message.reply("Домашняя страница",reply_markup=kb.mainmenu2)
    if message.text == "👤 Насчет нас":
        await message.reply("Ўзбекистон Савдо-Саноат палатаси"
                            " Тошкент вилояти худудий бошқармаси.\n"
                            "Манзил:Тошкент шахар, Яккасарой тумани\n"
                            "Ш.Руставели кўч. 22-уй ИНДЕКС 10070\n"
                            "STIR: 201 806 983   OKED 94110\n"
                            "Тел: 95 202-16-16 Юридик сектор\n"
                            "Тел:95 202-21-21 Қабул хона",reply_markup=kb.Main2)
    if message.text == "🇷🇺Рус-Rus/🇺🇿Узб-Uzb":
        await message.reply("Til o`zgardi", reply_markup=kb.mainmenu)


    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
