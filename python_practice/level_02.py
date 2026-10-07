"""# 1) count postive even numbers
numbers = [4, -2, 7, 10, -8, 15, 6, -3]
count=0
for x in numbers:
    if x>0:
        if x%2==0:
            count=count+1
print(count)

# 2) sum postive odd numbers
numbers = [-5, 3, 8, 11, -7, 4, 9, -2]
total=0
for i in numbers:
    if i>0 and i%2!=0:
        total=total+i
print(total)

# 3) count numbers between 10 and 30
numbers = [5, 12, 18, 31, 25, 7, 30, 15, 40]
count=0
for numbe in numbers:
    if numbe>10 and numbe<30:
        count=count+1
print(count)

#4) sum numbers between 10 and 30
numbers = [5, 12, 18, 31, 25, 7, 30, 15, 40]
total=0
for i in numbers:
    if i>10 and i<30:
        total=total+i
print(total)

# 5)largest postive odd number
numbers = [-3, 7, 12, 15, -9, 21, 8, 11]
largest=0
for x in numbers:
    if x>0 and x%2!=0:
        if x > largest:
            largest=x
print(largest)"""

# 6) smallest postive even number 
numbers = [-10, 8, 3, 14, -2, 6, 21, 4]
smallest=None
for i in numbers:
    if i>0 and i%2==0:
        if smallest is None:
            smallest=i
        elif i < smallest:
            smallest=i
print(smallest)

# 7) count postive numbers greter than 10 and even
numbers = [-5, 12, 8, 25, 16, -2, 30, 7, 14]
count=0
for x in numbers:
    if x>0 and x%2==0 and x>10:
        count=count+1
print(count)

# 8) find largest negative number
numbers = [-20, -5, -12, 8, -3, -15, 4]
largest=None
for i in numbers:
    if i<0:
        if largest is None:
            largest=i
        elif i>largest:
            largest=i
print(largest)

# 9)sum negative even numbers
numbers = [-10, 5, -8, 12, -3, -6, 7, -14]
total=0
for x in numbers:
    if x<0 and x%2==0:
        total=total+x
print(total)

# 10)find the smallest postive even number
numbers = [12, -5, 8, -20, 15, 7, -3, 30, 18]
smallest=None
for i in numbers:
    if i>0 and i%2==0:
        if smallest is None:
            smallest=i
        elif i<smallest:
            smallest=i
print(smallest)