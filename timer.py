import time

input("press enter to start timer")
start = int(time.time())
input("press enter to stop timer")
end = int(time.time())

print("time use:", (end - start))