l = [1, 2, 3, 4, 5, "ansh", True]
print(l)
print(type(l))
print(l[1])

print(l[-3])
print(l[len(l)-3])
print(l[7-3])
print(l[4])
# the above all are same

if 4 in l:
    print("yes")
else:
    print("no")

print(l[1:-1])
print(l[1:7-1:2])  # 2 is the jump index prints every second element of the list

print("\n new lists")

l2 = [i for i in range(4)]
print(l2)

l3 = [i*i for i in range(4)]
print(l3)

l4 = [i for i in range(10) if i % 2 == 0]
print(l4)


# LIST METHODS
l.append("Mondal")
print(l)
l.reverse()
print(l)

l4.sort(reverse=True)
print(l4)
print(l4.index(4))

m = l.copy()  # this copy is used so that the main list is not edited or changed instead a copy of it is changes i.e m
# and if we dont use the copy method the main string will also change
m[0] = 0
print(m)
m.insert(1, "mondal")
print(m)

l.extend(l2)  # open the l2 list and add it to the end of the l list
print(l)

l5 = l3+l4
print(l5)  # this is also lists can be concatenated
