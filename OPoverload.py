class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x):
        return vector(self.i + x.i , self.j + x.j , self.k + x.k)
    #this is how operator overloading is done , here addition is done through the dunder method add

v1=vector(1,2,3)
print(v1)

v2=vector(2,4,6)
print(v2)

print(v1+v2)