import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = 'laptop'
driver.get(f"https://www.amazon.in/s?k={query}&crid=2TW1IGLRI7Y5B&sprefix=laptop%2Caps%2C238&ref=nb_sb_noss_2")

elem = driver.find_element(By.CLASS_NAME, 'puis-desktop-list-row')
print(elem.get_attribute('outerHTML'))
time.sleep(6)
driver.close