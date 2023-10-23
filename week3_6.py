import requests
import json

url = 'https://api.coingecko.com/api/v3/exchange_rates'

response = requests.get(url)

print(response)
# <Response [200]

if response.status_code == 200:
    print(response.headers)
    print("Coingecko specific header: ")
    print("Date: ", response.headers.get('date'))
    # Date:  Mon, 23 Oct 2023 13:12:44 GMT
    print("Access-Control-Allow-Methods: ", response.headers['Access-Control-Allow-Methods'])
    # Access-Control-Allow-Methods:  POST, PUT, DELETE, GET, OPTIONS
else:
    print(response.status_code)
    response.headers['Content-Encoding']


response.text
print(type(response))
# <class 'requests.models.Response'>
print(response.json())

content = json.loads(response.text)
print(type(content))
# <class 'dict'>
print(content['rates'])

jsonDump = json.dumps(content, indent=4)
print(jsonDump)
# {'rates' :}
betterJsonDump = json.dumps(content, indent=4, separators=('. ', '= '))
print(betterJsonDump)
# {'rates' =}