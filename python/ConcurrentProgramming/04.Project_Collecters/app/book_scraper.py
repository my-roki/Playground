import asyncio
from concurrent.futures import ALL_COMPLETED
import aiohttp

from app.config import NAVER_API_ID, NAVER_API_SECRET


class NaverBookScraper:
    def unit_url(self, keyword, start):
        return {
            "url": f"https://openapi.naver.com/v1/search/book.json?query={keyword}&display=10&start={start}",
            "headers": {
                "X-Naver-Client-Id": NAVER_API_ID,
                "X-Naver-Client-Secret": NAVER_API_SECRET,
            },
        }

    @staticmethod
    async def fetch(session, url, headers):
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                items = result.get("items")
                return items

    async def search(self, keyword, total_page):
        apis = [self.unit_url(keyword, 1 + (i * 10)) for i in range(total_page)]
        async with aiohttp.ClientSession() as session:
            all_data = await asyncio.gather(
                *[
                    NaverBookScraper.fetch(session, api.get("url"), api.get("headers"))
                    for api in apis
                ]
            )
            result = list()
            for data in all_data:
                if data is not None:
                    result += data

            return result

    # run test
    def run(self, keyword, total_page):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        return asyncio.run(self.search(keyword, total_page))


if __name__ == "__main__":
    pass
    # scraper = NaverBookScraper()
    # a = scraper.run("비트코인", 1)

    # for i in a:
    #     print(i)
    # print(len(a))
