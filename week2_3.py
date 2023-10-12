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


## Nested Loops

adj = ['red', 'big', 'tasty', 'sweet', 'juicy', 'sour']
fruits = ['apple', 'banana', 'cherry', 'pineapple', 'gherkin']

# for x in adj:
#     for y in fruits:
#         print(x,y)

i = 0
for x in adj:
    i = 0
    while i < 3:
        print(x, fruits[i])
        i += 1
i=0

while i < 3:
    i2 = 0
    i += 1
    print(f'Count Outer: {i}')
    while i2 < 3:
        i2 += 1
        print(f'Count inside: {i2}')



## Loop control statements

# Create a list.
todo_list = ["take out trash", "play video games", "cook dinner", "learn programming"]

#
for task in todo_list:
    if(task == 'cook dinner'):
        print(f'stopping because of {task}')
        break
    print(task)

# continue
for task in todo_list:
    if(task == 'cook dinner'):
        continue
    print(task)


#The pass statement in Python is used when a statement is required but you do not want to run any command or code. It is often used as a placeholder for future implementation of loops or functions. 
for task in todo_list:
    pass


# Create a variable.
big_counter = 0

# Insert while loop.
while big_counter < 10:
    big_counter += 1
    if big_counter == 5:
        continue
    print("Loop #", big_counter)
    counter = 0
    while counter < 10:
        counter += 1
        if counter == 6:
            break
        print(counter)