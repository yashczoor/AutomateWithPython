from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click() #follows Read it online link
