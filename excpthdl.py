a = input("Enter the no. for the table: ")
print(f"the table of {a}")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {int(i)} = {int(a)*i}")

except:  # Exception as e: if we are not using e then no need to write this
    # print("error is: ", e)
    print("please enter a valid number")

print("program ends")

# specific kind of error

try:
    num = int(input("enter an integer: "))
    a = [0, 1]
    print(a[num])

except ValueError:
    print("enter a valid number")

except IndexError:
    print("enter a valid index")
