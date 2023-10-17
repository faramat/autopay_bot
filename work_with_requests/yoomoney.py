import requests,json


id = '3354285'
shop_id = '1412'

url = 'https://lk.rukassa.is/api/v1/create/'
urlt = 'https://lk.rukassa.is/api/v1/getPayInfo/'
params = {
    'shop_id':'1412',
    'order_id':'10000000000',
    'amount':'100',
    'token':'20b2eabfc91dc99ae0fdb61abf92d85f'
}
paramst = {
    'id':'3354285',
    'shop_id':'1412',
    'token':'20b2eabfc91dc99ae0fdb61abf92d85f',
}
response = requests.post(urlt,params=paramst)
print(response.json())

