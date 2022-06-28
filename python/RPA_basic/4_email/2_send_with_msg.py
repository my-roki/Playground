import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "테스트 메일입니다."  # 제목
msg["From"] = EMAIL_ADRESS  # 보내는 사람
msg["To"] = "anthony.yoon@testworks.co.kr"  # 받는 사람
msg["Cc"] = "anthony.yoon@testworks.co.kr"  # 참조
msg["Bcc"] = "anthony.yoon@testworks.co.kr"  # 숨은참조
msg.set_content("테스트 본문입니다.")  # 본문

# 여러명에게 보내고 싶을 때
msg["To"] = "anthony.yoon@testworks.co.kr, anthony.yoon@testworks.co.kr"
to_list = ["anthony.yoon@testworks.co.kr", "anthony.yoon@testworks.co.kr"]
msg["To"] = ",".join(to_list)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Done")
 















