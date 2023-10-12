# Print each item in the list.
cities = ['London', 'Paris', 'New York City', 'Singapore', 'Melbourne', 'Cape Town']

# 'item' in this line is an object in the list.
for city in cities:
    print(city)


a = 'Top Cities'
for word in a:
    print(word)


tup_a = ('London', 'Paris', 'New York City', 'Singapore', 'Melbourne', 'Cape Town')
for t in tup_a:
    print(t)


a_dict = {'city': 'London', 'age': 2000, 'population': 8.9}
for d in a_dict:
    print(d)
    # city, age, population

## WHILE loop
i = 1

while i < 20:
    i += 1
    print(i)

count = 1

while count < 5:
    count+= 1
    print((f"Count : {count}"))
    print('Python is fun')


i = 0
a = 'dragonballz'

while i < len(a):
    char = a[i]
    if char == 'a' or char == 'z':
        i += 1
        continue
        
    print(a[i])
    i += 1