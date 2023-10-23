import requests, json

url = 'https://httpbin.org/get'
request = requests.get(url)

print(request.status_code)
#200
print(request)
# <Response [200]>
print(request.headers)
# {'Date': 'Mon, 23 Oct 2023 12:22:14 GMT', 'Content-Type': 'application/json', 'Content-Length': '307', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}

payload =  {'page':2, 'count':25}

r = requests.get(url, params=payload)

print(r.text)
print(r.url)
# https://httpbin.org/get?page=2&count=25


url = 'https://httpbin.org/post'
payload = {'username': 'foxtail', 'password': 'testing'}
# r = requests.post(url, json=payload)
# # "json": {
#     "password": "testing",
#     "username": "foxtail"
#   },

r = requests.post(url, data=payload)
#  "form": {
#     "password": "testing",
#     "username": "foxtail"
#   },
print(r.text)

print(r.json)
# <bound method Response.json of <Response [200]>>

r_dict = r.json()

print(r_dict['form'])
# {'password': 'testing', 'username': 'foxtail'}


payload = {'username': 'foxtail', 'password': 'testing'}
url = 'https://httpbin.org/basic-auth/foxtail/testing'

r = requests.get(url, auth=('foxtail', 'testing'))

print(r.text)

# {
#   "authenticated": true,
#   "user": "foxtail"
# }

r = requests.get(url, auth=('foxtale', 'testing'))
print(r)
# <Response [401]>


payload = {'username': 'foxtail', 'password': 'testing'}
url = 'https://httpbin.org/delay/1'
r = requests.get(url, timeout=3, auth=('foxtail','testing'))

print(r)
# <Response [200]>