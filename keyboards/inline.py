from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardRemove
)
from config import Tokens

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
            InlineKeyboardButton(text="1 неделя - 300 р")
        ],
        [
            InlineKeyboardButton(text="2 недели - 600 р")
        ],
        [
            InlineKeyboardButton(text="3 недели - 900 р")
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
