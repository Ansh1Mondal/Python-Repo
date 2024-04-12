# READING A FILE

# f = open('test1.txt', 'r')
# r is for read mode and w is for write mode and by defalut r mode is default
# if we open a file in write mode that does not exists then it will create a file of that name
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open('test2.txt', 'w')
# f.write("BTech 4th year")
# f.close()

# a means append mode
# f = open('test1.txt', 'a')
# f.write(" Btech 4th year")
# f.close()

# this 'with' is used to open the file and doesnot needs a close operation it closes automatically
with open('test2.txt', 'a') as f:
    f.write(" this statements is inside with.")
