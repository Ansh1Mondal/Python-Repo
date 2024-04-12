class employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"the name is {self.name}")

class dancer:
    def __init__(self,style):
        self.style = style
    def show(self):
        print(f"the name is {self.name}")

class dancerEmployee(employee,dancer):
    def __init__(self, name,style):
        self.style=style
        self.name=name

one = dancerEmployee("rohan","hip hop")
print(one.name)
print(one.style)

one.show() # the show line of employee will be printed because the employee class is inherited first in the dancerEmployee class