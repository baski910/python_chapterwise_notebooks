import threading
import time

class MyThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print("starting"+self.name)
		threadLock.acquire()
		print_time(self.name,self.counter,5)
		threadLock.release()
		print("Exiting"+self.name)

def print_time(threadName,delay,counter):
	while counter:
		time.sleep(delay)
		print("%s: %s" %(threadName,time.ctime(time.time())))
		counter -= 1

threadLock=threading.Lock()

thread1=MyThread(1,"Thread-1",1)
thread2=MyThread(2,"Thread-2",2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")
		
