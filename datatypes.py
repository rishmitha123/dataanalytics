# strings
s="welcome to data analytics"
print(s)
print(type(s))
print(s[1])
print(s[8])
print(s[-1])

# list
l=eval(input("enter the list :"))
print(l)
print(type(l))

l1=[2,4,"rishmi",4+3j,True]
print(l1)
print(type(l1))
print(l1[2])
print(l1[3])
print(l1[-1])
l1[1]=2.567
print(l1)
# print(l1[-6])

# tuple
t1=(1,2,4,"hello",3.78)
print(t1)
print(type(t1))
print(t1[3])
print(t1[4])
print(t1[-1])

# boolean
a=True
print(a)
print(type(a))
b=False
print(type(b))

# set
s1=set("HelloWelcomeHelloWElcome")
print(s1)

s2=set(["hello","welcome","hello"])#removing the duplicates and this is set using list
print(s2)

# frozen set
fs=frozenset({1,2,3})
print(fs)
print(type(fs))
# fs.add(4)

# string sclicing
str="hello world"
print(str[1:4])
print(str[2:6])

# list functions
l1=[2,5,"anu",4+5j,True,4.67]

print(l1)
print(type(l1))
print(l1[0])
print(l1[-1])

# range
num=range(5,50,5)
num1=range(1,10,1)
print(list(num1))
print(list(num))



# dictionary
dict={"name":"rishmi","age":25,"city":"nuzvid"}
print(dict)
print(type(dict))
print(dict["city"])

b=bytes([65,66,67]) #returning the ascii characters 
print(b)
c=[65,66,67]
print(c)
d=bytes([69])
print(d,type(d))

x=None
print(x)
print(type(x))

# y
# print(y)
# print(type(y))