import requests

# data = {
#     'name': 'Umair',
#     'age': '30'
# }

# To add Data
# userdata = {
#     'username':'ImranTahir',
#     'password':'pucit.123++',
#     'password2':'pucit.123++',
#}
# response = requests.post('http://127.0.0.1:8000/api/user',json=userdata)
# response = requests.post('http://127.0.0.1:8000/api/get_token',json=userdata)
#

# token = response.json()['token']
# token_data = {"Authorization":f'token {token}'}
# r = requests.post('http://127.0.0.1:8000/auth/login/',json=userdata)
# # res = requests.get('http://127.0.0.1:8000/api/list')
# print(res)
# print(r.json()[0])

data = {
    'name': "ismail",
    'age': 32
}
# res = requests.post('http://127.0.0.1:8000/api/',json=data)
# print(res)

# r = requests.patch('http://127.0.0.1:8000/api/update/44469db8-541b-4b48-bc71-4f2542101cac',json={'age':32})



# This is for refresh Token

userdata = {
    'username': 'ImranTahir', 'password': 'pucit.123++',
}
acc_token = requests.post('http://127.0.0.1:8000/api/login', json=userdata).json()['access']
ref_token = requests.post('http://127.0.0.1:8000/api/login', json=userdata).json()['refresh']
headers = {"Authorization": f"Bearer {acc_token}"}
res = requests.get('http://127.0.0.1:8000/api/list', headers=headers)
print(res.json())
