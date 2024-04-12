# hybrid and heirarchical inheritance
class Base:
    pass

class derived1(Base):
    pass

class derived2(Base):
    pass

class derived3(derived1, derived2):
    pass

# this above eg is of the hybrid inheritance

class Base:
    pass

class D1(Base): 
    pass

class D2(Base):
    pass

# this is an eg of heirarchical inheritance 