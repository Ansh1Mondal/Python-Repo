# input function

# name = input("Enter your name:")
# print("Name is :", name)

# by default input takes strings

# a = input("enter the value of a:")
# b = input("enter the value of b:")
# print(a+b)
# print(int(a)+int(b))

# Strings

str1 = '''this
is 
a
multiline string techinique.'''
print(str1)

str2 = "to use 'quotes' this is the way to use it."
print(str2)

str3 = "ansh"
print(str3[3])

print("\n using for loop:")
for char in str3:
    print(char)

# string slicing

str4 = "Ansh.Mondal"
print(str4[0:4])  # last value is not included
print(len(str4))

print(str3.isalpha())
print(str3.capitalize())
print(str4.isalpha())
print(str4.swapcase())
