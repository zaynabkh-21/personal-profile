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
    print("Names: \t\t\t Grades:")
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
 
#function to get highest grade of the class
def get_heighest_grade(number_of_students,name,grade):
    heighst_grade=0
    student_of_heighst_grade=""
    for i in range (number_of_students):
        if grade[i]>heighst_grade:
            heighst_grade=grade[i]
            student_of_heighst_grade=name[i]
    print( "the heighst grade is for ",student_of_heighst_grade,"of grade is ",heighst_grade)

#recursive function to count the number of students with grade >=60
def count_passed(number_of_students,grade,count_students,i):
   if number_of_students==0:
     return count_students
   else :
     if grade[i]>=60 :
       count_students +=1
       i=i+1
     return count_passed(number_of_students-1,grade,count_students,i)

#call the function display_students_name
display_students_summary(num_of_students,student_name,student_grade)

print("The avg grade of the class :")
#call the function get_avg_grade
print(get_avg_grade(num_of_students,student_grade))

#call the function get_heighest_grade
get_heighest_grade(num_of_students,student_name,student_grade)

print("The number of students who passed are :")
#call the function count_passed
print(count_passed(num_of_students,student_grade,0,0))

#the prgram works as expected 
#user enters the number of students and their name and grade
#the program display the list of name and grade of the students
#the program display the average grade of the class
#the program display the highest grade of the class
#the program count recursivly the number of students who passed (grade>=60)
#taking into consideration the time complexity of the program

