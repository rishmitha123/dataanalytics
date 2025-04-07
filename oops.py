# inheritance

# parent class 
class Person(object): 
  
    # __init__ is known as the constructor 
    def __init__(self, name, idnumber): 
        self.name = name 
        self.idnumber = idnumber 
  
    def display(self): 
        print(self.name) 
        print(self.idnumber) 
         
    def details(self): 
        print("My name is {}".format(self.name)) 
        print("IdNumber: {}".format(self.idnumber)) 
     
# child class 
class Employee(Person): 
    def __init__(self, name, idnumber, salary, post): 
        self.salary = salary 
        self.post = post 
  
        # invoking the __init__ of the parent class here the inhritance concept builds
        Person.__init__(self, name, idnumber) 
         
    def details(self): 
        print("My name is {}".format(self.name)) 
        print("IdNumber: {}".format(self.idnumber)) 
        print("Post: {}".format(self.post)) 
        print("salary: {}".format(self.salary)) 
a = Employee('Rahul', 886012, 200000, "Intern") 
  
# calling a function of the class Person using 
# its instance 
a.display()
a.details()


# polymorphism

class Bird: 
    def intro(self): 
        print("There are many types of birds.") 
    def flight(self): 
        print("Most of the birds can fly but some cannot.") 

 
class sparrow(Bird): 
   
    def flight(self): 
        print("Sparrows can fly.") 
  
class ostrich(Bird): 
  
    def flight(self): 
        print("Ostriches cannot fly.") 
  
obj_bird = Bird() 
obj_spr = sparrow() 
obj_ost = ostrich() 
  
obj_bird.intro() 
obj_bird.flight() 
  
obj_spr.intro() 
obj_spr.flight() 
  
obj_ost.intro() 
obj_ost.flight() 

# Encapsulation
class Student: 
    def __init__(self, name="Rajaram", marks=50): 
        self.name = name 
        self.marks = marks 
s1 = Student()  
s2 = Student("Bharat", 25) 
print ("Name: {} marks: {}".format(s1.name, s2.marks)) 
print ("Name: {} marks: {}".format(s2.name, s2.marks))
 

# abstraction
from abc import ABC, abstractmethod    
class Car(ABC):    
    def mileage(self):    
        pass   
 
   
 
   
class Tesla(Car):    
    def mileage(self):    
        print("The mileage is 30kmph")    
class Suzuki(Car):    
    def mileage(self):    
        print("The mileage is 25kmph ")    
class Duster(Car):    
     def mileage(self):    
          print("The mileage is 24kmph ")    
   
class Renault(Car):    
    def mileage(self):    
            print("The mileage is 27kmph ")    
           
# Driver code    
t= Tesla ()    
t.mileage()    
   
r = Renault()    
r.mileage()    
   
s = Suzuki()    
s.mileage()    
d = Duster()    
d.mileage()  

