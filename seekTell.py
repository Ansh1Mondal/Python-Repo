with open('test1.txt','r') as f:
    print(type(f))

    f.seek(10) 
    # move to the 10th byte of the file 


    print(f.tell())
    # tells about the current position
    data = f.read(5)

    # read the next five data 
    print(data)