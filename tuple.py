print("welcome to the tuple")
students=("pavan","pavinder","kunal","rohit","vijay","ajay","monu")
print("total number or element in tuple = ",len(students))
print(students,type(students))
course=("mathemetics","englishj","hindi","chemistry","python")
temp=list(students) # change the tuple into lists because we are not change or perform operation diractly in tuple
temp.append("shivam")# add item
temp.pop(6)    # delete item
temp[5]= "monu" # change item
students=tuple(temp)
print(students)

rajput=students + course # add two tuple in one tuple
print(rajput)
