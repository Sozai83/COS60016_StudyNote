def my_decorator(func):
    def wrapper_function(*args):
        print(f'{func.__name__} is called with parameter {args}')
        return func(*args)
    return wrapper_function



# Three functions.
@my_decorator
def add(x, y):
    return x + y

@my_decorator
def add2(x, y,z):
    return x + y    

@my_decorator
def subtract(x, y):
    return x - y

@my_decorator    
def multiply(x, y):
    return x * y 

# View the output.
print("Adding two values: ", add(5,3))
print("Subtracting two values: ", subtract(5,3))
print("Multiplying two values: ", multiply(5,3))
