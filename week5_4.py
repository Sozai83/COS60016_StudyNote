def validation_decorator(func):
    def validation_decorator_wrapper(*args):
        temp_args =[]
        for num in args:
            if not num.isdigit():
                raise Exception("Both numebrs have to be either integers")
            else:
                temp_args.append(int(num))
        return func(*temp_args)
    return validation_decorator_wrapper


# # Create a function for the decorator.
# def validation_decorator(func):
#     # Insert a wrapper to contain the decorator function.
#     def validation_wrapper(*args):
#         # Insert an if statement.
#         if not args[0].isdigit() or not args[1].isdigit():
#            raise Exception("Both numbers have to be either integers")
#         # Insert an else statement.   
#         else:
#            num_01 = int(args[0])
#            num_02 = int(args[1])
#         # Insert an if statement.
#         if isinstance(num_01, int) and isinstance(num_02, int):
#            return func(num_01, num_02)
#         # Insert an else statement.
#         else:
#            raise Exception("Both numbers have to be integers")
#     # Insert return statement for wrapper_function.
#     return validation_wrapper


    

# Define the functions and add decorators.
# One function for each possible calculation (e.g. +, -, *, /).
@validation_decorator
def add(num_01, num_02):
    # Insert return statement.
    return num_01 + num_02

@validation_decorator
def subtract(num_01, num_02):
    # Insert return statement.
    return num_01 - num_02

@validation_decorator
def multiply(num_01, num_02):
    # Insert return statement.
    return num_01 * num_02

@validation_decorator
def divide(num_01, num_02):
    # Insert if and else statements.
   if num_02 != 0:
       return num_01 / num_02
   else:
       return "Cannot divide by zero!"
   

@validation_decorator
def exponentiation(num_01, num_02):
    return num_01 ** num_02
   

while True:
    fisrt_num = input('Enter first numebr or q to quit:')
    if fisrt_num == 'q':
        break
    second_num = input('Enter first numebr or q to quit:')
    if second_num == 'q':
        break
    operation = input('''Enter 1 for addition
    Enter 2 for subtraction
    Enter 3 for multiplication
    Enter 4 for division
    Enter 5 forexponentiation
    Enter q to quit:''')
    if operation == 'q':
        break
    if operation not in ['1','2','3','4','5']:
        raise Exception("Invalid operation. Try again!")
    if operation == '1':
        print(add(fisrt_num, second_num))
        break
    if operation == '2':
        print(subtract(fisrt_num, second_num))
        break
    if operation == '3':
        print(multiply(fisrt_num, second_num))
        break
    if operation == '4':
        print(divide(fisrt_num, second_num))
        break
    if operation == '5':
        print(exponentiation(fisrt_num, second_num))
        break