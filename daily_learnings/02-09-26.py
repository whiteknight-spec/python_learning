"""#read a global variable
name="lana"
def greet():
    print(name)
greet()

#2) local variable
x=9
def number():
    x=0
    print(x)
number()  
print(x)

#3)change global value
x=0
def number():
    global x
    x=2
number()
print(x)   

#4)fix the error

count=0
def increase():
    global count
    count+=1
    #count=count+1
increase()
print(count)    """
    