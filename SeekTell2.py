with open('test4.txt','w') as f:
    f.write('Ansh Mondal')
    f.truncate(5)
    # this allows the file to get the size allowance of how much data can be inserted into it

with open('test4.txt','r') as f:
    print(f.read())