import os
import requests
from dotenv import load_dotenv


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


if __name__ == "__main__":
    """
    프로젝트 최상단에 .env 파일 만들어서 설정하기
    """
    load_dotenv()  
    USERNAME = os.getenv("USERNAME")
    ENCRYPTED_PASSWORD = os.getenv("ENCRYPTED_PASSWORD")

    jsessionid = get_jsessionid(USERNAME, ENCRYPTED_PASSWORD)
    print(get_content(jsessionid))

    """ TODO
    - bs로 현재 개수 가져오기
        - 최초 시도시 개수 저장 후 이후 작업마다 비교해서 개수가 달라지면 알림을 줌
        - No가 존재하니 이걸 기준으로 업데이트 현황을 알 수 있지 않을까?
    - 텔레그램봇 연결해서 업데이트 될 때마다 알림오게 하기
    - 변수들 env로 뺄 수 있으면 빼기
    - 요청은 밴을 방지하기 위해 랜덤하게 설정하기
    """
