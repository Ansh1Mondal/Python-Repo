# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n*fact(n-1)


# print(fact(3))
# print(fact(4))
# print(fact(5))

def fib(n):

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (fib(n-1)+fib(n-2))


print(fib(2))

# f(0) = 0
# f(1) = 1
# f(2) = f(1)+f(0)
# fn = f(n-1)+f(n-2)
