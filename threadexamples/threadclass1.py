import threading
import time

class CustomThread(threading.Thread):
	def __init__(self,threadID,name,timegap):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.timegap = timegap
        
	def run(self):
		print("starting"+self.name)
		print_time(self.name,self.timegap,5)
		print("Exiting"+self.name)

def print_time(threadName,delay,counter):
	while counter:
		time.sleep(delay)
		print("%s: %s" %(threadName,time.ctime(time.time())))
		counter -= 1


thread1=CustomThread(1,"Thread-1",1)
thread2=CustomThread(2,"Thread-2",2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")
