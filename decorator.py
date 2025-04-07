import inspect
def decorator(func):#func=greet
    def wrapper():
        print("before caling the function")
        func()
        print("after calling the function")
    return wrapper

@decorator#greet=decorator(greet)

def greet():
    print("hello world!")
greet()

# when we call th egreet function the decorator would be invoked and that codde will be executed
# it is used to extend the behaviour of fucntion without changing the codes
# decorator uses only wrapper function to wrap and execute the code


print(inspect.signature(decorator))