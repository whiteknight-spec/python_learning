#simple calculator with error handling
try:
    a = float(input("enter the first value ="))

    operation=input("enter the operation (+,-,/,*):")

    b = float(input("enter the second value ="))

    if operation=="+":
        print("added value:",a+b)
    elif operation=="-":
        print("subtraction value =",a-b)
    elif operation=="*":        
        print("multiplication value=",a*b)
    elif operation=="/" :
        print("divison value=",a/b)
    else:
        raise ValueError ("invalid operator")    

except ValueError:
    print("invalid operation")

except ZeroDivisionError:
    print("can't divided by zero")

except Exception:
    print("something went wrong")

finally:
    print("code running")


