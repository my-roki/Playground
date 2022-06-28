#%%
# chromedriver를 다운받아주세요!
from selenium import webdriver
browser = webdriver.Chrome(r'D:\workpractice\chromedriver.exe')  # chromedriver open

#%%
browser.get("http://www.naver.com")  # naver로 이동

#%%
elem = browser.find_element_by_link_text("카페")
elem
elem.get_attribute("href")
elem.get_attribute("class")

#%%
elem.click()

#%%
browser.back()

#%%
browser.forward()

#%%
browser.refresh()

#%%
elem = browser.find_element_by_id("query")
elem.send_keys("윤창록")

#%%
from selenium.webdriver.common.keys import Keys

elem.send_keys(Keys.ENTER)

#%%
elem = browser.find_element_by_tag_name("a")
elem.get_attribute("href")

#%%
elems = browser.find_elements_by_tag_name("a")
elems
#%%
for e in elems:
    e = e.get_attribute("href")
    print(e)

#%%
browser.get("http://daum.net")

#%%
elem = browser.find_element_by_name("q")

#%%
elem.send_keys("윤창록")

#%%
elem.send_keys("윤창록")

#%%
elem.clear()

#%%
elem.send_keys("윤창록")

#%%
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()

#%%
browser.save_screenshot('daum.png')

#%%
browser.page_source

#%%
browser.close()

#%%
browser.quit()

# https://selenium-python.readthedocs.io/locating-elements.html
# Selenium 공부에 도움되는 공식 사이트
