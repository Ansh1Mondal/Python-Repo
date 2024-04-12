# access specifiers/modifiers  public private protected

# PRIVATE 
class employee:
    def __init__(self):
        self.__name = "ansh" # the __ makes the variable private or cannot be accessed directly

a=employee()
# print(a.name) cannot be accessed directly
print(a._employee__name) # can be accessed this way
#########################################

# PROTECTED

class student:
    def __init__(self):
        self._name = "ansh"

    def _funName(self):
        return "ansh mondal"
    
class Subject(student):
    pass

obj = student()
obj2 = Subject()

print(obj._name)
print(obj._funName())

print(obj2._name)
print(obj2._funName())