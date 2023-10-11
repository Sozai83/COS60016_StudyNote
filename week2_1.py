##LISTS##

# Create a variable to store the list.
# Specify a list with [].
myList = ['apple', 'banana', 'pear', 'apple']

# View the output.
print(myList)
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[-1])
print(myList[-2])

# View specific characters/indices.
print(myList[0:2])
# Check length of list
print(len(myList))

# Edit a list
# Add 'strawberry'
myList.append('strawberry')
# Remove 'apple'
myList.remove('apple')

print(myList)
# ['banana', 'pear', 'apple', 'strawberry']

# merge two lists
# Create variables to store the lists.
# Specify a list with [].
myList1 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

myList2 = ['brocolli', 'apricot', 'peach', 'Google', 'Cheesecake']

# Combine the two lists.
myList3 = myList1 + myList2


# View the output.
print(myList3)


##TUPLES##
myTuple = ('apple', 'banana', 'pear')

print(myTuple)
print(myTuple[0])
print(myTuple[1])
print(myTuple[2])
print(myTuple[0:2])
# Check length of tuple
print(len(myTuple))

# myTuple[0] = 'watermelon'
# The above returns the error
print(myTuple)


##DICTIONARIES##
# Specify a dictionary as key:value with {}.
student_info = {'name': 'John',
                'last name': 'Doe',
                'birthday': '1997',
                'major': 'Computer Science'}

# View the output.
print(student_info)

print(student_info['name'])
print(student_info['birthday'])
print(student_info['major'])

# Determine length of a dictionary
print(len(student_info))

student_info['name'] = 'Mark'
print(student_info)
#{'name': 'Mark', 'last name': 'Doe', 'birthday': '1997', 'major': 'Computer Science'}

student_info2 = {'name': 'John',
                'name': 'Mark',
                'last name': 'Doe',
                'birthday': '1997',
                'major': 'Computer Science'}

print(student_info2)
# {'name': 'Mark', 'last name': 'Doe', 'birthday': '1997', 'major': 'Computer Science'}
# Importantly, you cannot have duplicate keys in a dictionary. The second instance of a key will simply replace the first and overwrite the original value with the new value, as in the previous example.
