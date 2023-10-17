from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardRemove
)
from config import Tokens,Price

remove_kb = ReplyKeyboardRemove()

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
            InlineKeyboardButton(text=f"1 неделя - {Price.week} р",callback_data='week')
        ],
        [
            InlineKeyboardButton(text=f"2 недели - {Price.month} р",callback_data='month')
        ],
        [
            InlineKeyboardButton(text=f"3 недели - {Price.threeMonth} р",callback_data='threeMonth')
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


