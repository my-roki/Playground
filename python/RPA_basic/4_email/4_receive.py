from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# limit : 최대 메일 개수
# reverse : 최근 메일 부터(True)/과거 메일부터(False)
for msg in mailbox.fetch(limit=1, reverse=True):
    print({
        "subject" : msg.subject,
        "form": msg.from_,
        "to":msg.to,
        "cc":msg.cc,
        "bcc":msg.bcc,
        "date":msg.date,
        "text":msg.text,
        "html":msg.html})
    print("="*100)

    # 첨부파일
    for att in msg.attachments:
        print({
            "filename":att.filename,
            "type":att.content_type,
            "size":att.size})

        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print(f"참부파일 {att.filename} 다운로드 완료")

mailbox.logout()

