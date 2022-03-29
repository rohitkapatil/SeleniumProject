import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

for n in range(25000):
    driver.execute_script(f"window.scrollBy(0,{n})", "")
    time.sleep(0.5)

# element = driver.find_element(By.ID, "Development_environments")
# driver.execute_script("arguments[0].scrollIntoView()", element)
#
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
# driver.execute_script("window.scrollTo(0,0)", "")