import requests
from pprint import pprint

# response = requests.get('https://api.coingecko.com/api/v3/exchange_rates')
# pprint("Coingecko API headers:")
# print(response.headers)
# print("Date: ",response.headers.get('Date'))
# print("Content-Type: ",response.headers.get('Content-Type'))
# print("Content-Type: ",response.headers.get('content-type'))
# print("Access-Control-Allow-Methods: ",response.headers['Access-Control-Allow-Methods'])
# print("Access-Control-Allow-Methods: ",response.headers.get('Access-Control-Allow-Methods'))
# print("Access-Control-Request-Method: ",response.headers['Access-Control-Request-Method'])
# print("Content-Encoding: ",response.headers['Content-Encoding'])


# params = {'q':'stream', 'order':'length', 'min_width':'5000', 'min_height':'300'}
# url = 'https://catfact.ninja/fact'
# response = requests.get(url, json=params)

# print(response.status_code)
# # 200

# print(response.json())
# # {'fact': 'A cats field of vision is about 185 degrees.', 'length': 44}

query = [('q','Melbourne AU')]

url = 'https://openweathermap.org/find'

response = requests.get(url, params=query)

print(response.status_code)
# 200
print(response.url)
# https://openweathermap.org/find?q=Melbourne+AU
print(response.headers)

london = [('q', 'London UK')]
newYork = [('q', 'New York US')]
sydney = [('q', 'Sydney AU')]
capeTown = [('q','Cpae Town ZA')]

londonRequest = response = requests.get(url, params=london)
newYorkRequest = response = requests.get(url, params=newYork) 
sydneyRequest = response = requests.get(url, params=sydney) 
capeTownRequest = response = requests.get(url, params=capeTown)

print(londonRequest.url)
# https://openweathermap.org/find?q=London+UK
print(newYorkRequest.url)
# https://openweathermap.org/find?q=New+York+US
print(sydneyRequest.url)
# https://openweathermap.org/find?q=Sydney+AU
print(capeTownRequest.url)
# https://openweathermap.org/find?q=Cpae+Town+ZA



