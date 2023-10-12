# Create a list
list_colour = ['red', 'green', 'pink', 'yellow', 'white', 'black', 'blue']

print(list_colour)

# Add striped
list_colour.append('striped')

print(list_colour)

# Remove striped
list_colour.remove('striped')

print(list_colour)


##TUPLES##
# # Create a tuple
tuple_colour = ('red', 'green', 'pink', 'yellow', 'white', 'black', 'blue')
print(tuple_colour)

# tuple_colour.add('striped')
# print(tuple_colour)
# As you’ve learnt, a tuple can store multiple items in a single variable: ordered but unchangeable. Tuples are unique as we cannot employ the append() and remove() functions.

## Dictionaries
# Create a dictionary
dictionary_colour = {
    'red': 'apple',
    'green': 'grass',
    'pink':'peach',
    'yellow': 'lemon',
    'black':'pants'
}

print(dictionary_colour)

print(dictionary_colour['pink'])

dictionary_colour['white'] = 'cloud'

print(dictionary_colour)

dictionary_colour.update({'test':'test'})

print(dictionary_colour)

del dictionary_colour['green']
print(dictionary_colour)