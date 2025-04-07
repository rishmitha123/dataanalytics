# function without parameters
def greet():
    print("hello welcome")
greet()

# functions with parameters
def greet(name):
    print("hello welcome",name)
greet('anu')

def add(a,b):
    return a+b
result=add(3,5)
print("sum :",result)

# default parameter
def greet(name="greece"):
    print("hello",name)
greet()
greet('anu')

# function with multiple return values
def get_details():
    name='ajay'
    age=23
    return name,age
n,a=get_details()
print("name",n, "|age",a)

# function with multiple arguments using *(here *num represents a tuple)
def add_all(*num):
    return sum(num)#here sum is predefined function
print(add_all(1,2,3,4,5))

# functions with kwargs(**)keyword arguments
def info(**data):
    for key,value in data.items():#here item is predefined method
        print(key,":",value)
info(name="alice",age=24)

def fun1(msg):
    def fun2():
        print(msg)
    fun2()
fun1("hello")