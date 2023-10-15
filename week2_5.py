# Read CSV file

file = open('climate.csv', 'r')

climate = file.readlines()

print(climate)
print(type(climate))

# Create a list

newList = []

for line in climate:
    newList.append(line[:-1])

print(newList)

newList2 = []

for line in climate:
    newList2.append(line.strip())

print(newList2)

print(newList == newList2)