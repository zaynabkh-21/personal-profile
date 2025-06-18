num_of_students=int(input("Hello teacher ! enter the number of your students\n"))
#create an empty list of students names and grades
student_name=[]
student_grade=[]

print("enter the student name and grade")
#create for loop to get the student name and grade
for i in range(num_of_students):
    student_name.append(input().capitalize())
    student_grade.append(float(input()))
    while student_grade[i]>100 or student_grade[i]<0:
            print("invalid grade")
            student_grade.append(float(input()))