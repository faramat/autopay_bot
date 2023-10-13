import asyncio
from aiogram import Bot,Dispatcher,F
from handlers import user_commands
from config import Tokens
from data import db_start as db
from callbacks import sub_channels
from handlers.user_commands import approve_chat_join
from flask import Flask,request,Response

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def check_payment():
    print(request.json)
    print('test')

async def main():
    # db.sql_start()


    # bot = Bot(Tokens.bot_token,parse_mode="HTML")
    # dp = Dispatcher()
    # dp.include_routers(
    #     user_commands.router,
    #     sub_channels.router,
        
    # )
    # await bot.delete_webhook(drop_pending_updates=True)
    # res = await bot.set_webhook('https://f15f-2a03-d000-8504-5a02-8488-c01b-96dd-f24b.ngrok-free.app')
    # print(res)
    # await dp.start_polling(bot)
    app.run()



if __name__ == "__main__":
    asyncio.run(main())
    
    