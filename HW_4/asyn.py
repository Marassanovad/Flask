import asyncio
import aiohttp
import time
from urls import urls


async def download(url, index):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image = await response.read()
            filename = 'async_image_' + str(index) + ".jpg"
        with open(f"images/{filename}", "wb") as f:
            f.write(image)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for index, url in enumerate(urls, 1):
        task = asyncio.create_task(download(url, index))
        tasks.append(task)
        await asyncio.gather(*tasks)


start_time = time.time()
if __name__ == "__main__":
    asyncio.run(main())