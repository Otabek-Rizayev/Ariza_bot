from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton


btnMain = KeyboardButton("🔙 Орқага")
Main = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)

ar = KeyboardButton("📝 Ариза қолдириш")
ariza = ReplyKeyboardMarkup(resize_keyboard=True).add(ar).add(btnMain)

xizmat = KeyboardButton("✅ Хизмат турлари")
biz = KeyboardButton("👤 Биз ҳақимизда")
uz = KeyboardButton("🇺🇿Узб-Uzb/🇷🇺Рус-Rus")
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(xizmat).add(biz, uz)

ex = KeyboardButton("Экспортга кўмаклашиш")
kur = KeyboardButton("Кўргазма")
biz = KeyboardButton("Бизнес режа тайёрлаш")
yur = KeyboardButton("Юридик масалалар")
ish = ReplyKeyboardMarkup(resize_keyboard=True).add(ex, kur).add(biz, yur).add(btnMain)

btnMain2 = KeyboardButton("🔙 Назад")
Main2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain2)

xizmat2 = KeyboardButton("✅ Виды услуг")
biz2 = KeyboardButton("👤 О нас")
ru = KeyboardButton("🇷🇺Рус-Rus/🇺🇿Узб-Uzb")
mainmenu2 = ReplyKeyboardMarkup(resize_keyboard=True).add(xizmat2).add(biz2, ru)

ex2 = KeyboardButton("Продвижение экспорта")
kur2 = KeyboardButton("Выставки")
biz2 = KeyboardButton("Бизнес-план")
yur2 = KeyboardButton("Юридические проблемы")
ish2 = ReplyKeyboardMarkup(resize_keyboard=True).add(ex2, kur2).add(biz2, yur2).add(btnMain2)



