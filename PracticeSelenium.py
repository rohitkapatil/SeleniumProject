# FirstSelenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# print(driver.title)
# print(driver.current_url)
# driver.maximize_window()
# userName = driver.find_element(By.ID, "email")
# userName.send_keys("patilrohit215@gmail.com")
# passWord = driver.find_element(By.ID, "pass")
# passWord.send_keys("9403447172")
# driver.find_element(By.NAME, "login").click()
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span").click()
#
# # driver.back()
# # driver.forward()
# # driver.quit()

# ReadValues
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")
# textInput = driver.find_element(By.ID, "myTextInput2")
# print(textInput.get_attribute("value"))
# textInput.clear()
# textInput.send_keys("Rohit Patil")

# ConditionalElements
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")
# Drop1 = driver.find_element(By.ID, "drop1").is_displayed()
# print(Drop1)
#
# # if Drop1 == "False":
# checkBox = driver.find_element(By.ID, "checkBox1")
# print(checkBox.is_enabled())
# checkBox.click()

# ScrollingPage
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
# driver.execute_script("window.scrollBy(0,5000)")
# time.sleep(3)
# element = driver.find_element(By.ID, "Arithmetic_operations")
# driver.execute_script("arguments[0].scrollIntoView()", element)
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(3)
# driver.execute_script("window.scrollTo(0,0)")

# Alert
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button").click()
time.sleep(3)
driver.switch_to.alert.accept()