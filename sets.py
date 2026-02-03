print("welcome to the sets ")
s1={5,2,8,6,1,6,5,4,9,20,12,37,45,15,69,66}
s2={1,5,2,3,6,8,9,4,7,22,55,99,44,33,30,12,24}
print(s1,s2)
#I find the union between two sets.
s3=s1.union(s2)
print("union of two sets",s3)
#I find the intersection between two sets.
s4=s1.intersection(s2)
print("intersection of two sets",s4)
#I find the superset  between two sets.
s5=s1.issuperset(s2)
print("superset of two sets",s5)
#I find the symmetric_diffrence  between two sets.
s6=s1.symmetric_difference(s2)
print("symmetric_diffrence of two sets",s6)

# some method of sets.
s1.add(100)
print(s1)
s2.remove(4)
print(s2)
s2.pop()
print(s2)