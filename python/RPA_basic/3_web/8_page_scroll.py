from selenium import webdriver
import time

browser = webdriver.Chrome(r"D:\workpractice\chromedriver.exe")
browser.maximize_window()

browser.get(r"https://shopping.naver.com/")

# 무선마우스 입력 및 검색버튼 클릭
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys("무선마우스")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# 스크롤
# 지정한 위치로 스크롤을 내리는 방법
# 모니터 (해상도) 높이인 1080 위치로 스크롤 내리기
browser.execute_script('window.scrollTo(0,1080)')
time.sleep(1)
browser.execute_script('window.scrollTo(0,2080)')

# 화면 가장 아래로 내리는 방법
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에 대해서 맨 마지막까지 계속 내리기
interval = 1 

# 현재 문서의 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복수행
while True:
    # 스크롤을 화면 가장 아래로 내립니다
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 (interval 초)
    time.sleep(interval)

    # 현재 문서 높이를 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:  # 직전 높이와 같으면(높이 변화가 없으면)
        break  # 반복문 탈출(모든 스크롤 동작 완료)

    prev_height = curr_height

# 맨 위로 올리기
time.sleep(1)
browser.execute_script('window.scrollTo(0,0)')

time.sleep(3)
browser.quit()