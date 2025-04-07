class dog:
    sound="bark"
obj=dog()
print(obj.sound)


class Person:
    # self is a referecnce to  current instance of class 
        def __init__(self, name, age): 
            # init is a constructor (automatically called when a  object is created) which is called whenever an instace is created and intializes the attributes when object is created
            self.name = name  # Assigning the name attribute (instance attributes)
            self.age = age  # Assigning the age attribute 
 
    # Creating an object 
person1 = Person("Alice", 25) 
print(person1.name)  # Output: Alice
print(person1.age)  # Output: 25 
    
            

class Example: 
        # Default Constructor 
    def __init__(self): 
        self.value = 0 
 
        # Non-Parameterized Constructor 
    def __init__(self): 
        self.value = 10 
 
        # Parameterized Constructor 
    def __init__(self, value): 
        self.value = value 
e=Example(10)
print(e)

class Player: 
    team_name = "Dragons"  # Class attribute 
 
    def __init__(self, name): 
        self.name = name 
 
player1 = Player("Alice") 
player2 = Player("Bob") 
Player.team_name="rcb"
 
print(player1.team_name)  # Output: Dragons 
print(player2.team_name)  # Output: Dragons


class Player: 
    team_name = "Dragons"#class variable
    def __init__(self, name, score): 
        self.name = name 
        self.score = score 
 
player1 = Player("Alice", 100) 

player2 = Player("Bob", 50) 
print(player1.score)  # Output: 100 
print(player2.score)  # Output: 50


class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
p1 = Person("John", 36) 
print(p1.name) 
print(p1.age)
 
 
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def myfunc(self): 
        print("Hello my name is " + self.name) # self is not predefined we can use any of the identifier but for our convinience we are uisng self
p1 = Person("John", 36) 
p1.myfunc() 


class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def myfunc(self): 
        print("Hello my name is " + self.name) 
p1 = Person("John", 36) 

p1.age = 40  
print(p1.age)

# # inheritance

# # parent class 
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
 

