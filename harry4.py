# SEE THE 40TH VIDEO FOR THE STEPS OF TASK

print(''' The Encoder and Decoder:
1.Encode
2.Decode
''')
ans = int(input("Do you want to encode or decode your message(1 or 2):"))

match(ans):
    case 1:
        a = input("enter your message to encode:")
        # print(a)

        random = "abc"

        if (len(a) > 2):
            temp = a[0]
            # print(temp)
            a = a[1:]
            new = a+temp
            final = random+new+random
            print("Encoded message:", final)

        elif (len(a) <= 2):
            temp = a[0]
            # print(temp)
            a = a[1:]
            new = a+temp
            print("Encoded message:", new)

    case 2:
        b = input("enter the message to be Decoded:")

        if (len(b) > 2):
            b1 = b[3:-3]
            # print(b1)
            b2 = b1[-1]
            b3 = b1[0:-1]
            print("the decoded message is:", b2+b3)
        elif (len(b) <= 2):
            b2 = b[-1]
            b3 = b[0:-1]
            print("the decoded message is:", b2+b3)

    case _:
        print("choose only from the option:")
