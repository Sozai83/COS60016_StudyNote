class Person:
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
