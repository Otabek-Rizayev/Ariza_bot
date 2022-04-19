from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import loader
from pathlib import Path
from main import dp, bot, _
from lang import LANGS, LANG_STORAGE, Localization

btnMain = KeyboardButton(_("🔙 Back"))
Main = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)
ar = KeyboardButton(_("📝 Leave an application"))
ariza = ReplyKeyboardMarkup(resize_keyboard=True).add(ar).add(btnMain)
xizmat = KeyboardButton(_("✅ Types of services"))
biz = KeyboardButton(_("👤 About us"))
ch = KeyboardButton("🇺🇿UZ|🇷🇺RU|🇬🇧ENG")
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(xizmat).add(biz, ch)
ex = KeyboardButton(_("Export assistance"))
kur = KeyboardButton(_("Exhibition"))
biz = KeyboardButton(_("Preparation of a business plan"))
yur = KeyboardButton(_("Legal issues"))
ish = ReplyKeyboardMarkup(resize_keyboard=True).add(ex, kur).add(biz, yur).add(btnMain)

uz = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="🇺🇿 O'zbekcha")
ru = InlineKeyboardButton(text="🇷🇺 Русский", callback_data="🇷🇺 Русский")
eng = InlineKeyboardButton(text="🇬🇧 English", callback_data="🇬🇧 English")
til = InlineKeyboardMarkup(row_width=3).add(uz, ru, eng)
