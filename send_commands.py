from aiogram import types

async def set_commands(dp):
    await dp.bot.send_my_commands(
        [
        types.BotCommand("start", "Botni ishga tushurish"),
        types.BotCommand("help", "Yodam")
        types.BotCommand("form", "ariza qoldirish")
        ]
        )
    
