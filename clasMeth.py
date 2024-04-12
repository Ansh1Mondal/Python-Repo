class Employee:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and company name is {self.company}")

    @classmethod
    def changeComp(self,NewComp):
        self.company = NewComp # this changes the company name for just and instance not the original variable but the decorator makes it to change the variable

e1=Employee()
e1.name = "Ansh"
e1.show()
e1.changeComp("Google")
e1.show()
print(Employee.company)

####################################### CLASS METHODS AS ALTERNATIVE CONSTRUCTORS (70th video important)

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(self,string):
        return self(string.split("-")[0],int(string.split("-")[1]))

e = employee("Ansh",50000)
print(e.name)
print(e.salary)

string = "Amesterio-50000"
e = employee.fromStr(string)
print(e.name)
print(e.salary)