# lambda functions
# variable=lambda argument:expression
s1="hello"
func=lambda a:a.upper()
print(func(s1))

n=lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
print(n(5))
print(n(-3))
print(n(0))

sq=lambda x:x**2
print(sq(2))

li=[lambda arg=x:arg *10 for x in range(1,5)]
for i in li:
    print(i())#return values 10,20,30,40
    print(i)#address would be printed

check=lambda x:"even" if x%2==0 else "odd"
print(check(4))
print(check(3))

calc=lambda x,y:(x+y, x*y)
res=calc(3,4)
print(res)
# it filters the data based on a condition
n=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,n)
print(list(even))
# map iterates through every element in the function and perform modifications
n=[1,2,3,4,5,6]
mul=map(lambda x:x*2,n)
y=lambda x:x*2,n
print(y)
print(list(mul))

# reduces the whole list

from functools import reduce
a=[1,2,3,4]
b=reduce(lambda x,y:x*y,a)
print(b)   


    