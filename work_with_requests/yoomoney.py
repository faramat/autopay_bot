import requests,json




url = 'https://yoomoney.ru/quickpay/confirm'
client_id = '3F2B042CED54A545F1B23A7C9FABB9ACCB373F97D6BD7C7BC94F353EF581CCE9'
headerds = {

}
params = {
    'receiver':'4100116677873032',
    'quickpay-form':'button',
    'paymentType':'AC',
    'sum':'10',
    'label':'fdgrg42dsfcv4442',
    'successURL':'https://google.com/'
}
response = requests.post(url,headers=headerds,params=params)
print(response.url)

