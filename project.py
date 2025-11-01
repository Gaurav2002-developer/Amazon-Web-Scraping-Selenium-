import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = 'speakers'
file = 0
for i in range(1,4):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&xpid=YHRwq8TLrgFEx&crid=Q5869GOL6SVW&qid=1761952561&sprefix=speaker%2Caps%2C236&ref=sr_pg_2")

    elems = driver.find_elements(By.CLASS_NAME, 'puis-desktop-list-row')
    print(f"{len(elems)} found in list")

    for elem in elems:
        
        d = elem.get_attribute('outerHTML')
        with open(f"data/{query}_{file}.html" , 'w', encoding= 'utf-8') as f:
            f.write(d)
        file += 1

    # print(elem.text)
time.sleep(3)
driver.close