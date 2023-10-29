import requests
import os
import pprint

api_key = os.environ.get('GoogleMapAPIKey')

address = 'Lake District National Park'.replace(' ', '+')

url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + api_key

resp = requests.get(url)
print(resp.status_code)

status = resp.json()['status']

if resp.status_code == 200 and status != 'ZERO_RESULTS':
    print(resp.json()['results'][0]['geometry']['location'])

else:
    print(resp.status_code)