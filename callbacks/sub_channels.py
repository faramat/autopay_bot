from aiogram import Router,F
from aiogram.types import CallbackQuery
from keyboards import fabrics
from handlers.user_commands import check_sub_channel,start
from keyboards.inline import links_sub
router = Router()


@router.callback_query(F.data == 'sub_channel_free')
async def check_sub_to_free_channel(call: CallbackQuery):
    if await check_sub_channel(call.from_user.id):
        await call.answer("Сначала нужно подписаться на канал",reply_markup=links_sub)    
    else:
        await start(call.message)
