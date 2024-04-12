# f string is used for string formatting in python

line = "My name is {} and I am from {}"
name = "Ansh"
place = "Delhi"

print(line.format(name, place))  # old method

print(f"My name is {{name}} and I live in {place}")  # f string method

price = 12.0999
# this is for getting only 2 decimal places
line2 = f"price is only {price:.2f}"
print(line2)

print(f"{20*30}")
# this is how calculations are done and displayed as a string
