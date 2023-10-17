from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
import requests,random
from config import RuKassa,Tokens


def create_kb_payment(sum):
    url = RuKassa.payment_url
    order_id = random.randint(10000000000,99999999999)
    params = {
    'shop_id':f'{RuKassa.shop_id}',
    'order_id':f'{order_id}',
    'amount':f'{sum}',
    'token':f'{RuKassa.token}'
    }
    response = requests.post(url,params=params)
    url = response.json()['url']
    id = response.json()['id']
    builder = InlineKeyboardBuilder()
    builder.button(text='Оплатить',url=f'{url}',callback_data='pressed_pay_button')
    return builder.as_markup(),id