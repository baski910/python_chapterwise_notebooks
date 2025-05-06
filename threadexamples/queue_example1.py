import threading
import queue
import time

# Create a queue
data_queue = queue.Queue()

# Producer thread function
def producer():
    for i in range(5):
        item = f"Data {i}"
        data_queue.put(item)
        print(f"Produced: {item}")
        time.sleep(0.1)

# Consumer thread function
def consumer():
    while True:
        try:
            item = data_queue.get(timeout=1)  # Get with timeout to handle empty queue
            print(f"Consumed: {item}")
            data_queue.task_done()
            time.sleep(0.2)
        except queue.Empty:
            print("Queue is empty, exiting consumer")
            break


# Create and start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
data_queue.join()  # Wait for all tasks to be done
consumer_thread.join()

print("Both producer and consumer finished")
