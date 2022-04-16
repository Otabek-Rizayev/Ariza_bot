from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types
from pathlib import Path
from typing import Tuple, Any

LANGS = ['ru', 'uz', 'en']
LANG_STORAGE = {}

class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user: types.User = types.User.get_current()
        if LANG_STORAGE.get(user.id) is None:
            LANG_STORAGE[user.id] = "uz"
        *_, data_lang = args
        language = data_lang['locale'] = LANG_STORAGE[user.id]
        return language
