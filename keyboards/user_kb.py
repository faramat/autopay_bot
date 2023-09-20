from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

#Клавиатура начальная
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
my_sub = KeyboardButton('Моя подписка')
tariffs = KeyboardButton('Тарифы')
contact = KeyboardButton('Написать администратору')
start_kb.row(my_sub).row(tariffs).row(contact)
#Инлайн клавиатура подписок 
subs_kb = InlineKeyboardMarkup()
one_month = InlineKeyboardButton('Купить подписку на 1 мес', callback_data='one_month')
three_month = InlineKeyboardButton('Купить подписку на 3 мес', callback_data='navigation')
forever = InlineKeyboardButton('Купить подписку навсегда', callback_data='create_program')
subs_kb.row(one_month).row(three_month).row(forever)
