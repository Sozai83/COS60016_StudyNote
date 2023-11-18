import multiprocessing
from multiprocessing import Process, Manager
import os

# def test_01():
#     print("Function:", test_01.__name__, "PID:", os.getpid(), end=' ')

# def test_02():
#     print("Function:", test_02.__name__, "PID:", os.getpid(), end=' ')

# def test_03():
#     print("Function:", test_03.__name__, "PID:", os.getpid(), end=' ')


# if __name__ == '__main__':
#     processes = [
#         multiprocessing.Process(target=test_01, args=[]),
#         multiprocessing.Process(target=test_02, args=[]),
#         multiprocessing.Process(target=test_03, args=[]),
#     ]

#     for p in processes:
#         p.start()
#         p.join()
#         print(p.name)

def change_a_list(x_list):
    x_list.append(100)
    print("Inside the process:", x_list)
    return x_list


num_list = [1,2,3,6]
print("Before the process:", num_list)

if __name__ == '__main__':
    with Manager() as manager:
        pass_list = manager.list(num_list)
        our_process = Process(target=change_a_list, args=[pass_list])
        our_process.start()
        our_process.join()
        num_list = list(pass_list)
    
    print("Outside the process:", list(num_list))