x = 10  # global variable
print(x)


def fun1():

    global x
    x = 11  # local variable

    print("inside fun1")
    print(x)


fun1()
print(x)
