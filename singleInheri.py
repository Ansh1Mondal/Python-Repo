class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made by the animal")

    
class Dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!!")

class Cat(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print("Meow!!")

    def charateristics(self):
        print("Lazy and does nothing!!")

d = Dog("dog","gali ka kutta")
d.make_sound()
print(d.breed)

a=animal("dog","dog")
a.make_sound()

c = Cat("cat","awara billi")
c.make_sound()
c.charateristics()
print(c.breed)