print("Welcome to the Execption Handling")
try:
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    result= a / b
    print("result is ")
except ZeroDivisionError:
    print("you cannot divide by 0")

except ValueError:
    print("please enter number only")    
else:
    print("divide successfully")

finally:
    print("program ended")    