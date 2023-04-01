# n = int(input())
# if (n % 2 == 0):
#     if (2 <= n <= 5):
#         print("Not Wierd")
#     elif (6 <= n <= 20):
#         print("Weird")
#     elif (n > 20):
#         print("Not Weird")
# else:
#     print("Weird")


# n = int(input())
# for i in range(n):
#     if (i < n):
#         print(i*i)


# def is_leap(year):
#     leap = False

#     if (year >= 2000 and year < 2100):
#         if (year % 4 == 0):
#             leap = True
#     elif (year < 2000):
#         if ((year/100) % 4 == 0):
#             leap = True
#         elif (year % 4 == 0):
#             leap = True
#     elif (year > 2100 and year < (10*10*10*10*10)):
#         if ((year/100) % 4 == 0):
#             leap = True
#         elif (year % 4 == 0):
#             leap = True

#     return leap

# year = int(input())
# print(is_leap(year))


# n = int(input())
# for i in range(n):
#     print(i+1, end="")


a = []
a.append(input())
print(max(a))
