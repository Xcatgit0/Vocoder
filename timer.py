import time

input("press enter to start timer")
start = float(time.time())
input("press enter to stop timer")
end = float(time.time())

result = end - start
print("time use: {:.2f}".format(result))