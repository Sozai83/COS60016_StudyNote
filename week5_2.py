# Function as objects
# Create a function.
def scream(text):
    # Insert a return statement.
    return text.upper()

# View the output.
print(scream('Hello!'))

# Set yell equal to scream.
yell = scream

# View the output.
print(yell('Hello!'))

# Functions passing as argument

def scream(text):
    return text.upper()

def mutter(text):
    return text.lower()

def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)

greet(scream)
# HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
greet(mutter)
# hi, i am created by a function passed as an argument.


# Running functions from another function

def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15)
print(add_15(5))
# 20 = 15 + 5
print(add_15(1))
# 16 = 15 + 1



# Function as argument with decorator

def check_upper_case_decorator(func):
    def wrapper_func(*args):
        for str in args:
            if not str.isupper():
                return False
        return func(str)
    return wrapper_func

# Insert decorator.
@check_upper_case_decorator
def reverse_string_01(my_string):
   return "".join(reversed(my_string))

msg_01 = "aa01567ffba3097cc"
print(reverse_string_01(msg_01))
# False

msg_02 = "AA001344CCDFBBFFF"
print(reverse_string_01(msg_02))
# FFFBBFDCC443100AA


# Create a function.
def reverse_string_01(my_string):
   return "".join(reversed(my_string))
msg_01 = "aa01567ffba3097cc"
msg_02 = "AA001344CCDFBBFFF"

def reverse_string_02(my_string):
   for c in my_string:
       if not c.isupper() and not c.isdigit():
           return False
       return "".join(reversed(my_string))

# View the output.
print(reverse_string_01(msg_01))
# cc7903abff76510aa
print(reverse_string_01(msg_02))
# FFFBBFDCC443100AA