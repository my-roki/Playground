# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install beautifulsoup4

"""
웹 크롤링 : 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑 : 웹에서 데이터를 수집하는 프로그램
"""

import asyncio
import aiohttp

from config import get_secret


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
        print(images)


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    query = "아이유"
    urls = [f"{BASE_URL}?query={query}&display=20&start={1+(i*20)}" for i in range(10)]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
