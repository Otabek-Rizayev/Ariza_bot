from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

btnMain = KeyboardButton("🔙 Orqaga")
Main = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)

#ariza = KeyboardButton("📝 Ariza yuborish")
xizmat = KeyboardButton("✅ Xizmat turlari")
biz = KeyboardButton("👤 Biz haqimizda")
uz = KeyboardButton("🇺🇿Узб-Uzb/🇷🇺Рус-Rus")
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(xizmat).add(biz, uz)

ex = KeyboardButton("Eksportga ko`maklashish")
kur = KeyboardButton("Ko`rgazama")
biz = KeyboardButton("Biznes reja tayyorlash")
yur = KeyboardButton("Yuridik masalalar")
ish = ReplyKeyboardMarkup(resize_keyboard=True).add(ex, kur).add(biz, yur).add(btnMain)

btnMain2 = KeyboardButton("🔙 Назад")
Main2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain2)

xizmat2 = KeyboardButton("✅ Виды услуг")
biz2 = KeyboardButton("👤 Насчет нас")
ru = KeyboardButton("🇷🇺Рус-Rus/🇺🇿Узб-Uzb")
mainmenu2 = ReplyKeyboardMarkup(resize_keyboard=True).add(xizmat2).add(biz2, ru)

ex2 = KeyboardButton("Продвижение экспорта")
kur2 = KeyboardButton("Выставка")
biz2 = KeyboardButton("Бизнес-план")
yur2 = KeyboardButton("Юридические проблемы")
ish2 = ReplyKeyboardMarkup(resize_keyboard=True).add(ex2, kur2).add(biz2, yur2).add(btnMain2)



"""
tosh = KeyboardButton("Toshkent Shahri/Viloyati")
an = KeyboardButton("Andijon viloyati")
bux = KeyboardButton("Buxoro viloyati")
far = KeyboardButton("Fargʻona viloyati")
jiz = KeyboardButton("Jizzax viloyati")
xor = KeyboardButton("Xorazm viloyati")
nam = KeyboardButton("Namangan viloyati")
nav = KeyboardButton("Navoiy viloyati")
qash = KeyboardButton("Qashqadaryo viloyati")
sam = KeyboardButton("Samarqand viloyati")
sir = KeyboardButton("Sirdaryo viloyati")
sur = KeyboardButton("Surxondaryo viloyati")
viloyat = ReplyKeyboardMarkup(resize_keyboard=True).add(tosh,an,bux,far,jiz,xor,nam,nav,qash,sam,sir,sur, btnMain)"""
