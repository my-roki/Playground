import os
import requests
import re
import time
import random
from dotenv import load_dotenv
from bs4 import BeautifulSoup


def get_jsessionid(username: str, encrypted_password: str) -> str:
    session = requests.Session()  # 쿠키에 있는 JSESSIONID를 가져오기 위함
    url = "https://swmaestro.org/sw/login.do"
    payload = {
        "username": username,
        "password": encrypted_password,
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }

    response = session.request(
        "POST",
        url,
        headers=headers,
        data=payload,
        timeout=5,
        verify=False,
    )

    if response.status_code == 200:
        return session.cookies.get_dict().get("JSESSIONID")
    else:
        raise ValueError("JSESSIONID not found.")


def get_content(jsessionid: str) -> str:
    url = "https://swmaestro.org/sw/mypage/mentoLec/list.do?menuNo=200046"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }
    cookie = {
        "JSESSIONID": jsessionid,
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        timeout=5,
        verify=False,
        cookies=cookie,
    )

    if response.status_code != 200:
        raise Exception("There was a problem loading the mentoLec page.")

    return response.text


def get_total_lec(soup: BeautifulSoup) -> int:
    return int(soup.find_all("strong", class_="color-blue2")[0].get_text())


def get_lec_info(soup: BeautifulSoup) -> list:
    lec_infos = soup.find("tbody").contents

    result = []
    for info in lec_infos:
        if info == "\n":
            continue

        lec_id = info.find_all("td")[0].get_text().strip().replace("\n", "")
        lec_tit = info.find_all("div", class_="rel")[-1].find("a").get_text().strip().replace("\n", "")
        lec_date = info.find_all("td")[3].get_text().strip().replace("\n", "")
        lec_date = re.sub(r"\s", "", lec_date).replace("&nbsp", " ")
        lec_mento = info.find_all("td")[6].get_text().strip().replace("\n", "")

        lec_dict = dict(
            id=lec_id,
            title=lec_tit,
            date=lec_date,
            mento=lec_mento,
        )
        result.append(lec_dict)

    return result


def discord_webhook(DISCORD_WEBHOOK_URL: str, content: str):
    message = {"content": content}
    requests.post(DISCORD_WEBHOOK_URL, data=message)


if __name__ == "__main__":
    # InsecureRequestWarning 메세지 없애기
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    """
    프로젝트 최상단에 .env 파일 만들어서 설정하기
    """
    # 환경변수 설정
    load_dotenv()
    USERNAME = os.getenv("USERNAME")
    ENCRYPTED_PASSWORD = os.getenv("ENCRYPTED_PASSWORD")
    DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

    # 매크로에 필요한 변수 설정
    total_contents = -1
    login_cnt = 0
    while True:
        try:
            # 요청은 밴을 방지하기 위해 랜덤하게 설정하기
            time.sleep(random.randrange(3, 11))

            # 처음 시작할 때 로그인을 시도합니다.
            if total_contents == -1:
                jsessionid = get_jsessionid(USERNAME, ENCRYPTED_PASSWORD)
                login_cnt = 0

            # 10번 로그인 시도해도 안 되면 로그인에 문제가 생겼다고 판단하고 중단
            if login_cnt > 10:
                discord_webhook(DISCORD_WEBHOOK_URL, "로그인 설정에 문제가 생겼습니다.")
                raise Exception("로그인 설정에 문제가 생겼습니다.")

            # 멘토링 페이지 정보를 가져옵니다.
            html_doc = get_content(jsessionid)
            if "로그인이 필요한 페이지입니다. 로그인페이지로 이동하시겠습니까?" in html_doc:
                login_cnt += 1
                print(f"[info] 로그인 실패. 로그인을 다시 시도합니다.(시도횟수 : {login_cnt})")
                continue

            # Parsing
            soup = BeautifulSoup(html_doc, "html.parser")
            new_total_lec = get_total_lec(soup)

            # 처음 데이터를 불러온 상황
            if total_contents == -1:
                # 크롤링을 시작한다는 메세지 알림
                content = f"""
                [{time.strftime('%Y-%m-%d %H:%M:%S')}]\n매크로를 시작합니다.\n현재 등록된 강의 개수는 {new_total_lec}개 입니다.
                """
                discord_webhook(DISCORD_WEBHOOK_URL, content)
            # 멘토링 강의가 추가된 상황 업데이트
            elif total_contents < new_total_lec:
                l = get_lec_info(soup)
                block = ""
                for i in l:
                    tmp = f'{i.get("id"), i.get("title"), i.get("date"), i.get("mento")}\n'
                    block += tmp

                content = f"""
                [{time.strftime('%Y-%m-%d %H:%M:%S')}]\n새로운 강의 업데이트 알림!({total_contents} -> {new_total_lec})\n\n상위 10개 강의 리스트\n{block}
                """
                discord_webhook(DISCORD_WEBHOOK_URL, content)
            # 멘토링 강의 변경 내역이 없거나 적어졌을 때는 아무것도 하지 않습니다.
            elif total_contents >= new_total_lec:
                pass

            # 다음 상황을 확인하기 위해서 총 개수를 업데이트 합니다.
            total_contents = new_total_lec
        except Exception as e:
            content = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]\n에러 발생 \n ```\n{e}\n```"
            discord_webhook(DISCORD_WEBHOOK_URL, content)
            break

    print("[Error] 에러 발생으로 매크로를 종료합니다.")
    discord_webhook(DISCORD_WEBHOOK_URL, "[Error] 에러 발생으로 매크로를 종료합니다.")
