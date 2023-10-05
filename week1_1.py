#Variables

# Create the age variable and set it to equal to 52
age = 52

# Use the print() function to return the age variable
print(age)

name = 'Susan'

print(f'{name} is {age} yo.')

# Specify the variables

name = 'Shiori'
surname = 'Coding'
age = '32'

# print variables
print (name, surname, age)


# Input and print a variable

name = input("What's your name? ")

# Print the output
print(name)

#Specify a second variable
surname = input("What's your surname? ")

# print the output
print(surname)

# print both outputs
print(f'Hi {name} {surname}, Nice to meet you.')

## View the list of keywords
import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# Following returns error because those are reserved words (keywords)
# ## Create Variables
# import = 15
# except = 'test'
# if = True
# #view output
# print(import)
# print(except)
# print(if)

# Create variables
import_ = 15
except_ = 'test'
if_ = True

#View the output
print(import_)
print(except_)
print(if_)

# Text and numeric data types

# String
sentence1 = "This is a string in double quotes."
print(sentence1)

# Print multiple strings
sentence2 = """This is a multline string.
    Line 1 added
    Line 2 added
    Line 3 added
"""

print(sentence2)

# Specify characters of a string
sentence3 =  "This is a longer string."
print(sentence3)
print(sentence3[1], sentence3[2],sentence3[10])