print("welcome to the student marks grade")
num= input("enter the marks")
num=int(num)
if(num>=80):
    if(num>=75):
        print("Grade A+")
        print("Win 100 ruppes")
    else:
        print("Grade A")
        print("Win 70 ruppes")
elif(num<70):
    if(num<65):
        print("Grade B+")
        print("Win 50 ruppes")
    else:
        print("Grade B")
        print("Win 45 ruppes")
else:
    print("grade F")
    print("Win 0 ruppes")