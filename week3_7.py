import requests, json

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)

status = response.status_code

if status == 200:
    print('Header information:')
    print("Date: ", response.headers.get('Date'))
    print("Content type: ", response.headers.get('Content-Type'))
    print("access-control-allow-origin: ", response.headers.get('access-control-allow-origin'))
    print("Content-Encoding: ", response.headers.get('Content-Encoding'))
    print('Response:')

    print(response.json())

    responseJSON = json.loads(response.text)
    print(responseJSON)
    print(responseJSON['people'])

    responseJSONDumps = json.dumps(responseJSON, indent=6, separators=('. ', '= '))
    print(responseJSONDumps)



else:
    print(status)
