from selenium import webdriver
import time


browser = webdriver.Chrome(r"D:\workpractice\chromedriver.exe")
browser.maximize_window()

browser.get(r'https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle)  # 현재 윈도우 핸들 정보

# Try it your self
browser.find_element_by_xpath(r'//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles  # 모든 핸들 정보
for handle in handles:
    print(handle)
    browser.switch_to.window(handle)
    print(browser.title)  # 현재 핸들(브라우저)의 제목 표시

# 새로 이동된 브라우저에서 작업을 수행하고 그 브라우저를 종료
print("close handle")
browser.close()

# 이전 핸들로 돌아오기
print("switch to current handle")
browser.switch_to_window(curr_handle)
print(browser.title) # HTML input type="radio"

# 브라우저 컨트롤이 가능한 지 확인
time.sleep(1)
browser.get('http://www.daum.net')

time.sleep(3)
browser.quit()