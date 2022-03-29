import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH, "/html/body/button").click()
time.sleep(3)
driver.switch_to.alert.accept()
