import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

a = driver.find_element(By.ID, "myDropdown")
b = driver.find_element(By.ID, "dropOption2")
action = ActionChains(driver)
action.move_to_element(a).move_to_element(b).click().perform()
time.sleep(3)
action.double_click(driver.find_element(By.ID, "myButton")).perform()
action.context_click(driver.find_element(By.ID, "svgRect")).perform()