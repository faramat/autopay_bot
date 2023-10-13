import requests,json




url = 'https://f15f-2a03-d000-8504-5a02-8488-c01b-96dd-f24b.ngrok-free.app'
client_id = '3F2B042CED54A545F1B23A7C9FABB9ACCB373F97D6BD7C7BC94F353EF581CCE9'
headerds = {

}
params = {
    'receiver':'4100116677873032',
    'quickpay-form':'button',
    'paymentType':'AC',
    'sum':'3',
    'label':'fdgrg42dsfcv4442',
    'successURL':'https://google.com/'
}
response = requests.get(url)
print(response.url)

