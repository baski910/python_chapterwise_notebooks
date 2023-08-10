# thread example
# threading module is used for creating thread in python
import time
import threading

def sleeper(n):
    print("threading is going to sleep for {} seconds".format(n))
    time.sleep(n)
    print("threading completed")

t1 = threading.Thread(target=sleeper,args=(5,))

t1.start()

print("Done...")
