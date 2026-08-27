#1) safe integer input
"""try: 
    a=int(input())
    print("u entered",a)

except ValueError:
    print("enter a valid number")

#zerodivison error
try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("enter numbers only")        

#even or odd

try:
    a=int(input("eneter the number"))
    if a%2==0:
        print(f"{a}:even")
    else:
        print(f"{a}:odd")

except ValueError:
    print("enter the valid number") 

finally:
    print("programfinished")  

#positive negative zero
             
try:
    a=int(input("enter the number"))             
    if a>0:
        print(f"{a}: positive")
    elif a<0:
        print(f"{a}: is negative")
    else:
        print(f"{a}: is zero")

except ValueError:
    print("enter the valid number")

finally:
    print("code running successful")     """

       

            