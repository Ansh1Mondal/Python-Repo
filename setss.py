# sets are unordered collection of data items.
s = {1, 2, 3, 4, 1, 2, "ansh", False, 10}
print(s)
# set doesn't takes repeated values count them only once
# have almost all the methods like that of list
# there is no fixed order of printing of sets
s1 = {}
s2 = set()  # to create an empty set we must write like this
print(type(s))
print(type(s1))
print(type(s2))

for value in s:
    print(value)

# SETS METHODS

s3 = {1, 2, 3, 4, 5}
s4 = {1, 3, 5, 6}
print(s3.union(s4))
print(s3.intersection(s4))
s3.update(s4)  # to update or change the value of s3
print(s3)

# similarly there are methods of union_update and intersection_update to update the default values of the set

print(s3.symmetric_difference(s4))  # values which are not common

print(s3.isdisjoint(s4))  # disjoint sets are those that has nothing in common

print(s3.issuperset(s4))

s3.add(7)
print(s3)

s3.remove(7)  # this gives error if the value is not present in the set
s3.discard(7)
# while this does not shows any error if the value is not present in the set
print(s3)

print(s3.pop())  # pops a random value as order does not matters in the sets

del s3  # is used to delete the entire set
s3.clear()  # is used to clear all the values of the set
