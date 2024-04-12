# Decorators = modifies the functions

def decorfunc(after):
    def before(*args,**kwargs): # *args takes tuple as an argument and **kwargs takes key value pairs as arguments
        print("Hello")
        after(*args,**kwargs)
        print("Thanks You")
    return before

@decorfunc # syntax of using decorator
def greet():
    print("Good Morning !")

greet() 

def add(a,b):
    print("sum is ",a+b)

decorfunc(add)(3,5) # this is also a method or syntax using of decorator

# video decorators day 59