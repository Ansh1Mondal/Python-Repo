f = open("test3.txt", 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    # this method is opening the file and using that variable reading the line of the files
    # this readline method is used when there are more than one lines in a file
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    # all the above values are str so to obtain the integer values we need to typecast these
    print(f"Marks of student {i} in maths is:{m1}")
    print(f"Marks of student {i} in maths is:{m2}")
    print(f"Marks of student {i} in maths is:{m3}")

    # print(line)

#################################################################

# f = open("test2.txt", 'w')
# lines = ["line 1\n", "line 2\n", "line 3\n"]
# f.writelines(lines)
# # writelines does not adds new lines to the document we have to do this by us
# f.close()
