# MAP FILTER REDUCE
########### MAP
def cube(x):
    return x*x*x

# def square(x):
#     return x*x     instead of this we can use the lambda function

print(cube(2))

l1 = [1,2,3,4,5]

l2=[]
for item in l1:
    l2.append(cube(item))

print(l2)

# this is the basic way to append a list with values

# now there is an alternative called map
# here the map requires a function and the elements on which i will apply that function
l2 = map(lambda x: x*x,l1) #  this will return a map object so we need to convert it into string
l2 = list(l2)
print(l2)

############# FILTER

def filterVal(x):
    return x>3
# filtering values of the list according to the expression provided by the function
# it returns true of false for each value in the list ... if the value is true then only it will add it to the list 
l3 = list(filter(filterVal,l1)) # this also returns a filter object so converting it into list 
print(l3)

######### REDUCE
from functools import reduce

l4 = [1,2,3,4,5,6]

sum = reduce(lambda x,y: x+y,l4)
print(sum)
# this simply reduces the list by applying the function to the list