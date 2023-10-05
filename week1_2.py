#Basic operators
# Create variables.
small = 10
big = 20 

# View the output.
print("small + big = ",small + big)
print("small - big = ",small - big)
print("small * big = ",small * big)
print("small * big = ",small / big)

# Create variables.
admin_password = 1234  
user_input = 1235  

# View the output.
print(admin_password == user_input) 
print(admin_password <= user_input) 
print(admin_password != user_input) 

# If statement
# Create a variable.
password = '1234'

# Specify an if statement.
if password == '1234':
    print('password is correct')

# Specify an else statement.    
else: 
    print('password is incorrect')


# elif statement
# Create a variable.
fruit = 'test'

# Specify the if statement.
if fruit == 'orange':
    print('I do not really like oranges.')

# Specify the elif statement.
elif fruit == 'apple':
    print('apples are my favourite.')

else:
    print('I like any fruits')


# Create variables.
first_name = input("What's your first name? ")
last_name = input("What's your family name? ")

# Specify the if statement.
if first_name == 'Jane' and last_name == 'Doe':
    print('Welcome ' + first_name + ' ' + last_name)

# Specify the else statement.    
else: 
    print('User not recognised')


