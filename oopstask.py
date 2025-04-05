#single inheritance

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def welcome(self):
        print("Hello from Child")

obj = Child()
obj.greet() 
obj.welcome()

# multilevel inheritance
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def say_hello(self):
        print("Hello from Parent")

class Child(Parent):
    def bye(self):
        print("bye from child")

obj = Child()
obj.greet()
obj.say_hello()  
obj.bye()

# heirarchial inheritance

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def hello(self):
        print("welcome from child 1")

class Child2(Parent):
    def bye(self):
        print("bye from child 2")

obj1 = Child1()
obj2 = Child2()

obj1.greet()
obj1.hello()
obj2.greet()
obj2.bye()

# multiple inheritance
class A:
    def hello(self):
        print("hello to multiple inheritance")

class B:
    def welcome(self):
        print("welcome all")

class C(A, B):
    pass

obj = C()
obj.hello()
obj.welcome()

# hybrid

class A:
    def methodA(self):
        print("Method A")

class B(A):
    def methodB(self):
        print("Method B")

class C(A):
    def methodC(self):
        print("Method C")

class D(B, C):
    def methodD(self):
        print("Method D")

obj = D()
obj.methodA() 

# method overloading
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5)) 
print(calc.add(5, 3)) 
print(calc.add(5, 3, 2)) 

# method overriding

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

a = Animal()
d = Dog()
print(a.sound()) 
print(d.sound()) 

# public anywhere in the program it wont have any unserscore
class Car:
    def __init__(self):
        self.brand = "Toyota" 

c = Car()
print(c.brand) # Toyota

# protected which are accessible within classes and their subclasses
class Car:
    def __init__(self):
        self._speed = 120 # Protected

class SportsCar(Car):
    def show_speed(self):
        print("Speed:", self._speed)

s = SportsCar()
s.show_speed() # Speed: 120
print(s._speed)

# private which can be accessed only in that class
class Car:
    def __init__(self):
        self.__engine_number = "ABC123" # Private

    def show_engine(self):
        print(self.__engine_number)

c = Car()
c.show_engine() # ABC123
# print(c.__engine_number) 
# print(c._Car__engine_number) # Still accessible via name mangling

