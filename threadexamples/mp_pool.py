import multiprocessing
import requests

def fetch_url(url):
    response = requests.get(url)
    return f"{url}: {response.status_code}"

urls = ["https://example.com", "https://google.com", "https://github.com"]

with multiprocessing.Pool(processes=3) as pool:
    results = pool.map(fetch_url, urls)

print(results)
