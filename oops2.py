# Constructor 

class Employee:

    def __init__(self,n,o):
        print("this is a constructor , it is called everytime when an obj of class is created")
        self.name = n
        self.occ = o
    # name = "Ansh M"
    # occ = "Developer"

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Employee("Ansh","Developer")
b = Employee("Amesterio","Gamer")

a.info()
b.info()
# a.name="Ansh Mondal"
# a.info()
