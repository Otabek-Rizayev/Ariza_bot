from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
import loader
from pathlib import Path
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from main import dp, bot, _

btnMain = KeyboardButton(_("🔙 Орқага"))
Main = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)

ar = KeyboardButton(_("📝 Ариза қолдириш"))
ariza = ReplyKeyboardMarkup(resize_keyboard=True).add(ar).add(btnMain)

xizmat = KeyboardButton(_("✅ Хизмат турлари"))
biz = KeyboardButton(_("👤 Биз ҳақимизда"))
til = KeyboardButton("Til")
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(xizmat).add(biz, til)

ex = KeyboardButton(_("Экспортга кўмаклашиш"))
kur = KeyboardButton(_("Кўргазма"))
biz = KeyboardButton(_("Бизнес режа тайёрлаш"))
yur = KeyboardButton(_("Юридик масалалар"))
ish = ReplyKeyboardMarkup(resize_keyboard=True).add(ex, kur).add(biz, yur).add(btnMain)