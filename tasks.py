
# grades
marks=int(input("enter marks :"))
if marks>=90 and marks<=100:
    print("grade A")
elif marks>=80 and marks<90:
    print("grade B")
elif marks>=70 and marks<80:
    print("grade C")
elif marks>=60 and marks<70:
    print("grade D")
else:
    print("fail")

# palindrome
a="anuradha"
k=a[::-1]
if k==a:
    print("palindrome")
else:
    print("not palindrome")

n=int(input("enter number :"))
orig=n
rev=0
while n!=0:
    temp=n%10
    rev=rev*10+temp
    n=n//10
if rev==orig:
    print("palindrome")
else:
    print("not palindrome")
    
    
# prime
n=int(input("enter value :"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not prime")
    
# even or not
n=int(input("enter number :"))
if n%2==0:
    print("even number")
else:
    print("odd number")

# fibonacci
def fibonacci(n):
    a=0
    b=1
    for i in range(n+1):
        print(a,end=" ")
        a,b=b,a+b
n=int(input("enter number of terms :"))
print(fibonacci(n))

# # range function
output=[i if i%2!=0 else  '@' for i in range(1,101) ]
print(output)

#squaring the collection elements 
l=[1,2,3,4,5,6]
for i in l:
    print(i**2,end=' ')
    
# retieve key and based on key display the value
d={"name":"rishmi","age":22,"city":"nuzvid","state":"ap"}
for i in d.keys():
    key=input("enter key value :")
    if key in d:
        print(d[key])

# functions
def getDetails():
    details={}
    details["name"]=input("enter name :")
    details["age"]=int(input("enter age :"))
    details["address"]=input("enter address :")
    return details
def display(details):
    for key,value in details.items():
        # print(f"{key}:{value}")
        print(key,":",value)
info=getDetails()
display(info)

# tuple functions
t=(1,2,3,4,5)
print(len(t))
print(min(t))
print(max(t))
l=list(t)
l.insert(1,"hello")
l.pop()
print(l)
print(tuple(l))
    