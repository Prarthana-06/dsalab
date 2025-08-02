students={}
for i in range(3):
    name=input("enter a name {i+1}")
    marks=int(input("enter a marks for student{i+1}"))
    students[name]=marks
topper=max(students,key=students.get)
print("Topper is",topper,"with marks",students[topper])    