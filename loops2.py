# for loop with else

for i in range(5):
    print(i+1)

else:
    print("printed no. till 5")

# else works only when the loop successfully finishes and there are no breaks

for i in range(10):
    print(i+1)
    if (i == 4):
        break

else:
    print("loop unfinished")
    # this statement has executed because the loop isn't finished successfully
