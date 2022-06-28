from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



browser = webdriver.Chrome(r"D:\workpractice\chromedriver.exe")
browser.maximize_window()

browser.get(r'https://flight.naver.com/flights/')

# 가는 날 클릭
browser.find_element_by_link_text('가는날 선택').click()
time.sleep(1)
browser.find_elements_by_link_text('30')[0].click()
time.sleep(1)

# 오는 날 클릭
# browser.find_element_by_link_text('오는날 선택').click()
# time.sleep(1)
browser.find_elements_by_link_text('5')[1].click()
time.sleep(1)

# 제주도 클릭
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()
time.sleep(1)

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()
time.sleep(1)

# # 첫 번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
except:
    print("failed")

time.sleep(3)
browser.quit()