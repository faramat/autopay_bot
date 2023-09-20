#----
#ТГ
from create_bot import dp, bot
from aiogram import types, Dispatcher
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove,CallbackQuery
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
#БД
from data_base import main_requests
#Клавиатуры
from keyboards import *
#Машина состояний 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup 
#Другое

#----

async def start(message: types.Message):
    await message.answer('Welcome!',reply_markup=user_kb.start_kb)
    await message.answer('Select Sub ->', reply_markup=user_kb.subs_kb)

async def one_month(query: types.CallbackQuery):
    umoney_kb = InlineKeyboardMarkup()
    price = InlineKeyboardButton('Оплатить подписку', callback_data='buy')
    umoney_kb.row(price)
    await query.bot.edit_message_text(
        text='Price 300 rub',
        chat_id=query.from_user.id,
        message_id=query.message.message_id,
        reply_markup=umoney_kb
    )

async def buy(call: types.CallbackQuery):
    pass
# class fsmSearchFio(StatesGroup):
#     surname = State()
#     name = State()
#     patronymic = State()

# async def search_fio(message: types.Message):
#     await message.answer('Введите фамилию сотрудника:',reply_markup=user_kb.inline_user_keyboard_forgot_surname) 
#     await fsmSearchFio.surname.set()

# async def search_surname(message: types.Message, state: FSMContext):
#     await state.update_data(surname=message.text)
#     data = await state.get_data()
#     if data['surname']:
#         response = main_requests.search_surname(data)
#         await message.answer(f'''По запросу {data['surname']} было найдено {response[0]} сотрудников''')
#     await message.answer('Введите имя сотрудника:',reply_markup=user_kb.inline_user_keyboard_forgot_name) 
#     await fsmSearchFio.next()

# async def forgot_patronymic(query: types.CallbackQuery,state: FSMContext):
#     await state.update_data(patronymic=None)
#     data = await state.get_data()
#     await state.finish()
#     await query.message.delete()
#     await get_info(query.message,data)
    
    

#регистрация функций для дальнейшей передачи
def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(start,commands = ['start'])
    dp.register_callback_query_handler(one_month,text = "one_month")
    dp.register_callback_query_handler(buy,text = "buy")

    # dp.register_message_handler(search_fio,text = "Поиск по ФИО",state=None)
    # dp.register_message_handler(search_surname,state=fsmSearchFio.surname)
