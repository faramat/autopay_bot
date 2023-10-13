import random,asyncio
from aiogram import Router, Bot,F
from aiogram.types import Message,ChatJoinRequest
from aiogram.filters import Command,CommandStart    
from keyboards import reply,inline
from data import *
from config import Tokens

router = Router()
db = db_user_start_bot.DatabaseUser('autopay.db')
db_check_active_sub = db_user_sub.DatabaseUserSub('autopay.db')
bot = Bot(Tokens.bot_token,parse_mode="HTML")

# проверка подписки на канал
async def check_sub_channel(user_id):
    if 'left' in str((await bot.get_chat_member(chat_id=Tokens.private_free_channel_id,user_id=user_id))):
        return True
    else: 
        return False
# автопринятие подписки тг канал
@router.chat_join_request()
async def approve_chat_join(update: ChatJoinRequest):
    if update.chat.id == Tokens.private_free_channel_id: # если запрос в бесплатный канал
        await update.approve()
        await bot.send_message(Tokens.admin_id,f'@{update.from_user.username} подписался в бесплатный канал')
    else: # если в платный
        if db_check_active_sub.check_sub(update.from_user.id):
             await update.approve()
        else:
             pass
# команда /start
@router.message(CommandStart())
async def start(message: Message):
    # await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    if (not db.user_exists_start(message.from_user.id)): #Регистрация пользователя 
        db.user_start(message.from_user.id,f"@{message.from_user.username}")
        await start(message)
    else: # Пользователь зарегистрирован
        if await check_sub_channel(message.from_user.id):
            await message.answer("Сначала нужно подписаться на канал",reply_markup=inline.links_sub)       
        else:
            await message.answer('Воспользуйтесь навигацией:',reply_markup=reply.main)

@router.message(F.text == 'Профиль')
async def profile(message: Message):
            if await check_sub_channel(message.from_user.id):
                await message.answer("Сначала нужно подписаться на канал",reply_markup=inline.links_sub)
            else:
                if db_check_active_sub.check_sub(message.from_user.id): #платная подписка есть
                    await message.answer(f'''
Подписка : активна
Закончится через:
----                                  
                ''',reply_markup=inline.join_private_channel)
                else: #платной подписки нет
                    await message.answer("Привет! Чтобы получить эксклюзивный и сочный контент, приобретите подписку.",reply_markup=inline.buy_sub)

@router.message(F.text == 'Купить подписку')
async def buy_subcription(message: Message):
            if await check_sub_channel(message.from_user.id):
                await message.answer("Сначала нужно подписаться на канал",reply_markup=inline.links_sub)
            else:
                if db_check_active_sub.check_sub(message.from_user.id): #платная подписка есть
                    await message.answer(f'''
Подписка : активна
Закончится через:
----                                  
                ''',reply_markup=inline.join_private_channel)
                else: #платной подписки нет
                    await message.answer("Чтобы купить подписку на приватный канал, выбери срок подписки",reply_markup=inline.buy_sub)
        



