print("welcome to the dictonary")
student={"name":"pavan","age":22,"course":"b.tech","section":"A","branch":"cse"}
print(student,type(student))
print(student.keys())
print(student.values())

#  dictonary method 
student.update({"age":25})
student.update({"DOB":2005})
del student["name"]
print(student)
student.clear()
print(student)
# student.pop("name")
# print(student)
