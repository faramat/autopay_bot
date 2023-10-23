from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")  # Образ шедулера
start_status = True  # Оповещение админам о запуске бота (True или False)


class Tokens():
    bot_token = '6198074177:AAElHxTlJkKiFAXNRIkHoL0pumapRXSwubA'
    bot_url = 'https://t.me/sdfokosdofk_bot'
    admin_id = '1983853146'
    private_free_channel_id = '-1001596306304'
    private_free_channel_url = 'https://t.me/+TvypGRWl4RQ1YmZi'
    private_channel_id = '-1001973605743'
    private_channel_url = 'https://t.me/+5wTgR-jMQjYyZDgy' #создать пригласительную ссылку!!!
    # YooMoney


class RuKassa():
    payment_url = 'https://lk.rukassa.is/api/v1/create/'
    check_order_url = 'https://lk.rukassa.is/api/v1/getPayInfo/'
    shop_id= '1412'
    token = '20b2eabfc91dc99ae0fdb61abf92d85f'

