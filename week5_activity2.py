# Import libraries
import time
import multiprocessing
import sys
import os

# Create a variable to store the time.time() method.
start_time = time.time()

# Create a function to determine the prime number(s).
def prime_test(num, start_index, end_index):
    for i in range(start_index, end_index):
        if num % i == 0:
            print("This is not a prime number")
            return False
    return True

# Determine number of available threads.
def get_the_number_of_available_threads():
    if sys.platform == 'win32':
        return int((os.environ['NUMBER_OF_PROCESSORS']))
    else:
        return int((os.popen('grep -c cores /proc/cpuinfo').read()))

# Schedule the processes according to available threads.
def split_tasks(num):
    threads = get_the_number_of_available_threads()
    remainder = int(num % threads)
    task_chunks = int(num // threads)
    processes = []
    for i in range(threads):
        if i != 0:
            t = multiprocessing.Process(target=prime_test,
                                        args=(num, (task_chunks * i), (task_chunks * (i + i))))
            processes.append(t)
            t.start()
        elif i == threads - 1:
            t = multiprocessing.Process(target=prime_test,
                                        args=(num, (task_chunks * i), (task_chunks * (i + i + remainder))))
            processes.append(t)
            t.start()
        else:
            t = multiprocessing.Process(target=prime_test, args=(num, 2, task_chunks))
            processes.append(t)
            t.start()

    for th in processes:
        th.join()
        
        
if __name__ == '__main__':
    num = 2**31-1
    split_tasks(num)


# View the output.
print("All Threads Have finished!")
print("It took: ", time.time()-start_time, "seconds to run the script")
