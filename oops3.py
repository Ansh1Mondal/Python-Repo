# Inheritance

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def ShowInfo(self):
        print(f"The name of the employee is {self.name} with id {self.id}")

class Programmer(Employee):
    def showLang(self):
        print("The language is python")


e = Employee("Ansh Mondal", 9)
f = Programmer("Amesterio",10) # this is an inherited class thus it can take the arguments for its parents class

e.ShowInfo()
f.ShowInfo()
f.showLang()