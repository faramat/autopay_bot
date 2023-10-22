from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardRemove
)
from config import Tokens
from data import db_admin

remove_kb = ReplyKeyboardRemove()
db = db_admin.DatabaseAdmin('autopay.db')

price = db.getPrice()
links_sub = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="ПОДПИСАТЬСЯ!",url=f"{Tokens.private_free_channel_url}")
        ],
        [
            InlineKeyboardButton(text="Я ПОДПИСАЛСЯ",callback_data='sub_channel_free')
        ]
    ]
)

buy_sub = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text=f"1 неделя - {price[0]} р",callback_data='week')
        ],
        [
            InlineKeyboardButton(text=f"2 недели - {price[1]} р",callback_data='month')
        ],
        [
            InlineKeyboardButton(text=f"3 недели - {price[2]} р",callback_data='threeMonth')
        ]
    ]
)
join_private_channel = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Открыть приватный канал",url='t.me/+5wTgR-jMQjYyZDgy')
        ]
    ]
)


