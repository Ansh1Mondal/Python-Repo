# KBC
print("WELCOME TO KBC")
print("(maximum points one can win is 10)")

questions = ["what is the national bird of India?",
             "what is the national animal of India?",
             "In which year India got its independence?",
             "How many states are there in India?",
             "What is the capital of India?"]

Canswers = ["peacock", "tiger", "1947", "29", "delhi"]

points = 0

print("Let's start the game!!!")

for i in range(len(questions)):
    print("Q", i+1, ".", questions[i])
    ans = input("Answer:")
    if (ans == Canswers[i]):
        points = points+2
        print("Point after this answer:", points, "\n")
    else:
        print("oops! wrong answer\n")

print("Your total win points are:", points)
