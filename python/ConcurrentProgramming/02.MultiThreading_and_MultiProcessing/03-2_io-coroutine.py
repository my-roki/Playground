import asyncio
import aiohttp
import time
import os
import threading


async def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://google.com", "https://apple.com"] * 10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end = time.time()
    print(end - start)  # 0.6809983253479004
