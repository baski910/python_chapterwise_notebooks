import multiprocessing
import requests

def fetch_url(url):
    response = requests.get(url)
    return f"{url}: {response.status_code}"

urls = ["https://example.com", "https://google.com", "https://github.com"]

with multiprocessing.Pool(processes=3) as pool:
    results = pool.map(fetch_url, urls)

print(results)


mport multiprocessing

def increment(shared_counter):
    for _ in range(100000):
        with shared_counter.get_lock():
            shared_counter.value += 1

counter = multiprocessing.Value('i', 0)  # Shared integer value

processes = [multiprocessing.Process(target=increment, args=(counter,)) for _ in range(2)]

for p in processes:
    p.start()

for p in processes:
    p.join()

print(f"Final counter value: {counter.value}")
