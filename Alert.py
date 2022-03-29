import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# alterElement = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button")
# alterElement.click()
# time.sleep(4)
#
# # driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

alertConfirm = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
alertConfirm.click()
time.sleep(4)
driver.switch_to.alert.accept()

