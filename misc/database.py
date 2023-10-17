
from aiogram import Bot
from config import Tokens
from data import *


db_check_subscription = db_user_payment.DatabaseUserPay('autopay.db')


async def startup_notify(bot: Bot):
        await bot.send_message(chat_id=Tokens.admin_id, text="<b>✅ Bot was started</b>")


async def check_subscription():
        pass
        # Проверка подписок, сравнить время в секундах сегодня и date_end у всех юзеров дб.
        # Если время отрицательное, оставить подписку, иначе sub_active = 0 + кикаем юзера с приватки