#Functions

def say_hi(name):
    print(f'Hello and welcome to my program, {name}!')

say_hi('Shiori')

def say_hi(name):
    return f'Hello and welcome to my program, {name}!'

greeting = say_hi('Shiori')
print(greeting)

# Positional and keyword arguments
def add_optional_bonus(a,b, c=0, d=0):
    return (a + b + c + d)

print(add_optional_bonus(5,6))
print(add_optional_bonus(5,6, c=10))
print(add_optional_bonus(5,6,10))
print(add_optional_bonus(5,6, d=20))

def next_three_values(x):
    a = x + 1
    b = x + 2
    c = x + 3

    return a, b, c

print(next_three_values(5))
x,y,z = next_three_values(5)
print(x,y,z)

#Lambda (Anonymous) functions
def number_squared(x):
    return x**2

print(number_squared(3))

print(lambda x: x**2)

equiv_func = lambda x: x**2
print(equiv_func)

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)


print(factorial(3))

#Builtin functions

# str() - changes the argument type to string
a = 4
print(type(str(a)))

# enumerate() - convert a list into a dictionary
x = ('red', 'bule', 'yellow')
y = enumerate(x)

print(x)
print(y)
print(list(y))

# zip() - pairs up elements of a number of lists, tuples or other sequences to creat a list of tuples

a = ('Shiori', 'Karl','Best','Happy')
b = ('Chiku', 'van Zoggel', 'Family')
c = ('Test','Test2')
x = zip(a,b, c)

print(x)
print(tuple(x))

# sorted() - returns a new sorted list from the elements of any sequence
# List
list_of_items = ['P', 'y', 't', 'h', 'o', 'n']
print(sorted(list_of_items))
print(list_of_items)
 
# Tuple
tuple_of_items = ('P', 'y', 't', 'h', 'o', 'n')
print(sorted(tuple_of_items))
 
# Dictionary
dictionary = {'P': 1, 'y': 2, 't': 3, 'h': 4, 'o':5, 'n':6}
print(sorted(dictionary))
 
# Set
set_of_values = {'P', 'y', 't', 'h', 'o', 'n'}
print(sorted(set_of_values))


# reversed()-  iterates over the elements in the reverse order. 
# Create a variable.
fruits = ['apple', 'banana', 'cherry', 'red', 'blue', 'white']
print(fruits)

# Specify the reverse() function.
fruits.reverse()

# View the output.
print(fruits)
