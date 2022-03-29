from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/download")
driver.find_element(By.LINK_TEXT, "download.jpg").click()