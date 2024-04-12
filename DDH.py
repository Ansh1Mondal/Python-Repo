# DDH = dir() __dict__ help() 

x= [1,2,3]
print(dir(x)) # it tells us about which methods we can run on the list

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
        self.gender = 'male'
    
p=Person('ansh',22)
print(p.__dict__) #it gives a dictionary representation of the objects provided to it


print(help(Person)) # this help method is used to get help for the documentation for an ovject including a description of its attributes