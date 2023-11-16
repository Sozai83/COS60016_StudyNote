import requests
import os
from pprint import pprint

url = 'https://api.openweathermap.org/data/2.5/weather'
API_key = os.environ.get('OpenWeather_API_key')

resp = requests.get(url)
print(resp.status_code)
print(resp.encoding)

class GetRequests():
    def __init__(self,url):
        self.url = url

    def make_get_requests(self):
        resp = requests.get(url=self.url)
        if(resp.status_code) == 200:
            print('Headers are returend')
            return resp.headers
        else:
            print(resp.status_code)
            return resp.status_code

urls = {'openweather': 'https://openweathermap.org/'}

my_get = GetRequests(urls['openweather'])

my_get.make_get_requests()

weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=51.5009088&lon=-0.176087569708498" "&appid=" + API_key
resp1 = requests.get(weather_url)
print("Today's weather in London:")
pprint(resp1.json())
