class Person:
    #An instance attribute is a Python variable belonging to only one object. 
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
    
    def introduce(self):
        print(f'My name is {self.name} and I am {self.age} years old. I speak {self.language}')


person_object = Person('Shiori', 32, 'Japanese')
person_object.introduce()

person_object2 = Person('Jane', 42, 'German')
person_object2.introduce()

### Classes Objects and instances

# Code for demonstration.
# A class attribute is something fixed and unique to each class. 
class Person2:
    
    # Specify parameters.
    name = 'Karl'
    age = 22

