class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        animal.show_details(self)
        print(f"Breed:{self.breed}")

class husky(dog):
    def __init__(self, name, color):
        dog.__init__(self,name, breed="husky")
        self.color = color
    
    def show_details(self):
        dog.show_details(self)
        print(f"Color: {self.color}")

obj = husky("spike","black")
obj.show_details() # this is first executing its own lines of class husky then it is going up to the dog class then going to the animal class 

# to find the chain the mro() is used it is a method resolution operator 