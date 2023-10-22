from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    ReplyKeyboardRemove
)

rmk = ReplyKeyboardRemove()



main = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Профиль"),
            KeyboardButton(text="Купить подписку")
            
        ]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True, #убирается кб после 1 использования
    selective=True #активация кб у того, кто ее вызвал
)

admin_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Обновить прайс"),
            KeyboardButton(text="Дб")
            
        ]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True, #убирается кб после 1 использования
    selective=True #активация кб у того, кто ее вызвал
)
