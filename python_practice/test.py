"""#find largest and smallest number

numbers=[1,12,22,34,32,54,2]
print(min(numbers))

#find largest and smallest number without using max,min

numbers=[1,12,22,34,32,54,2]
largest=numbers[0]

for i in numbers:
    if i > largest:
        largest=i
print(largest)

smallest=numbers[0]

for x in numbers:
    if x < smallest:
        smallest=x
print(smallest)

#add numbers useing sum
numbers = [10, 20, 5, 30, 15]
print(sum(numbers))

#add numbers without sum
total=0
for x in numbers:
    total=total+x

print(total)

#add only even numbers
numbers = [10, 15, 20, 25, 30]
total=0
for i in numbers:
    if i % 2 == 0:
        total=i+total

print(total)

#add only odd numbers
numbers = [12, 7, 25, 4, 18, 9]
total=0
for x in numbers:
    if x % 2 != 0:
        total=total + x
print(total)

#count even_numbers
numbers = [10, 15, 20, 25, 30, 35]
count=0
for i in numbers:
    if i % 2 == 0:
        count=count+1
print(count)

#find a value 

numbers = [10, 25, 7, 40, 15]
if 40 in numbers:
    print("Found")

for x in numbers:
    if x==40:
        print("Found")

numbers = [10, 25, 7, 40, 15]
Found=False
for i in numbers:
    if i==25:
        found=True
if found:
    print("Found")
else:
    print("Not Found")

numbers = [10, 20, 30, 20, 40, 20]
count=0
for i in numbers:
    if i==20:
        count=count+1
print(count)

#find the largest even numbers

numbers = [10, 5, 20, 15, 30, 25]
largest=0
for x in numbers:
    if x % 2 == 0:
        if x>largest:
            largest=x
print(largest)

numbers = [10, -5, 20, -8, 15, -3]
count=0
for x in numbers:
    if x>0:
        count=count+1
print(count)

total=0
for i in numbers:
    if i<0:
        total=total+i
print(total)

numbers = [4, 7, 2, 9, 6, 3]
total=0
for i in numbers:
    if i % 2 == 0:
        total=total+i
print(total)

numbers = [10, 25, 7, 40, 15, 30]
count=0
for x in numbers:
    if x>10:
        count=count+1
print(count)

numbers = [5, 12, 8, 20, 3, 15]
total=0
for i in numbers:
    if i>10:
        total=total+i

print(total)

numbers = [4, 8, 15, 23, 42]
largest=0
for i in numbers:
    if i>largest:
        largest=i
print(largest)"""

numbers = [10, 25, 7, 40, 15, 30, 18]
count=0
for x in numbers:
    if x>20:
        count=count+1
print(count)

total=0
for i in numbers:
    if i>20:
        total=total+i
print(total)

numbers = [18, 7, 25, 3, 14, 9]
smallest=numbers[0]
for x in numbers:
    if x < smallest:
        smallest=x
print(smallest)

numbers = [5, 12, 8, 21, 14, 7, 30]
largest=0
for i in numbers:
    if i%2==0:
        if i>largest:
            largest=i
print(largest)