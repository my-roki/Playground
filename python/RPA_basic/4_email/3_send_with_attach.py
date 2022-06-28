import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "테스트 메일입니다."  # 제목
msg["From"] = EMAIL_ADRESS  # 보내는 사람
msg["To"] = "anthony.yoon@testworks.co.kr"  # 받는 사람
# msg["Cc"] = "anthony.yoon@testworks.co.kr"  # 참조
# msg["Bcc"] = "anthony.yoon@testworks.co.kr"  # 숨은참조
msg.set_content("첨부파일 테스트입니다.")  # 본문

# msg.add_attachment

d_image = r'D:\workpractice\RPA_basic\3_web\daum.png'
with open(d_image, 'rb') as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name.split("\\")[-1])  
# mime type : https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
# print(f.name.split("\\")[-1])

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Done")