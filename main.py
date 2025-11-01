import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
assert  "Python" in driver.title

elem = driver.find_element(By.NAME, 'q')
elem.clear()
elem.send_keys('pycondrjrfn')
elem.send_keys(Keys.RETURN)
assert "No Results are Found" not in driver.page_source
time.sleep(6)

driver.close