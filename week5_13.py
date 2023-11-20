# import multiprocessing
# import os


# def test_01():
#     print(test_01.__name__, os.getpid(), end="")


# def test_02():
#     print(test_02.__name__, os.getpid(), end="")


# def test_03():
#     print(test_03.__name__, os.getpid(), end="")



# if __name__ == '__main__':
#     processes = [
#         multiprocessing.Process(target=test_01, args=[]),
#         multiprocessing.Process(target=test_02, args=[]),
#         multiprocessing.Process(target=test_03, args=[])
#     ]

#     for p in processes:
#         p.start()
#         p.join()
#         print(p.name)


# # Create a function to append the list.
# def change_list(x_list):
#     x_list.append(10)

# # Insert the wrapping structure. 
# if __name__ == '__main__': 
#     our_list = [1, 2, 3, 4, 5]
#     change_list(our_list)
#     # View the output.
#     print(our_list)


# # Import the library.
# import multiprocessing
 
# # Create a function to append the list. 
# def change_list(x_list):
#    return x_list.append(10)
 
# # Create a new list. 
# our_list = [1, 2, 3, 4, 5]

# # View the output before processing.
# print("The list before processing:", our_list)

# # Employ the multiprocessing method.
# p1 = multiprocessing.Process(target=change_list, args=[our_list])

# # Start the multiprocess.
# p1.start()

# # View the output after processing.
# print("The list after processing:", our_list)


# # Import the library.
# import multiprocessing
 
# # Create a function to append lists. 
# def change_list(x_list):
#    x_list.append(10)
#    print(x_list, "inside the process")
#    return x_list
 
# # Insert wrapping structure.
# if __name__ == '__main__':
#     our_list = [1, 2, 3, 4, 5]
#     print("The list before processing:", our_list)

#     # Employ the multiprocessing method.
#     p1 = multiprocessing.Process(target=change_list, args=[our_list])


#     # Start the multiprocess.
#     p1.start()
#     p1.join()

#     # View the output.   
#     print(our_list, "outside the process")


# Import the modules.
from multiprocessing import Process, Manager

# Create a function to append a list.
def change_a_list(x_list):
    x_list.append(100)
    print("inside the process:", x_list)
    return x_list

# Create a new list.
num_list = [1, 2, 3, 6]
print("Before the process:", num_list)

if __name__ == '__main__':
    with Manager() as manager:
        pass_list = manager.list(num_list)
        our_process = Process(target=change_a_list, args=[pass_list])
        our_process.start()
        our_process.join()
        num_list = list(pass_list)

    print("Outside the process:", list(num_list))