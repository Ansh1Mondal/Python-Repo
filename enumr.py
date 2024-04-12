# ENUMERTATE FUNCTION

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# index = 0
# for num in numbers:
#     print(num)
#     if (index == 5):
#         print("you are in middle")
#     index += 1

# to avoid the assigning the index we can use enumerate


# this gives the inde3x automatically
for index, num in enumerate(numbers, start=1):
    print("index=", index,  "value=", num)
    if (index == 4):
        print("you are in middle")


# SEE THE 43RD VIDEO TO KNOW HOW TO CREATE VIRTUAL ENVIRONMENT OF PYTHON AND ALSO VERSION CONTROL INSTALLATION OF LIBRARIES
