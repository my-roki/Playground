# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install beautifulsoup4

# https://github.com/Tinche/aiofiles
# pip install aiofiles==0.7.0

"""
웹 크롤링 : 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑 : 웹에서 데이터를 수집하는 프로그램
"""

import os
import asyncio
import aiohttp
import aiofiles
import time

from config import get_secret


async def image_downloader(session, img_url):
    img_name = img_url.split("/")[-1]

    try:
        os.makedirs("./images", exist_ok=True)
    except FileExistsError:
        pass

    async with session.get(img_url) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)


async def fetch(session, url):
    headers = {
        "X-Naver-Client-Id": get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET"),
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        # print(result)
        items = result.get("items")
        images = [item.get("link") for item in items]
        # print(images)

        await asyncio.gather(*[image_downloader(session, img_url) for img_url in images])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    query = "IU"
    urls = [f"{BASE_URL}?query={query}&display=20&start={1+(i*20)}" for i in range(10)]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
