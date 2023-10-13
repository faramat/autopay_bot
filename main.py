import asyncio
from aiogram import Bot,Dispatcher,F
from handlers import user_commands
from config import Tokens
from data import db_start as db
from callbacks import sub_channels
from handlers.user_commands import approve_chat_join
from flask import Flask,request,Response

app = Flask(__name__)

@app.route('/',methods = ["GET"])
def check_payment():
    print(request.json)

async def main():
    db.sql_start()
    bot = Bot(Tokens.bot_token,parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        sub_channels.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(Tokens.webhook_url)
    # await dp.start_polling(bot)
    app.run()
if __name__ == "__main__":
    asyncio.run(main())
    
    