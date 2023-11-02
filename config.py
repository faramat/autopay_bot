from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")  # Образ шедулера
start_status = True  # Оповещение админам о запуске бота (True или False)


class Tokens():
    bot_token = '6789528126:AAF5gnutLbX-4hHSj6q4aTFLPsf3oOh0tHA'
    bot_url = 'https://t.me/private_sliffki_bot'
    admin_id = '6383556618'
    private_free_channel_id = '-1001971370200'
    private_free_channel_url = 'https://t.me/+RCeXIiYXJlQzZWYy'
    private_channel_id = '-1001986343473'
    private_channel_url = 'https://t.me/+uBB23o4XHpE1YzVi' #создать пригласительную ссылку!!!
    # переходник - https://t.me/+EC77ffB92uxlNGVi


class RuKassa():
    payment_url = 'https://lk.rukassa.is/api/v1/create/'
    check_order_url = 'https://lk.rukassa.is/api/v1/getPayInfo/'
    shop_id= '1412'
    token = '20b2eabfc91dc99ae0fdb61abf92d85f'

