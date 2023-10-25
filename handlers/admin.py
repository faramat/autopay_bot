import random,asyncio,json
from aiogram import Router, Bot,F
from aiogram.types import Message
from data import *
from config import Tokens
from keyboards import reply
from aiogram.fsm.context import FSMContext
from utils.states import form_price,form_send_messages
from misc.database import autobackup_admin


router = Router()
db = db_admin.DatabaseAdmin('autopay.db')
bot = Bot(Tokens.bot_token,parse_mode="HTML")


async def send_messages_without_photo(data):
    users = await db.get_users()
    counter_users = 0
    counter_messages = 0
    for row in users:
        try:
            await bot.send_message(chat_id=row[1],text=data['text'])
            counter_users+=1
            counter_messages+=1
        except:
            counter_users+=1
    await bot.send_message(chat_id=Tokens.admin_id,text = f'''
<b>Рассылка завершена</b>
Всего юзеров в БД - {counter_users}
Всего отправлено сообщений - {counter_messages}
''',reply_markup=reply.admin_kb)
    
async def send_messages_with_photo(data):
    users = await db.get_users()
    counter_users = 0
    counter_messages = 0
    for row in users:
        try:
            await bot.send_photo(chat_id=f'{row[1]}',photo=f'''{data['photo']}''',caption=f'''{data['text']}''')
            counter_users+=1
            counter_messages+=1
        except:
            counter_users+=1
    await bot.send_message(chat_id=Tokens.admin_id,text = f'''
<b>Рассылка завершена</b>
Всего юзеров в БД - {counter_users}
Всего отправлено сообщений - {counter_messages}
''',reply_markup=reply.admin_kb)

@router.message(F.text == 'Обновить прайс')
async def update_price(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        price = (await db.getPrice())
        await message.answer(f'''
Текущий прайс:
1 неделя - {price[0]}
1 месяц - {price[1]}
3 месяца - {price[2]}
        ''')
        await state.set_state(form_price.first_sum)
        await message.answer("Введите цену за неделю подписки (пример: 100)")


@router.message(form_price.first_sum)
async def update_price_first_sum(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        await state.update_data(first_sum=message.text)
        await state.set_state(form_price.second_sum)
        await message.answer("Введите цену за месяц подписки (пример: 300)")


@router.message(form_price.second_sum)
async def update_price_second_sum(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        await state.update_data(second_sum=message.text)
        await state.set_state(form_price.third_sum)
        await message.answer("Введите цену за 3 месяца подписки (пример: 600)")

@router.message(form_price.third_sum)
async def update_price_third_sum(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        await state.update_data(third_sum=message.text)
        data = await state.get_data()
        await state.clear()
        await db.updatePrice(data)

        price = (await db.getPrice())
        await message.answer(f'''
        Текущий прайс:
        1 неделя - {price[0]}
        1 месяц - {price[1]}
        3 месяца - {price[2]}
        ''',reply_markup=reply.admin_kb)


@router.message(F.text == 'Дамп БД')
async def dump_database(message: Message):
    if str(message.from_user.id) == Tokens.admin_id:
        await autobackup_admin(bot)    

@router.message(F.text == 'Рассылка пользователям')
async def send_messages(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        await message.answer('Пришлите текст поста',reply_markup=reply.rmk)
        await state.set_state(form_send_messages.text)
        # # users = await db.get_users()
        # for row in users:
        #     try:
        #         await message.answer()
        #     finally:
        #         print(row[0])


@router.message(form_send_messages.text)
async def update_text_send_messages(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        await state.update_data(text=message.text)
        await message.answer("Отправьте фото, если не нужно - 0 ")
        await state.set_state(form_send_messages.photo)



@router.message(form_send_messages.photo)
async def update_text_send_messages(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        if message.text == '0':
            await state.update_data(photo='0')
            data = await state.get_data()
            await state.clear()
            await send_messages_without_photo(data)
        else:
            await state.update_data(photo=message.photo[-1].file_id)
            data = await state.get_data()
            await state.clear()
            await send_messages_with_photo(data)