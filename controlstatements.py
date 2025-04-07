a=23
b=12
if b>a:
    print("b is greater than a")
elif a==b:
    print("both are equal")
else:
    print("a is greater than b")
    
    
i=0
if i!=0:
    if i>0:
        print("positive")
    if i<0:
        print("negative")
else:
    print("zero")
    
# marks=int(input())
# if marks>=90 and marks<=100:
#     print("grade A")
# elif marks>=80 and marks<90:
#     print("grade B")
# elif marks>=70 and marks<80:
#     print("grade C")
# elif marks>=60 and marks<70:
#     print("grade D")
# else:
#     print("fail")
    
# loops

n=5
while n>0:
    n=n-1
    print(n)
    
n=5
while n>0:
    n=n-1
    if n==2:
        break
    print(n)
    
n=5
while n>0:
    n=n-1
    if n==2:
        continue
    print(n)
    


# for loop
l=[1,2,34,7]
for i in l:
    print(i)
    
l=[1,2]
l1=[3,4]
for i in l:
    for j in l1:
        print(i,j)
        
# getting all the keys in dictionary
d={"name":"geethu","age":25,"salary":24000,"city":"ap"}
for i in d.keys():
    print(i)
    
# array    
import array   
fruits=array.array('u',"applebanana")# if we pass 3 charcters it will give error only atmost 2 characters are needed to array
print(fruits[0])
for i in fruits:
    print(i)
    
    
import array
num=array.array('i',[1,2,3,4,5])# for numbers we should use i as they are integers whereas for characters we need to give u
length=len(num)
print(length)

import array
num=array.array('i',[1,7,6,9,3])
sorted=sorted(num)
print(sorted)