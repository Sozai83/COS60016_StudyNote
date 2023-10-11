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