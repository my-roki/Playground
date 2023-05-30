import os
import requests

from dotenv import load_dotenv


class RequestBot:
    def __init__(self):
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        }
        self.timeout = 10
        self.verify = False

    def POST(self, url: str, payload: dict = {}, cookie: dict = {}) -> requests.Session:
        session = requests.Session()
        response = session.request(
            "POST",
            url,
            headers=self.headers,
            data=payload,
            cookies=cookie,
            timeout=self.timeout,
            verify=self.verify,
        )

        if response.status_code == 200:
            return session
        else:
            raise Exception("POST request failed.")

    def GET(self, url: str, payload: dict = {}, cookie: dict = {}) -> requests.Session:
        response = requests.request(
            "GET",
            url,
            headers=self.headers,
            data=payload,
            cookies=cookie,
            timeout=self.timeout,
            verify=self.verify,
        )
        if response.status_code == 200:
            return response
        else:
            raise Exception("GET request failed.")


if __name__ == "__main__":
    # 환경변수 설정
    load_dotenv()
    USERNAME = os.getenv("USERNAME")
    ENCRYPTED_PASSWORD = os.getenv("ENCRYPTED_PASSWORD")

    crawling_bot = RequestBot()

    jsessionid = crawling_bot.POST(
        "https://swmaestro.org/sw/login.do",
        payload={"username": USERNAME, "password": ENCRYPTED_PASSWORD},
    ).cookies.get("JSESSIONID")

    print(jsessionid)

    html_doc = crawling_bot.GET(
        "https://swmaestro.org/sw/mypage/mentoLec/list.do?menuNo=200046",
        cookie={"JSESSIONID": jsessionid},
    ).text

    print(html_doc)
