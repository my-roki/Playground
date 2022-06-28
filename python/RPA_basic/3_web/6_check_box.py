import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(r'chromedriver.exe')
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')
browser.maximize_window()  # 창 최대화
browser.switch_to.frame('iframeResult')  # 프레임 전환

# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
elem = browser.find_element(By.XPATH,'//*[@id="vehicle1"]')

time.sleep(5)
if elem.is_selected() == False:  # 라디오 버튼이 선택되어 있지 않으면
    print("체크박스가 선택되어 있지 않으므로 선택합니다.")
    elem.click()
else:
    print("체크박스가 선택되어 있으므로 아무것도 하지 않습니다.")

browser.quit()

