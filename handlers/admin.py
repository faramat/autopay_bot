import random,asyncio,json
from aiogram import Router, Bot,F
from aiogram.types import Message
from data import *
from config import Tokens
from keyboards import reply
from aiogram.fsm.context import FSMContext
from utils.states import Form

router = Router()
db = db_admin.DatabaseAdmin('autopay.db')
bot = Bot(Tokens.bot_token,parse_mode="HTML")


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
        await state.set_state(Form.first_sum)
        await message.answer("Введите цену за неделю подписки (пример: 100)")


@router.message(Form.first_sum)
async def update_price_first_sum(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        await state.update_data(first_sum=message.text)
        await state.set_state(Form.second_sum)
        await message.answer("Введите цену за месяц подписки (пример: 300)")


@router.message(Form.second_sum)
async def update_price_second_sum(message: Message,state = FSMContext):
    if str(message.from_user.id) == Tokens.admin_id:
        await state.update_data(second_sum=message.text)
        await state.set_state(Form.third_sum)
        await message.answer("Введите цену за 3 месяца подписки (пример: 600)")

@router.message(Form.third_sum)
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
        ''')
