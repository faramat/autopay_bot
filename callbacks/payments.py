from aiogram import Router,F
from aiogram.types import CallbackQuery
from keyboards import fabrics
from handlers.user_commands import check_sub_channel,start
from keyboards.inline import links_sub
from keyboards import builders,inline
from config import Price,RuKassa
from main import bot
import requests,time
import datetime
from data import *

router = Router()
db_check_active_pay = db_user_payment.DatabaseUserPay('autopay.db')


async def check_order(id):
    time.sleep(30)
    url = RuKassa.check_order_url
    params = {
    'id':f'{id}',
    'shop_id':f'{RuKassa.shop_id}',
    'token':f'{RuKassa.token}',
    }
    for i in range(20):    
        response = (requests.post(url,params=params)).json() 
        if response['status'] == "PAID":
            return True
        else:
            time.sleep(30)
    return False        

@router.callback_query(F.data == 'one')
async def check_sub_to_free_channel(call: CallbackQuery):
    kb , id = builders.create_kb_payment(Price.one)
    await call.message.edit_text(text="После оплаты средства зачислять автоматически, ссылка активна 10 минут")
    await call.message.edit_reply_markup(reply_markup=kb)
    if await check_order(id):
        today = datetime.datetime.now()
        date_pay = (int(today.timestamp()))
        delta = datetime.timedelta(days=7)
        date_end = today + delta
        date_end = int(date_end.timestamp())
        db_check_active_pay.activate_sub(call.from_user.id,date_pay,date_end)
        await call.message.answer("Подписка активирована",reply_markup=inline.join_private_channel)
    else:
        await call.message.answer("Ссылка на оплату не активна, создайте новую")

