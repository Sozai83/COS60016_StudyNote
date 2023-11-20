def test_01(msg):
    print("test01:", msg)

def test_02(msg):
    print("test02:", msg)


msg1= "Something"
msg2= "Anything"

test_01(msg1)
test_02(msg2)

# Create two functions with print() functions.
def test_01(msg):
   print("test01: ", msg)

def test_02(msg):
   print("test02: ", msg)

# Create a variable to store the message.
msg = 'Something'
msg = 'Anything'

# View the output.
test_01(msg)
test_02(msg)

import threading

def test_01(msg):
    print("test01:", msg)

def test_02(msg):
    print("test02:", msg)

msg = "In THREAD something"

t1 = threading.Thread(target=test_01, args=[msg])
msg = "In THREAD anything"
t2 = threading.Thread(target=test_02, args=[msg])


t1.start()
t2.start()

t1.join()
t2.join()


# Import library.
import threading
from time import sleep

# Create two functions with print() as return.
def test_01(msg):
    # Insert a for loop.
    for i in range(50):
        sleep(2)
        print("Function test_01 ################################")

def test_02(msg):
    # Insert a for loop.
    for i in range(50):
        sleep(2)
        print("Function test_02 --------------------------------")   

# Create threads.
msg = "In THREAD something" 
t1 = threading.Thread(target=test_01, args=[msg]) 

msg = "In THREAD anything" 
t2 = threading.Thread(target=test_02, args=[msg])


# Creating threads.
t1.start() 
t2.start()

# Join the threads.
t1.join() 
t2.join()


import threading
import os

def test_01(msg):
    print(msg)
    print("PID: ", os.getpid())

def test_02(msg):
    print(msg)
    print("PID: ", os.getpid())

msg="Print Somthing"
t1 = threading.Thread(target=test_01, args=[msg])

msg="Print Anything"
t2 = threading.Thread(target=test_02, args=[msg])

t1.start()
t1.join()

t2.start()
t2.join()


print("Name:", t1.name)
print("Name:", t2.name)

import threading
import os

def test_01():
    print("PID: ", os.getpid())

def test_02():
    print("PID: ", os.getpid())

msg="Print Somthing"
t1 = threading.Thread(target=test_01, args=[])
t1.start()
t1.join()

msg="Print Anything"
t2 = threading.Thread(target=test_02, args=[])
t2.start()
t2.join()


print("Name:", t1.name)
print("Name:", t2.name)


t2.setName("Our Thread")
print(t2.name)


# Import libraries.
import threading
from random import *

# Create function to read the list.
def read_list(x_list):
    for i in range(len(x_list)):
        print(i)
    print()

# Create a function to insert to a list.
def insert_into_list(x_list):
    for i in range(len(x_list)):
        x_list.insert(randint(0, 100), randint(0, len(x_list) - 1))

# Create a function to delete from a list.
def delete_from_list(x_list):
    for i in range(len(x_list)):
        n = randint(0, 1)
        if n == 1:
            x_list.pop(randint(0, len(x_list) - 1))


# Create a list.
our_list = [1, 2, 5, 7, 1, 9]

# Create threads.
t1 = threading.Thread(target=read_list, args=[our_list])
t2 = threading.Thread(target=insert_into_list, args=[our_list])
t3 = threading.Thread(target=delete_from_list, args=[our_list])

# Start threads.
t1.start()
t2.start()
t3.start()

print(our_list)

# Create a for loop to display output.
for k in range(100):
    threading.Thread(target=read_list, args=[our_list]).start()
    threading.Thread(target=insert_into_list, args=[our_list]).start()
    threading.Thread(target=delete_from_list, args=[our_list]).start()


from threading import *
from time import sleep
import time

class one(Thread):
    def test_01(self):
        for i in range(5):
            print("Function Test_01")
            sleep(10)


class two(Thread):
    def test_02(self):
        for i in range(5):
            print("Function Test_02")
            sleep(10)



t1 = one()
t2 = two()

# Calculate the total time.
time_start = time.time()
print('started timer...')

t1.start()
sleep(1)
t2.start()
sleep(1)

t1.join()
t2.join()

print('Python')

time_end = time.time() 

print(f'{time_end - time_start}')