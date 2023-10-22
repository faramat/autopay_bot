
from aiogram import Bot
from config import Tokens
from data import *


db_check_subscription = db_user_payment.DatabaseUserPay('autopay.db')
db_check_date_end = db_user_sub.DatabaseUserSub('autopay.db')

async def startup_notify(bot: Bot):
        await bot.send_message(chat_id=Tokens.admin_id, text="<b>✅ Bot was started</b>")


# Проверка времени для обновления статуса подписки 
async def check_subscription(bot: Bot):     
        await bot.send_message(chat_id=Tokens.admin_id, text="<b>✅ Запущена проверка времени подписки</b>")   
        await db_check_date_end.check_date_end(bot)