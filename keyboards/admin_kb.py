from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
#клавиатура администратора
admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_admins = KeyboardButton('Test1')
admin_keyboard.row(button_admins)
#Инлайн клавиатура
inline_finded_keyboard = InlineKeyboardMarkup()
button_change_tg_id_parent = InlineKeyboardButton('Test', callback_data='test')
inline_finded_keyboard.row(button_change_tg_id_parent)