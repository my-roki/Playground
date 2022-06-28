"""
Quiz) Selenium 을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오.

1. https://www.w3schools.com 접속(URL은 구글에서 w3school 검색)
2. 화면 중간 LEARN HTML 클릭
3. 상단 메뉴 HOW TO 클릭
4. 좌측 메뉴 중 Contact Form 메뉴 클릭
5. 입력란에 아래 값 입력
    First Name : 창록
    Last Name : 윤
    Country : Canada
    Subject : 퀴즈를 완료하였습니다.
6. 5초 대기 후 Submit 버튼 클릭
7. 5초 대기 후 브라우저 종료
"""
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

# https://www.w3schools.com 접속
browser.get('https://www.w3schools.com')

# 화면 중간 LEARN HTML 클릭
browser.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/a[1]').click()

# 상단 메뉴 HOW TO 클릭
browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]').click()

# 좌측 메뉴 중 Contact Form 메뉴 클릭
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() 
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()
# browser.find_element_by_link_text('Contact Form').click()  # Contact Form 이라는 2개 이상의 링크 텍스트가 있는 경우 실패
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()  # 일부 텍스트 비교

# 입력란에 값 입력
first_name = "창록"
last_name = "윤"
country = "Canada"
subject = "퀴즈를 완료하였습니다."

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 5초 대기 후 Submit 버튼 클릭, 5초 대기 후 브라우저 종료
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()
