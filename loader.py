from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
from pathlib import Path
from lang import Localization

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

I18N_DOMAIN = "tkmbot"
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / "locales"
i18n = Localization(I18N_DOMAIN, LOCALES_DIR)
dp.middleware.setup(i18n)
_ = i18n.lazy_gettext