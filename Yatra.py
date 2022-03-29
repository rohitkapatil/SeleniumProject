import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.yatra.com/")
departCity = driver.find_element(By.ID, "BE_flight_origin_city")
departCity.click()
action = ActionChains(driver)
selectCity = driver.find_element(By.XPATH, "//div[@class='oneway-roundtrip CitySwap']//li[2]//div[1]//p[1]")
action.move_to_element(selectCity).click().perform()
time.sleep(3)
goingCity = driver.find_element(By.ID, "BE_flight_arrival_city")
goingCity.click()
selectGoingCity = driver.find_element(By.XPATH, "//*[text()='Bangalore ']")
action.move_to_element(selectGoingCity).click().perform()
time.sleep(3)
swapCity = driver.find_element(By.XPATH, "//a[@class='beSwapCity']")
swapCity.click()
time.sleep(3)
openGermany = driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/travel-guidelines/international/germany"
                                            "']//div[@class='imgRes']//img")
action.move_to_element(openGermany).click().perform()
driver.current_window_handle