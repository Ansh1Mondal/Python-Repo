class employee:
    companyName = "Google" # this is a class variable that will remain same for all the instances 
    def __init__(self,name):
        self.name = name # these are instance variables which will be different for each instance created
        self.raise_amount = 20 # these are 
    def showDetails(self):
        print(f"The name of the employee is {self.name} who works in {self.companyName} and the raise amount is {self.raise_amount}%")
    
emp1 = employee("Ansh")
emp1.raise_amount = 30
emp1.showDetails()

emp2 = employee("amesterio")
emp2.companyName = "Apple"
emp2.showDetails()

# agr class variable ka insance variable hoga to vo show hoga lekin agr nahi hoga koi instance variable to class variable hi show hoga