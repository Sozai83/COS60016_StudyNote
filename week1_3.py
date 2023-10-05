#Functions

def say_hi(name):
    print(f'Hello and welcome to my program, {name}!')

say_hi('Shiori')

def say_hi(name):
    return f'Hello and welcome to my program, {name}!'

greeting = say_hi('Shiori')
print(greeting)
