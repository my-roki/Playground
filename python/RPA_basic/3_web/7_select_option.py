from selenium import webdriver
import time

browser = webdriver.Chrome(r'chromedriver.exe')
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
browser.maximize_window()  # 창 최대화
browser.switch_to.frame('iframeResult')  # 프레임 전환

time.sleep(3)

# cars에 해당하는 element를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
elem.click()

# 텍스트 값을 통해서 선택하는 방법
time.sleep(3)
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Saab"]')
elem.click()

# 텍스트 값이 부분일치 하는 항목 선택하는 방법
time.sleep(3)
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Op")]')
elem.click()

time.sleep(3)
browser.quit()



