import time
from selenium import webdriver

browser = webdriver.Chrome(r'chromedriver.exe')
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
browser.maximize_window()  # 창 최대화

time.sleep(3)

browser.switch_to.frame('iframeResult')  # 프레임 전환
elem = browser.find_element_by_xpath('//*[@id="age1"]')  # 클릭 성공

# 선택이 안 되어 있으면 선택하기
if elem.is_selected() == False:  # 라디오 버튼이 선택되어 있지 않으면
    print("라디오 버튼이 선택되어 있지 않으므로 선택합니다.")
    elem.click()
else:
    print("라디오 버튼이 선택되어 있으므로 아무것도 하지 않습니다.")

time.sleep(5)

if elem.is_selected() == False:  # 라디오 버튼이 선택되어 있지 않으면
    print("라디오 버튼이 선택되어 있지 않으므로 선택합니다.")
    elem.click()
else:
    print("라디오 버튼이 선택되어 있으므로 아무것도 하지 않습니다.")

browser.quit()
