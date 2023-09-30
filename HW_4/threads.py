import requests
import threading
import time
from urls import urls



def download(url, index):
    response = requests.get(url)
    filename = 'threads_image_' + str(index) + ".jpg"
    with open(f"images/{filename}", "wb") as f:
        f.write(response.content)
    print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")


threads = []
start_time = time.time()


if __name__ == "__main__":
    for index, url in enumerate(urls, 1):
        thread = threading.Thread(target=download, args=[url, index])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()