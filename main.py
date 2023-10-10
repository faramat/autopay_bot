import asyncio
from aiogram import Bot,Dispatcher,F
from handlers import user_commands
from config import Tokens
from data import db_start as db
from callbacks import sub_channels
from handlers.user_commands import approve_chat_join

async def main():
    db.sql_start()

    bot = Bot(Tokens.bot_token,parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        sub_channels.router,
        
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())