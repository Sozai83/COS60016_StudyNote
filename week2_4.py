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

### Class Attributes
# A class attribute is something fixed and unique to each class. 
class Person2:
    
    # Specify parameters.
    name = 'Karl'
    age = 22

### Instance Attributes

# Returns true (has) if 'age' exists (attr).
hasattr(person_object, 'age') 

# Returns (get) value of 'age' attribute (attr).
getattr(person_object, 'age') 

# Sets (set) attribute (attr) 'age' to 19, for example.
setattr(person_object,'age',19) 

# Deletes (del) the attribute (attr) 'age'.
delattr (person_object, 'age')


x = hasattr(Person2, 'age')
print(x) #True

x = hasattr(Person2, 'lang')
print(x) #False

x = getattr(Person2, 'age')
print(x) #22

# x = getattr(Person2, 'lang')
# print(x) #AttributeError: type object 'Person2' has no attribute 'lang'

setattr(Person2, 'age', 100)
x = getattr(Person2, 'age')
print(x) #100

delattr(Person2, 'age')
x = hasattr(Person2, 'age')
print(x) #False

setattr(person_object2, 'self.age', 100)
x = getattr(person_object2, 'self.age')
print(x) #100