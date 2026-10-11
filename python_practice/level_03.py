"""#Count a specific number
numbers = [10, 20, 10, 30, 10, 40, 20, 10]
count=0
for i in numbers:
    if i==10:
        count=count+1
print(count)

#count 5 and 8
numbers = [5, 8, 5, 3, 8, 5, 2, 8]
count_5=0
count_8=0
for x in numbers:
    if x==5:
        count_5=count_5+1
    elif x==8:
        count_8=count_8+1
print("5 appears",count_5,"times")
print("8 appears",count_8,"times")

# Find First occurrence
# Target number 7
numbers = [10, 30, 20, 30, 40]
for index,value in enumerate(numbers):
    if value==30:
        break
print(index,value)

# Target number 7
numbers = [12, 7, 25, 7, 30, 7, 18]

for index,value in enumerate(numbers):
    if value==7:
        break
print(value,index)

# Number not found
numbers = [12, 7, 25, 30, 18]
found=False
for i in numbers:
    if i==100:
        found=True
        break
if found:
    print("Found")
else:
    print("Not Found")

numbers = [12, 7, 25, 30, 18]
target = 25
found=False

for x in numbers:
    if x==target:
        found=True
        break
if found:
    print("Found")
else:
    print("Not Found")

# Find the index of a target
numbers = [15, 8, 22, 8, 35, 10]
target = 35
found=False
for index,value in enumerate(numbers):
    if value==target:
        found=True
        break
if found:
    print(index)
else:
    print("Not Found")

# Count all accurrences of a target
numbers = [4, 7, 4, 9, 4, 2, 7]
target = 4
count=0
for index,value in enumerate(numbers):
    if value==target:
        count=count+1
print(count)"""

numbers = [4, 7, 4, 9, 4, 2, 7]
target = 4
for index,value in enumerate(numbers):
    if value==target:
        print(index)

numbers = [10, 20, 10, 30, 20, 10, 40]
