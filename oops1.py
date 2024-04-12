class Person:
    name="Ansh"
    occupation="Software Developer"
    salary=500000
    def info(self):
        print(f"{self.name} is a {self.occupation} and has a salary of {self.salary}")
        # self is the reference to the current isinstance of the class 
        # self ka matlb vo object jispe vo method call hora h

a = Person()
b=Person()
a.name = "Ansh Mondal"

print(a.name,"\n",a.occupation)
a.info()

b.name="Rishi"
b.info()