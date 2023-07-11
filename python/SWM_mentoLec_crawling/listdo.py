import os
import requests
import re
import time
import random

from dotenv import load_dotenv
from bs4 import BeautifulSoup

from request_bot import RequestBot
from message_bot import MessageBot
from logger import LoggerFactory


def get_total_contents(soup: BeautifulSoup) -> int:
    return int(soup.find_all("strong", class_="color-blue2")[0].get_text())


def get_content_info(soup: BeautifulSoup) -> list:
    lec_infos = soup.find("tbody").contents

    result = []
    for info in lec_infos:
        if info == "\n":
            continue

        lec_id = info.find_all("td")[0].get_text().strip().replace("\n", "")
        lec_title = info.find_all("div", class_="rel")[-1].find("a").get_text().strip().replace("\n", "")
        lec_link = info.find_all("div", class_="rel")[-1].find("a", href=True).get("href")
        lec_date = info.find_all("td")[3].get_text().strip().replace("\n", "")
        lec_date = re.sub(r"\s", "", lec_date).replace("&nbsp", " ")
        lec_mento = info.find_all("td")[6].get_text().strip().replace("\n", "")

        lec_dict = dict(
            id=lec_id,
            title=lec_title,
            link=lec_link,
            date=lec_date,
            mento=lec_mento,
        )
        result.append(lec_dict)

    return result


if __name__ == "__main__":
    # InsecureRequestWarning 메세지 없애기
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    # logging config
    LoggerFactory.create_logger()
    logging = LoggerFactory.get_logger()

    """
    프로젝트 최상단에 .env 파일 만들어서 설정하기
    """
    # 환경변수 설정
    load_dotenv()
    USERNAME = os.getenv("USERNAME")
    ENCRYPTED_PASSWORD = os.getenv("ENCRYPTED_PASSWORD")
    DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
    SLACK_TOKEN = os.getenv("SLACK_TOKEN")

    # 메세지 봇 객체 생성
    request_bot = RequestBot()
    message_bot = MessageBot(
        discord_webhook_url=DISCORD_WEBHOOK_URL,
        slack_token=SLACK_TOKEN,
    )

    # 매크로에 필요한 변수 설정
    total_contents = -1
    crawling_fail_count = 0
    while True:
        # 크롤링 과정에서 일정 횟수 이상 초과하면 더이상 크롤링을 하지 않습니다.
        if crawling_fail_count > 10:
            break

        # 크롤링은 1~5초 마다 한번씩 이루어집니다.
        time.sleep(random.randrange(1, 6))

        # 로그인을 시도합니다.
        for i in range(1, 6):
            try:
                jsessionid = request_bot.POST(
                    "https://swmaestro.org/sw/login.do",
                    payload={"username": USERNAME, "password": ENCRYPTED_PASSWORD},
                ).cookies.get("JSESSIONID")
                break
            except Exception as e:
                logging.warning(f"로그인 실패. 다시 시도합니다.(시도횟수 : {i})")
                logging.warning(e)
                time.sleep(random.randrange(1, 4))
                continue
        else:
            logging.error("로그인 실행횟수 초과!")
            break

        # 멘토링 페이지 정보를 가져옵니다.
        for i in range(1, 6):
            try:
                html_doc = request_bot.GET(
                    "https://swmaestro.org/sw/mypage/mentoLec/list.do?menuNo=200046",
                    cookie={"JSESSIONID": jsessionid},
                ).text
                break
            except ConnectionResetError as cre:
                logging.warning(f"ConnectionResetError. 다시 시도합니다.(시도횟수 : {i})")
                logging.warning(e)
                continue
            except ConnectionError as nce:
                logging.warning(f"NewConnectionError. 다시 시도합니다.(시도횟수 : {i})")
                logging.warning(e)
                continue
            except Exception as e:
                logging.warning(f"페이지 정보 불러오기 실패. 다시 시도합니다.(시도횟수 : {i})")
                logging.warning(e)
                continue
        else:
            crawling_fail_count += 1
            logging.warning(f"멘토링 페이지 불러오는 단계에서 페이지 정보를 불러올 수 없습니다. 처음부터 다시 시작합니다. (시도횟수 : {crawling_fail_count})")
            continue

        # 올바르게 로그인이 됐는지 확인합니다.
        login_fail_messages = [
            "로그인이 필요한 페이지입니다. 로그인페이지로 이동하시겠습니까?",
            "잘못된 접근입니다. 해당 세션을 전체 초기화 하였습니다.",
            "요청하신 페이지를 찾을수가 없습니다.",
        ]

        # html_doc 안에 login_fail_messages가 있으면 로그인이 필요한 페이지라고 판단합니다.
        if any([message in html_doc for message in login_fail_messages]):
            crawling_fail_count += 1
            logging.warning(f"멘토링 페이지 불러오는 단계에서 로그인 정보를 찾을 수 없습니다. 처음부터 다시 시작합니다. (시도횟수 : {crawling_fail_count})")
            continue

        # Parsing
        soup = BeautifulSoup(html_doc, "html.parser")
        soup = soup.find_all("div", class_="bbs-list")[-1]
        new_total_contents = get_total_contents(soup)

        # 처음 데이터를 불러온 상황
        if total_contents == -1:
            # 크롤링을 시작한다는 메세지 알림
            content = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]\n매크로를 시작합니다.\n현재 등록된 강의 개수는 {new_total_contents}개 입니다."
            logging.info(content)
            message_bot.discord_message(content)
        # 멘토링 강의가 추가된 상황 업데이트
        elif total_contents < new_total_contents:
            block = ""
            n = 5
            for idx, i in enumerate(get_content_info(soup), 1):
                block += f'{i.get("id")}. {i.get("date")} {i.get("mento")} <https://swmaestro.org/{i.get("link")}|{i.get("title")}>\n'
                if idx == n:
                    break

            content = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]\n새로운 강의 업데이트 알림! ({total_contents} -> {new_total_contents})\n\n<상위 {n if n < 10 else 10}개 강의 리스트>\n{block}\n\n전체보기: https://swmaestro.org/sw/mypage/mentoLec/list.do?menuNo=200046"
            logging.info(content)
            message_bot.slack_message("#98-mentoring-alert", content)
        # 멘토링 강의 변경 내역이 없거나 적어졌을 때는 아무것도 하지 않습니다.
        elif total_contents >= new_total_contents:
            pass

        # 다음 상황을 확인하기 위해서 총 개수를 업데이트 합니다.
        total_contents = new_total_contents

        # 크롤링 성공했으므로, crawling_fail_count를 초기화 합니다.
        crawling_fail_count = 0

    logging.error("에러 발생으로 매크로를 종료합니다.")
    message_bot.discord_message("[Error] 에러 발생으로 매크로를 종료합니다.")
