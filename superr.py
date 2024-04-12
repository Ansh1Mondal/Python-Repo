# Super keyword

class ParentCLass:
    def parent_method(self):
        print("this is the parent method.")

class ChildClass(ParentCLass):
    def parent_method(self):
        print("Ansh")
        # super().parent_method()
    def child_method(self):
        print("this is the child method.")
        super().parent_method()            # this is used to refer the parent class and to get some of the objects from a particular class when there are multiple parent classes

child_object=ChildClass()
child_object.child_method()
child_object.parent_method()


########## ANOTHER EXAMPLE

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)      # we are inheriting the properties of super class or parent class
        self.lang = lang
    
a=Employee('ansh',"123")
b=Programmer('amesterio','234','python')

print(a.name)
print(a.id)
print(b.name)
print(b.id)
print(b.lang)
