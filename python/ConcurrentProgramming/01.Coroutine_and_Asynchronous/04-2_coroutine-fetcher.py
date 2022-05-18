# https://docs.aiohttp.org/en/stable/
# pip install aiohttp~=3.7.3

import aiohttp
import asyncio
import time


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        "https://naver.com",
        "https://www.google.com/",
        "http://13.209.92.28:15400/view/make",
        "https://github.com/my-roki",
    ] * 10
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end = time.time()
    print(end - start)
