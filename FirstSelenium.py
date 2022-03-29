from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.back()
driver.forward()
# driver.close()
inputUsername = driver.find_element(By.ID, "email")
inputUsername.send_keys("patilrohit215@gmail.com")
inputPass = driver.find_element(By.ID, "pass")
inputPass.send_keys("9403447172")
btnLogin = driver.find_element(By.NAME, "login")
btnLogin.click()
#
# btnLogout = driver.find_element(By.LINK_TEXT, "Log Out")
# btnLogout.click()
