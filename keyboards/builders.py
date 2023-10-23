from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
import requests,random
from config import RuKassa,Tokens
import asyncio
from data import db_admin
db = db_admin.DatabaseAdmin('autopay.db')



async def create_kb_payment(sum):
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

async def create_price_kb():
    price = await db.getPrice()
    buy_sub = InlineKeyboardBuilder()
    buy_sub.button(text=f"1 неделя - {price[0]} р",callback_data='week')
    buy_sub.button(text=f"1 месяц - {price[1]} р",callback_data='month')
    buy_sub.button(text=f"3 месяца - {price[2]} р",callback_data='threeMonth')
    return buy_sub.as_markup()




# buy_sub = InlineKeyboardMarkup(
#     inline_keyboard = [
#         [
#             InlineKeyboardButton(text=f"1 неделя - {db.getPrice()[p]} р",callback_data='week')
#         ],
#         [
#             InlineKeyboardButton(text=f"2 недели - {price[1]} р",callback_data='month')
#         ],
#         [
#             InlineKeyboardButton(text=f"3 недели - {price[2]} р",callback_data='threeMonth')
#         ]
#     ]
# )