name=input("Enter your name:")
print("hello",name)
age=int(input("enter you age :"))
print("so ",name,"you are",age,"years old")
print("let me tell you about our program ")
print("our program afford scholarships and internships")
print("first ,are you a graduated student ?")
graduation=input()
print("if your intereted enter the following to see what we can afford to you: ")
GPA=float(input("GPA: "))
FOI=input("field your interest on :")
if age<25 and GPA>=3.5 and graduation=="yes":
    print("your eligible for a scholarship in",FOI)
elif age<30 and GPA>=2.5:
    print("your eligible for an internship in",FOI)
else :
    print("sorry maybe later you can register to our company ")
    print(" please apply again later on ")




