class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x * self.y
    
class circle(shape):
    def __init__(self, rad):
        self.rad = rad
        super().__init__(rad, rad)
    
    def area(area):
        return 3.14 * super().area()
    
rec = shape(4,5)
print(rec.area())
c = circle(5)
print(c.area())