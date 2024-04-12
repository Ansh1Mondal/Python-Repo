def double(x):
    return x*2

print(double(5))

# the above one is normal function

triple = lambda y: y*3
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(triple(4))
print(cube(5))
print(avg(2,3,4))

# this is a lambda function
# this can be used to write mini functions

def appl(fn,value):
    return 10+ fn(value)

print(appl(cube,(2)))
# this is function as an argument