import time

def usingwhile():
    i=0
    while i<100:
        i=i+1
        print(i)

def usingfor():
    for i in range(100):
        print(i)

init = time.time() # this shows the total no. of seconds from the 1970 till now
usingfor()
t1=time.time() - init
print("t1:",t1)
init = time.time()
usingwhile()
t2=time.time()-init
print("t2:",t2)

print("calculating...")
time.sleep(2) # this is for waiting time 
if t1>t2:
    print("for is slower")
else:
    print("while is slower")

t=time.localtime()
formatted_time = time.strftime("%d-%m-%Y %H:%M:%S",t) # this is how we format the time
print("todays date and time :",formatted_time)