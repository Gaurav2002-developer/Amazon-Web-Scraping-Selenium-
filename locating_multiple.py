import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = 'speakers'
for i in range(1,4):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&xpid=YHRwq8TLrgFEx&crid=Q5869GOL6SVW&qid=1761952561&sprefix=speaker%2Caps%2C236&ref=sr_pg_2")

    elems = driver.find_elements(By.CLASS_NAME, 'puis-desktop-list-row')
    print(f"{len(elems)} found in list")
    print(elems)
    for elem in elems:
        
        print(elem.text)
    # print(elem.get_attribute('outerHTML'))
    # print(elem.text)
    time.sleep(3)
    driver.close