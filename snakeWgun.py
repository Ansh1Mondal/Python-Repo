import random
user = int(input("0 for snake, 1 for water and 2 for gun"))

comp = (random.randint(0,2))

if (user == 0 and comp==0):
    print("draw, you both chose snake")
elif (user == 1 and comp == 1):
    print("draw, you both chose water")
elif ( user == 2 and comp == 2):
    print("draw, you both chose gun")
elif (user == 0 and comp == 1):
    print("you chose snake and comp chose water so you won!")
elif(user == 0 and comp == 2):
    print("you chose snake and comp chose gun so you lost!")
elif(user == 1 and comp == 0):
    print("you chose water and comp chose snake so you lost!")
elif(user == 1 and comp == 2):
    print("you chose water and comp chose gun so you won!")
elif(user == 2 and comp == 0):
    print("you chose gun and comp chose snake so you won!")
elif(user == 2 and comp == 1):
    print("you chose gun and comp chose water so you lost!")
else:
    print("wrong choice!!!")