import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.back()
driver.forward()
# driver.close()

InputUser = driver.find_element(By.ID, "email")
InputUser.send_keys("patilrohit215@gmail.com")
InputPass = driver.find_element(By.ID, "pass")
InputPass.send_keys("9403447172")
btnLogin = driver.find_element(By.NAME, "login")
btnLogin.click()

driver.find_element(By.XPATH, "//div[@aria-label='Menu']").click()
a = driver.current_window_handle
time.sleep(3)

# Account1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span")
Account1 = driver.find_element(By.XPATH, "//div[@aria-label='Account']//*[name()='svg']")
Account1.click()
time.sleep(4)

# btnLogout2 = [driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div/div[1]"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div/div[1]/div[1]"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div/div[1]/div[1]/div"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div/div[1]/div[1]"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div/div[1]/div[2]"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div/div[1]/div[2]/div"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div/div[1]/div[2]/div/div/div/div"),
#               driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[1]/div["
#                                             "1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div["
#                                             "4]/div/div[1]/div[2]/div/div/div/div/span")]
#
# for buTTon in btnLogout2:
#     buTTon.click()
#     break
profile = driver.find_element(By.XPATH, "//*[text()='Rohit Patil']")
profile.click()

time.sleep(6)
Account1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span")
Account1.click()

btnLogout = driver.find_element(By.XPATH, "//*[text() ='Log Out']")
btnLogout.click()
