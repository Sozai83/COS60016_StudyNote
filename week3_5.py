import requests, json

url = 'https://swapi.dev/api/people/1/'
response = requests.get(url)

print(response.status_code)
# 200
print(response.json())
# {'name': 'Luke Skywalker', 'height': '172', 'mass': '77', 'hair_color': 'blond', 'skin_color': 'fair', 'eye_color': 'blue', 'birth_year': '19BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/1/', 'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'], 'species': [], 'vehicles': ['https://swapi.dev/api/vehicles/14/', 'https://swapi.dev/api/vehicles/30/'], 'starships': ['https://swapi.dev/api/starships/12/', 'https://swapi.dev/api/starships/22/'], 'created': '2014-12-09T13:50:51.644000Z', 'edited': '2014-12-20T21:17:56.891000Z', 'url': 'https://swapi.dev/api/people/1/'}


def jprint(obj):
    text=json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

info = requests.head(url)
print(info.headers)
# {'Server': 'nginx/1.16.1', 'Date': 'Mon, 23 Oct 2023 12:45:20 GMT', 'Content-Type': 'application/json', 'Connection': 'keep-alive', 'Vary': 'Accept, Cookie', 'X-Frame-Options': 'SAMEORIGIN', 'ETag': '"ee398610435c328f4d0a4e1b0d2f7bbc"', 'Allow': 'GET, HEAD, OPTIONS', 'Strict-Transport-Security': 'max-age=15768000'}
print(info)
# <Response [200]>
# print(info.json())
#  raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)

head_response = requests.head('https://jsonplaceholder.typicode.com/posts/1')
print("Head: ", head_response.headers)

url = 'https://jsonplaceholder.typicode.com/posts/1'
myobj = {
    'title': 'Inserted through requests library',
    'body' : 'This post was inserted through the requests library in python. This  was performed using a PUT request',
    'userId': 1,
    'id': 1
}

put_response = requests.put(url, data=myobj)
print("Put: ", put_response.text)
# Put:  {
#   "title": "Inserted through requests library",
#   "body": "This post was inserted through the requests library in python. This  was performed using a PUT request",
#   "userId": "1",
#   "id": 1
# }

delete_response = requests.delete(url)
print("Delete: ", delete_response.text)
# Delete:  {}

myobj_patch = {'title': 'None'}
               
patch_response = requests.patch(url, data=myobj_patch)

print("Patch: ", patch_response.text)
# Patch:  {
#   "userId": 1,
#   "id": 1,
#   "title": "None",
#   "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }