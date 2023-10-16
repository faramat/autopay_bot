from aiogram import Router,F
from aiogram.types import CallbackQuery
from keyboards import fabrics
from handlers.user_commands import check_sub_channel,start
from keyboards.inline import links_sub
from keyboards import builders
from config import Price,YooMoney
from main import bot
import requests,time


router = Router()


async def check_order(label):
    print(label)
    time.sleep(60)
    url = YooMoney.payment_url + "operation-history/"
    params = {
        'type':'deposition',
        'label':f'{label}'
    }
    response = requests.post(url,params=params)
    response = response.json()
    print(response)
    return True


@router.callback_query(F.data == 'one')
async def check_sub_to_free_channel(call: CallbackQuery):
    kb , label = builders.create_kb_payment(Price.one)
    await call.message.edit_text(text="После оплаты средства зачислять автоматически, ссылка активна 15 минут")
    await call.message.edit_reply_markup(reply_markup=kb)
    print(type(label))
    await call.message.answer(text=str(label))
    if await check_order(label):
        await call.message.answer("Подписка активирована")
    else:
        await call.message.answer("Ссылка на оплату не активна, создайте новую")

