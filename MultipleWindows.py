from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH, "//*[@id='content']/div/a").click()
print("Current Window handle:", driver.current_window_handle)
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])

word = driver.find_element(By.XPATH, "/html/body/div/h3")
print(word.get_attribute("innerHTML"))