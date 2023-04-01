# tuples cannot be changed like lists

t1 = (1, 2, 3, 4, 5, 6)
print(type(t1), t1)
print(t1[5])
# used when we need a constant list that cannot be changed

if 3 in t1:
    print("yes")

# sliced t1 and made an new tuple t2 with the sliced values
t2 = t1[1:3]
print(t2)

t3 = t1+t2
print(t3)

# OPERATIONS IN TUPLES

food = ("momos", "chowmine", "pizza", "burger")
print(food)

foods = list(food)  # changed into list for using methods

foods.append("shawarma")
print(foods)
foods.pop(3)
# print(foods)

food = tuple(foods)  # changed into tuple after applying changes
print(food)

c = t3.count(3)
print("3 occurs", c, "times")
