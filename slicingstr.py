# str1 = "Ansh "
# str2 = "Mondal"
# str3 = str1+str2
# print(str3)
# print(str3[0:6])  # till 5 it will read
# # when the size of the sting is unknown and you have to access the last element
# print(str3[-1])
# # [first value : last value (leave blank for last): values to be skipped]
# print(str3[0::2])

# # String functions

# str5 = "Hello Everyone this is a string"

# print("no. of characters or length of string is :", len(str5))
# print(str5.endswith("string"))
# print(str5.count("e"))
# print(str5.find("a"))  # -1 if not founded
# print(str5.replace("Everyone", "Ansh"))

# Practice set

a = input("Enter your name:\n")
print("Good afternoon", a)


letter = ''' Dear, <name>
           You are selected !!!
           <date>'''

name = input("Enter the name for the letter:\n")
date = input("Enter the date for the letter:\n")

letter = letter.replace("<name>", name)
letter = letter.replace("<date>", date)

print(letter)
