# match case

a = int(input("enter the value of a (1 to 3):"))

match (a):
    case 1:
        print("wow")
    case 2:
        print("superb")
    case 3:
        print("get lost")
    case _:
        # this is the default statement
        print("choose within the limit you gawar")
