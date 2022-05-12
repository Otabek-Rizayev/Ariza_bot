from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import loader
from pathlib import Path
from main import dp, bot, _
from lang import LANGS, LANG_STORAGE, Localization

btnMain = KeyboardButton(_("🔙 Orqaga"))
Main = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)


feed = KeyboardButton(_("💬 Adminga xabar qoldirish"))
ar = KeyboardButton(_("📝 Ariza qoldirish"))
biz = KeyboardButton(_("👤 Biz haqimizda"))
ch = KeyboardButton("🇺🇿UZ|🇷🇺RU|🇬🇧ENG")
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(feed, ar).add(biz, ch)

ex = KeyboardButton(_("Meneger"))
kur = KeyboardButton(_("Buxgalter"))
biz = KeyboardButton(_("Injiner"))
yur = KeyboardButton(_("Loyiha boshqaruvchisi"))
ish = ReplyKeyboardMarkup(resize_keyboard=True).add(ex, kur).add(biz, yur).add(btnMain)

uz = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="🇺🇿 O'zbekcha")
ru = InlineKeyboardButton(text="🇷🇺 Русский", callback_data="🇷🇺 Русский")
eng = InlineKeyboardButton(text="🇬🇧 English", callback_data="🇬🇧 English")
til = InlineKeyboardMarkup(row_width=3).add(uz, ru, eng)
