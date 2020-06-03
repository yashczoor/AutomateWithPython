#!python3
#implicit wait - pauses for amount of time for every action. Case e.g. slow internet connection
#selenium webdriver

from selenium import webdriver

driver = webdriver.Firefox()

driver.implicitly_wait(10) #will wait 10 sec on every action

driver.get('http://www.python.org')
myDynamicElement = driver.find_element_by_id('start-shell')
myDynamicElement = driver.find_element_by_id('there is no such element')
driver.close()
