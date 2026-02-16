print("welcome to the inharitance")

class student:
    def __init__(self,name,rollnumber,section,course,):
        self.name=name
        self.rollnumber=rollnumber
        self.section=section
        self.course=course
    def info (self):
     print(f"student name is {self.name} rollnumber is {self.rollnumber} section A{self.section} course is {self.course}")

class collegestudent(student):#attributes inharit
   def __init__(self,name,rollnumber,section,course,branch):
      super().__init__(name,rollnumber,section,course,)
      self.branch=branch
   def info_p (self):# method inharit form parant class
      super().info()  
      print(f"branch is {self.branch}")
        
   
s1=collegestudent("pavan",12,'A',"B.tech","CSE")   
# print(s1.name,s1.rollnumber,s1.section,s1.course)
s1.info_p()
s1.info()