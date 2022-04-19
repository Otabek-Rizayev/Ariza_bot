from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types
from pathlib import Path
from typing import Tuple, Any

LANG_STORAGE = {}  
LANGS = {
    "🇺🇿 O'zbekcha": "uz",
    "🇷🇺 Русский":"ru",
    "🇬🇧 English": "en"
    }

class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user: types.User = types.User.get_current()
        if LANG_STORAGE.get(user.id) is None:
            LANG_STORAGE[user.id] = "uz"
        *_, data = args
        language = data['locale'] = LANG_STORAGE[user.id]
        return language
