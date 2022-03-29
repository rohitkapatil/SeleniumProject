import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")


btnLogin = driver.find_element(By.XPATH, "//*[text() = 'Login']")
action = ActionChains(driver)
action.move_to_element(btnLogin).perform()
time.sleep(2)

loginCancel = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
loginCancel.click()
time.sleep(2)

btnLogin = driver.find_element(By.XPATH, "//*[text() = 'Login']")
action = ActionChains(driver)
action.move_to_element(btnLogin).perform()
time.sleep(2)

my_profile = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a")
my_profile.click()
time.sleep(2)

loginCancel = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
loginCancel.click()
time.sleep(2)

btnTravel = driver.find_element(By.XPATH, "//*[text() = 'Travel']")
# btnTravel = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[8]/a/div[2]")
btnTravel.click()
time.sleep(3)

# btnMobiles = driver.find_element(By.XPATH, "//*[text() = 'Mobiles']")
# btnMobiles.click()
# time.sleep(3)
#
# btnApple = driver.find_element(By.XPATH, "//*[text() = 'APPLE']")
# btnApple.click()
# time.sleep(3)

# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]").click()
# driver.current_window_handle

moreOption = driver.find_element(By.XPATH, "//*[text() = 'More']")
moreOption = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]")
action.move_to_element(moreOption).perform()

notificationOption = driver.find_element(By.XPATH, "//*[text()  = 'Notification Preferences']")
# action.move_to_element(moreOption).move_to_element(notificationOption).click().perform()
# time.sleep(2)
notificationOption.click()

