import requests
import urllib.request as urlb
from pprint import pprint


response_url = urlb.urlopen('https://api.publicapis.org/entries')

# print(response.response_url)
# NameError: name 'response' is not defined

print(response_url)
# <http.client.HTTPResponse object at 0x000002751D8B7070>

print(response_url.info())
# Access-Control-Allow-Origin: *
# Content-Type: application/json
# Date: Mon, 23 Oct 2023 10:20:12 GMT
# Server: Caddy
# X-Rate-Limit-Duration: 1
# X-Rate-Limit-Limit: 10.00
# X-Rate-Limit-Request-Forwarded-For: 180.150.38.46
# X-Rate-Limit-Request-Remote-Addr: 172.17.0.1:57590
# Connection: close
# Transfer-Encoding: chunked


pprint(response_url.read())