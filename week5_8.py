from random import randint, random
import inspect

def password_generator_01(max_length,allowed_chars,  seed=None):
    if max_length < 10:
        raise Exception("Password cannot be shorter then 10")
    
    if seed:
        random.seed(seed)

    length = randint(int(max_length - (max_length * 0.1)), max_length)

    psswd = ''

    for i in range(length):
        psswd += allowed_chars[randint(0, len(allowed_chars)-1)]

    return psswd

max_characters = 15

character_selection = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+{}|>?<[];',./~`><"


password = password_generator_01(max_characters, character_selection)

print(password)


def password_generator_01(max_length: int,allowed_chars:str,  seed=None):
    if max_length < 10:
        raise Exception("Password cannot be shorter then 10")
    
    if seed:
        random.seed(seed)

    length = int(randint(int(max_length - (max_length * 0.1)), max_length))
    passwd = ''

    for i in range(length):
        passwd += allowed_chars[randint(0, len(allowed_chars) - 1)]
    
    return passwd


# Specify max and type of characters.
max_characters = 15
character_selection = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+{}|>?<[];'\,./~`><"

# Pass the function.
password = password_generator_01(max_characters, character_selection)

# View the output.
print("Password: ", password)
print(password_generator_01.__annotations__)
print(inspect.getfullargspec(password_generator_01))