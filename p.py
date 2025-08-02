student ={}
for i in range(3):
    print(f" \n enter details for student{i+1}")
    rollno=int(input("enter a rol no"))
    name=input("enter a name")
    student[rollno]=name
    print("\n student dictionary")
    print(student)