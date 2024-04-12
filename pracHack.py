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


# a = []
# a.append(input())
# print(max(a))

# METHOD 1
# n = int(input())
# a = []
# for i in range(n):
#     b = input()
#     a.append(b)

# a.sort()
# t = a[-1]
# if (a[-1] == t):
#     a.pop()
# else:
#     print(a[-1])

# METHOD 2
# n = int(input())
# a = []
# a = input()
# b = a.split(" ")
# c = 0

# for i in range(len(b)):
#     c.append(abs(int(b[i])))

# b.sort()
# print(b)
# i = 0
# t = b[-1]

# print(type(t))
# for i in range(n):
#     if (int(b[-2]) > int(t)):
#         # print(b)
#         # print(t)
#         c = b[-2]
#         break
#     if (int(b[-2]) == int(t)):
#         b.pop()
#         # print(b)
#         # print(b[-1])
#         c = b[-1]
#     if (int(b[-2]) < int(t)):
#         c = b[-1]

# print(c)

#################################################

# def split_and_join(line):
#     a = line.split(" ")
#     b = "-".join(a)
#     return b


# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

#################################################

# def print_full_name(first, last):
#     # Write your code here
#     print(f"Hello {first} {last}! You just delved into python.")


# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

###############################################

# def mutate_string(string, position, character):
#     # converting string into llist to access the indexes of the string
#     l = list(string)
#     l[position] = character
#     string = "".join(l)
#     return string


# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

###############################################

# def count_substring(string, sub_string):
#     s1 = set()
#     s2 = set()
#     for i in range(0, len(string)):
#         s1.add(string[i])

#     for i in range(0, len(sub_string)):
#         s2.add(sub_string[i])
#     a = s1.intersection(s2)

#     return len(a)


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)

################################################

# n = int(input("enter the no. of students="))
# name = []
# marks = []
# i = 0
# j = 0
# for i in range(n):
#     name[i] = input("enter the name:")
#     for j in range(3):
#         marks[j] = input("enter marks:")

# print(name, marks)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
# a = student_marks.get(query_name)
# print(format((sum(a)/3), '.2f'))

#######################################
# n = input()
# eval(n)
#######################################

def swap_case(s):
    a = list(s)
    for i in range(len(s)):
        if a[i].islower():
            a[i] = a[i].upper()
        elif s[i].isupper():
            a[i] = a[i].lower()
    return "".join(a)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
