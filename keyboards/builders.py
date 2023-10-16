from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
import requests,random
from config import YooMoney,Tokens


def create_kb_payment(sum):
    url = YooMoney.payment_url
    label = random.randint(10000000000,99999999999)
    params = {
        'receiver':f'{YooMoney.payment_wallet}',
        'quickpay-form':'button',
        'paymentType':'AC',
        'sum':f'{sum}',
        'label':f'{label}',
        'successURL':f'{Tokens.bot_url}'
    }
    response = requests.post(url,params=params)
    builder = InlineKeyboardBuilder()
    builder.button(text='Оплатить',url=f'{response.url}',callback_data='pressed_pay_button')
    return builder.as_markup(),label