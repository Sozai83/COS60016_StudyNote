
# Create a list.
input_string = "Iterate this"

# View the output.
output_list = list(input_string)
print(output_list)

# For loop
my_list = ["First item", "Second item","Third item"]
for current_item in my_list:
    print(current_item)


# While loop
our_list = ["First item", "Second item","Third item"]
list_length = len(our_list)
current_item = 0

while current_item < list_length:
    print(our_list[current_item])
    current_item += 1


# The iter() and next() methods
string = ["I love Python!", "Python is fun?"]
int = [1, 2, 3, 4, 5]

a = iter(string)
b= iter(int)

print(next(a))
print(next(b))
print(next(a))
print(next(b))


# A while loop and next() metho

string = ["I love Python!", "Python is fun?"]
iter_object = iter(string)

while True:
    try:
        item = next(iter_object)
        print(item)
    except StopIteration:
        print()
        break



# The __iter__ and __next__ methods

class Numbers:
    def __iter__(self):
        self.i = 2
        return self

    def __next__(self):
        x = self.i
        self.i +=2
        return x
    
myclass = Numbers()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
    