# thread example
# threading module is used for creating thread in python
# create multiple threads with join primitive
import time
import threading

def sleeper(n):
    print("threading is going to sleep for {} seconds".format(n))
    time.sleep(n)
    print("threading {} completed".format(n))

threads = []
for i in range(1,6):
    t1 = threading.Thread(target=sleeper,args=(i,))
    threads.append(t1)

for t in threads:
    t.start()

# join - ensure the main process block till the completion of threads
for t in threads:
    t.join()

print("Done...")
