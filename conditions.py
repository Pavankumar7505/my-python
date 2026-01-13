print("welcome to the age checker")
r=input("enter your age")
age =0
age=int(r)

if (age >18):
    print("you are eligable for voting")
    print("you are adult")    
elif(age<14):
    print("you are not eligable for voting")
    print("you are teenager")
else:
    print("you are children")
    