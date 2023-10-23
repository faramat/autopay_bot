import asyncio
from aiogram import Bot,Dispatcher,F
from handlers import user_commands,admin
from config import Tokens,scheduler
from data import db_start as db
from callbacks import sub_channels,payments
from misc.database import startup_notify,check_subscription
import logging

async def scheduler_start(bot):
    scheduler.add_job(check_subscription, "interval", hours = 12, args=(bot,))  # Ежедневная проверка подписок

bot = Bot(Tokens.bot_token,parse_mode="HTML")

async def main():
    scheduler.start()
    db.sql_start()
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        sub_channels.router,
        payments.router,
        admin.router
    )
    await startup_notify(bot)
    await check_subscription(bot)
    await scheduler_start(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    logging.basicConfig(level=logging.DEBUG)

    