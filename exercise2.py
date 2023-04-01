import time
time1 = time.strftime("%H:%M:%S")
print("the time is : ", time1, " hrs")

timestamp = time.strftime('%H')

if (int(timestamp) >= 12 and int(timestamp) < 17):
    print("good afternoon sir")
elif (int(timestamp) >= 17 and int(timestamp) < 0):
    print("good night sir")
elif (int(timestamp) < 12 and int(timestamp) >= 0):
    print("good morning sir")
