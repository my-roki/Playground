import time
from selenium import webdriver

browser = webdriver.Chrome(r'chromedriver.exe')
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')  # 프레임 전환

elem = browser.find_element_by_xpath('//*[@id="age1"]')  # 클릭 성공
elem.click()

browser.switch_to_default_content()  # 상위로 빠져나옴

elem = browser.find_element_by_xpath('//*[@id="age1"]')  # 클릭 실패
elem.click()
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="age1"]"}

time.sleep(5)
browser.quit()
