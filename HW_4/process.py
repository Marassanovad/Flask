import requests
from multiprocessing import Process
import time
from urls import urls

# urls = [
#     "https://i.pinimg.com/564x/c1/94/ca/c194ca73451c6b0f9b8ef5e1e67923e8.jpg",
#     "https://i.pinimg.com/564x/26/62/c4/2662c4a0743a12821917d7b5ddedb019.jpg",
#     "https://i.pinimg.com/564x/59/1a/59/591a598f3a6825f463b9844cc5a2fcfa.jpg",
#     "https://i.pinimg.com/564x/a9/f9/7b/a9f97b04b55619c90b1c97b172b65924.jpg",
#     "https://i.pinimg.com/564x/44/99/68/449968ef6624a7040902350b2b707187.jpg",
#     "https://i.pinimg.com/564x/f5/a3/8a/f5a38a9408e9eb9a9c33023896da2648.jpg",
#     "https://i.pinimg.com/564x/8e/ba/cb/8ebacbc531ba5c7931f033f959a2d394.jpg",
#     "https://i.pinimg.com/564x/7c/28/92/7c2892e7e0835726c436cf27cafa2456.jpg",
#     "https://i.pinimg.com/564x/06/ad/85/06ad85ee362117581d5747c050f93d34.jpg",
#     "https://i.pinimg.com/564x/b2/36/7c/b2367cb94834c2dbaac1ec6e4042196a.jpg",
# ]

def download(url, index):
    response = requests.get(url)
    filename = 'multiprocessing_image_' + str(index) + ".jpg"
    with open(f"images/{filename}", "wb") as f:
        f.write(response.content)
    print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")


processes = []
start_time = time.time()

if __name__ == "__main__":
    for index, url in enumerate(urls, 1):
        process = Process(target=download, args=(url, index))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()