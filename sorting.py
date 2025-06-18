#selection sort
def select(s):
    n=len(s)
    for i in range (n-1):
        small=i
        for j in range (i+1,n):
            if s[j]<s[small]:
                small=j
        if small != i:
            t=s[i]
            s[i]=s[small]
            s[small]=t
#test
list=[1,-2,-5,6]
select(list)
print("selection sort",list)

#bubble sort
def bubble(s):
    n=len(s)
    for i in range (n-1):
        for j in range (n-1-i):
            if s[j]>s[j+1]:
                t=s[j]
                s[j]=s[j+1]
                s[j+1]=t
#test
list=[1,-2,-5,6]
bubble(list)
print("bubble sort",list)

#insertion sort
def insert(s):
    n=len(s)
    for i in range (1,n):
      value=s[i]
      pos=i

      while pos>0 and value<s[pos-1]:
          s[pos]=s[pos-1]
          pos-=1
      s[pos]=value

#test
list=[1,-2,-5,6]
insert(list)
print("insertion sort",list)


#merge sort 
def merge(i):
    if len(i)<=1:
        return
    mid=len(i)//2
    left=i[:mid]
    right=i[mid:]
    merge(left)
    merge(right)

    ii=0
    li=0
    ri=0
    while li<len(left) and ri<len(right):
        if left[li]<right[ri]:
            i[ii]=left[li]
            li+=1
        else:
            i[ii]=right[ri]
            ri+=1
        ii+=1
    while li<len(left):
        i[ii]=left[li]
        li+=1
        ii+=1
    while ri<len(right):
        i[ii]=right[ri]
        ri+=1
        ii+=1
    



#test
list=[1,-2,-5,6]
merge(list)
print("merged sort",list)

#quick sort 

def part(s,first,last):
   pivot=first
   left=first-1
   right=last

   while left<=right:
       while left<right and s[left]<pivot:
           left+=1
       while right>=left and s[right]>=pivot:
           right-=1
       if left<=right:
           tem=s[left]
           s[left]=s[right]
           s[right]=tem
           left+=1
           right-=1
   if  right!=first:
       s[first]=s[right]
       s[right]=pivot
   return right
       
#test
list=[1,-2,-5,6]
merge(list)
print("quick sort",list)



def exponent_of_list(list):
    while i <len(list):
        if list[i]>0:
           list[i]*=list[i]
        i+=1
    return list
a=[1,-10,3]
print(exponent_of_list(a))
