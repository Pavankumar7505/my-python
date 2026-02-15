print("welcome to the OOPS")
# class student:# class
#     name = "pavan kumar"
#     rollnumber=12
#     secation="A"

# a=student # object
# print(a.name,a.rollnumber,a.secation)
    

#class and object with constracter
class student:
    def __init__(self,name,course,rollnumber):#method
        self.name=name#attributes
        self.course=course#attributes
        self.rollnumber=rollnumber#attributes
        
    # def info (self): # method
        # print(f"{self.name} course in {self.course} and rollnumber is {self.rollnumber} ")    

#object instance
a=student("pavan kumar","b.tech",72)
b=student("mukul sharma","b.tech",64)

print(a.name,"course in ",a.course,"and rollnumber is",a.rollnumber)
# a.info()
# b.info()

