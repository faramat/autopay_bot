import asyncio
from aiogram import Bot,Dispatcher,F
from handlers import user_commands
from config import Tokens,scheduler
from data import db_start as db
from callbacks import sub_channels,payments
from misc.database import startup_notify


async def scheduler_start(bot):
    scheduler.add_job(startup_notify, "interval", seconds = 10, args=(bot,))  # Ежедневный Автобэкап в 00:00
    # scheduler.add_job(autobackup_admin, "cron", hour=12, args=(bot,))  # Ежедневный Автобэкап в 12:00

bot = Bot(Tokens.bot_token,parse_mode="HTML")

async def main():
    scheduler.start()
    db.sql_start()
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        sub_channels.router,
        payments.router
    )
    await startup_notify(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
    