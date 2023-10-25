
from aiogram import Bot
from config import Tokens
from data import *
from aiogram.types import FSInputFile
from datetime import datetime
db_check_subscription = db_user_payment.DatabaseUserPay('autopay.db')
db_check_date_end = db_user_sub.DatabaseUserSub('autopay.db')

async def startup_notify(bot: Bot):
        await bot.send_message(chat_id=Tokens.admin_id, text="<b>✅ Bot was started</b>")


# Проверка времени для обновления статуса подписки 
async def check_subscription(bot: Bot):     
        await db_check_date_end.check_date_end(bot)

# Автоматические бэкапы БД
async def autobackup_admin(bot: Bot):
        try:
            await bot.send_document(
                Tokens.admin_id,
                FSInputFile('autopay.db'),
                caption=f"<b>📦 AUTOBACKUP</b>\n"
                        f"🕰 <code>{datetime.today()}</code>",
            )
        except:
            pass