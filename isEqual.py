# "is" compares exact location of the obj in the memory while "==" compares the values of the objects

a = 4
b="4"

print(a is b)
print(a==b,"\n")

c=[1,2,3]
d=[1,2,3]
# they are creating different lists even the value is same for python they are at different places
print(c is d)
print(c == d,"\n")

e=5
f=5
# they both are pointing on the same memory, this even works for the tuple and strings as they have immutable values
print(e is f)
print(e == f)