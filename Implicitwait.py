import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.find_element(By.XPATH, "//*[@id='start']/button").click()
# time.sleep(10)
driver.implicitly_wait(120)
element = driver.find_element(By.XPATH, "//*[@id='finish']/h4")
print(element.get_attribute("innerHTML"))
