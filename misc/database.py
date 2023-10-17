
from aiogram import Bot
from config import Tokens




async def startup_notify(bot: Bot):
        await bot.send_message(chat_id=Tokens.admin_id, text="<b>✅ Bot was started</b>")