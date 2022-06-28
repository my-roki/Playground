import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'D:\workpractice\RPA_basic\3_web'})

browser = webdriver.Chrome(r"D:\workpractice\chromedriver.exe", options=chrome_options)
browser.maximize_window()

browser.get(r'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame(r'iframeResult')

elem = browser.find_element_by_xpath(r'/html/body/p[2]/a')
elem.click()

time.sleep(3)
browser.quit()