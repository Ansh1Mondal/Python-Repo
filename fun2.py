# def avg(a=2, b=4):  # these are default values/arguments used if there are no values passed while calling
#     print("The average is=", (a+b)/2)


# avg(4, 6)

# avg(b=6, a=8)  # these are keyword arguments in which sequence doesn't matters

def avg(*num):  # num is a tuple this is how we define a tuple
    sum = 0
    for i in num:
        sum = sum+i
    print("the average is:", sum/len(num))


avg(1, 2, 3, 4, 5, 6, 7, 8, 9)
