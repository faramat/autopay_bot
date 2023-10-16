import requests,json




url = 'https://yoomoney.ru/api/oauth/authorize'
params = {
    'client_id':'C8D02963670FD08F1F4CDEF48C8EAD305ACADBE848E63F6E58F5A709205B410A',
    'response_type':'code',
    'redirect_uri':'https://google.com',
    'scope':'account-info operation-history operation-details'
}
response = requests.post(url,params=params)
print(response.url)
