#!python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) #scrolls to bottom
time.sleep(2)
htmlElem.send_keys(Keys.HOME) #scrolls to top

