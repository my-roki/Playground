from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADRESS, EMAIL_PASSWORD, initial_folder="INBOX")

with MailBox("imap.gmail.com", 993).login(EMAIL_ADRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
# https://pypi.org/project/imap-tools/ 참고..

    # for msg in mailbox.fetch(limit=5, reverse=True):  
    #     print(f'[{msg.from_}] {msg.subject}')

    # for msg in mailbox.fetch('(UNSEEN)'):  # 읽지 않은 메일 가져오기
    #     print(f'[{msg.from_}] {msg.subject}')

    # for msg in mailbox.fetch('(FROM dbsckdfhr123@gmail.com)'):  # 특정인이 보낸 메일 불러오기
    #     print(f'[{msg.from_}] {msg.subject}')

    # for msg in mailbox.fetch('(TEXT "20200401")'):  # 특정 글자가 포함된 메일 불러오기
    #     print(f'[{msg.from_}] {msg.subject}')

    # for msg in mailbox.fetch('(SUBJECT "20200401")'): # 특정 글자가 포함된 메일 불러오기(제목만)
    #     print(f'[{msg.from_}] {msg.subject}')
    
    # # imap에서 한글은 인식을 못 하기 때문에 아래와 같은 우회 방법으로 한글 텍스트를 search합니다.
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print(f'[{msg.from_}] {msg.subject}')

    # for msg in mailbox.fetch('(SENTSINCE 01-Jan-2021)', reverse=True, limit=10):  # 특정 날짜 이후의 메일 불러오기
    #     print(f'[{msg.from_}] {msg.subject}')  

    # for msg in mailbox.fetch('(ON 13-Apr-2021)', reverse=True):  # 특정 날짜에 온 메일
    #     print(f'[{msg.from_}] {msg.subject}')  

    # for msg in mailbox.fetch('(ON 13-Apr-2021 SUBJECT "100")', reverse=True):  # 두개 이상의 조건을 모두 만족하는 메일
    #     print(f'[{msg.from_}] {msg.subject}')  

    for msg in mailbox.fetch('(OR ON 13-Apr-2021 SUBJECT "100")', reverse=True):  # 두개 이상의 조건을 모두 만족하는 메일
        print(f'[{msg.from_}] {msg.subject}')  






