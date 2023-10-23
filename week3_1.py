import requests, json

# Get cat api
response = requests.get('https://cat-fact.herokuapp.com/facts/random')
responseStatus = response.status_code
print(responseStatus)
responseJSON = response.json()
print(responseJSON['text'])

if responseStatus == 200:
    print(response.headers)
else:
    print(responseStatus)