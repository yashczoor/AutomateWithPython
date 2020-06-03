#! python3
#script to show explicit wait while navigating python doc
#selenium webdriver, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('http://www.python.org')

try: #if element is found within 10 seconds will close browser else throw error
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "start-shell"))
        )
finally:
    driver.quit()

