from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://gmail.com')

inputMail = browser.find_element_by_id('Email')
inputMail.send_keys('your@gmail.com')
inputPassword = browser.find_element_by_id('Passwd')
inputPassword.send_keys('*****')
inputPassword.submit()

