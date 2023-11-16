import asyncio
import time

async def test_01():
    print("Something")
    await asyncio.sleep(3)
    print("Anything")


async def test_02():
    print("Hi")
    await asyncio.sleep(1)
    print("Goodbye")


async def main():
    await asyncio.gather(test_01(), test_02(), test_01())


start = time.perf_counter()
asyncio.run(main())
execution_time = time.perf_counter() - start

print(
    f"Execution time: {str(round(execution_time,2))} seconds" 
)

# Import the library.
import time

# Create two functions.
def test_01():
   print("Something")
   time.sleep(3)
   print("Anything")


def test_02():
   print("Hi")
   time.sleep(1)
   print("Goodbye")


# Calculate the total time.
time_start = time.time()
test_01()
test_02()
test_01()
time_end = time.time()

# View the output.
print("Execution Time: " + str(round(time_end - time_start, 2)) + " seconds")


# Import the library.
import asyncio 
import time

# Create five functions.
async def test_03(): 
   print("Something") 
   await asyncio.sleep(1)
   return await test_04()


async def test_04(): 
   print("Hi")
   await asyncio.sleep(1)
   return await test_05()


async def test_05(): 
   print("Walk") 
   await asyncio.sleep(1)
   return await test_end()


async def test_end(): 
   print("Finished!")


async def main(): 
   await asyncio.gather(test_03(), test_05(), test_04(), test_05(), test_end())


# Calculate the total time.
time_start = time.time() 
asyncio.run(main()) 
time_end = time.time() 

# View the output.
print("Execution Time: " + str(round(time_end - time_start, 2)) + " seconds")