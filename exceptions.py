try:
    x=10/0
except ZeroDivisionError:
    print("divided by zero")
finally:
    print("program completed")
    
try:
    num=int(input("enter num"))
    result=10/num
except ValueError as e:
    print("invalid input :{e}")
except ZeroDivisionError as e:
    print("divided by zero")
except Exception as e:
    print("unexpected")
else:
    print(f"result :{result}")
finally:
    print("code executed successfully")
    
    
def checkAge(age):
    if age<18:
        raise ValueError("age must be 18")#it is similar tomthrow in java which is ued to throw 
    else:
        print("eligible")
try:
    checkAge(16)
except ValueError as e:
    print("error")
    
# custom exception 
class noteligibleexception(Exception):
    pass
def checkAge(age):
    if age<18:
        raise ValueError("age must be 18")
    else:
        print("eligible")
try:
    checkAge(16)
except noteligibleexception as e:
    print("error")

        
    
    