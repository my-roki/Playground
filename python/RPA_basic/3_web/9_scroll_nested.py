from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome(r"D:\workpractice\chromedriver.exe")
browser.maximize_window()

browser.get(r'https://www.w3schools.com/html/default.asp')

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[37]')
time.sleep(1)

# # 방법1. ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# # 방법2
# xy = elem.location_once_scrolled_into_view  # 함수가 아니니까 ()를 쓰지 않습니다.
# print("type : ", type(xy))
# print(" value : ", xy)
# elem.click()

# 실제로 xPath를 알면 스크롤을 내리지 않아도 클릭하는덴 문제 없음
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[37]')
elem.click()

time.sleep(3)
browser.quit()