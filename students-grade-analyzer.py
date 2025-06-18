#create integer input field 
num_of_students=int(input("Hello teacher ! enter the number of your students\n"))

#create list to store student names and grades
student_name=[]
student_grade=[]

#loop to get student names and grades
print("enter the student name and grade")
for i in range(num_of_students):
    student_name.append(input().capitalize())
    student_grade.append(float(input()))
    #verification to ensure grade is between 0 and 100
    while student_grade[i]>100 or student_grade[i]<0:
            print("invalid grade")
            student_grade.append(float(input()))

#function to display students summary list
def display_students_summary(number_of_students,name,grade):
    print("Names: \t\t\t\t Grades:")
    for i in range(number_of_students):
        print(name[i], "\t", grade[i])

#function to get avarage grade of the class 
def get_avg_grade(number_of_students,grade):
    avg_grade=0
    sum_of_grade=0
    for i in range (number_of_students):
        sum_of_grade=sum_of_grade+grade[i]
    avg_grade=sum_of_grade/number_of_students
    return avg_grade
 