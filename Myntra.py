import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")
action = ActionChains(driver)
Men = driver.find_element(By.XPATH, "//a[@class='desktop-main'][normalize-space()='Men']")
action.move_to_element(Men).perform()
MenTShirt = driver.find_element(By.XPATH, "//a[@href='/men-tshirts']")
MenTShirt.click()
driver.current_window_handle
Tshirt = driver.find_element(By.XPATH, "//div[contains(@class,'slick-slide slick-active "
                                       "slick-center')]//div//div//img[contains(@title,'White Pure Cotton Printed "
                                       "Polo Collar Pure Cotton T-shirt')]")
action.move_to_element(Tshirt).click().perform()
handel = driver.window_handles
driver.switch_to.window(handel)
