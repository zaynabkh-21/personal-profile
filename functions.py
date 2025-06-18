def sum(number):
    if number<=0:
        return 0
    else:
     return number + sum(number-1)
print(sum(10))


def factorial(f):
   if f==1 or f==0:
      return 1
   else:
      return f* factorial(f-1)
print(factorial(4))



def fibonacci(num):
   if num==0:
      return 0
   if num==1:
      return 1
   return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(2))


def strings(list):
   list.lower()
   vowels='aioue'
   count=0
   for i in range (len(list)):
      if i in vowels:
         count+=1
      return count
   

print(strings('hello'))


def multi(list):
   
   if len(list)==0:
      return 0
   if len(list)==1:
      return 1
   else:
      num=list.pop()
      return num*multi(list)
   
def ast_rec(num):
   if num<=0:
      return 
   else:
     print("*"*num)
     ast_rec(num-1)

      
      
def multi(list):
   
   if len(list)==0:
      return 0
   if len(list)==1:
      return 1
   else:
      num=list.pop()
      return num*multi(list)
   
def ast_rec(num):
   if num<=0:
      return 
   else:
     print("*"*num)
     ast_rec(num-1)

def pstv(list):
   for i in range (len(list)):
      if list[i]>=0:
         print(list[i])
      else:
         continue
def pstv_rec(list):
   i=len(list)
   pos_list=[]
   if i>=0:
     
      if list[i]>=0:
         pos_list.append(list[i])

def calc(a,b):
   if b==0:
     return a
    
