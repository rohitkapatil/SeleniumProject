import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
searchDropdown = driver.find_element(By.ID, "searchDropdownBox")
searchDropdown.click()
option = driver.find_element(By.XPATH, "//option[@value='search-alias=electronics']")
option.click()
time.sleep(3)
tabSearch = driver.find_element(By.ID, "twotabsearchtextbox")
tabSearch.send_keys("Redmi Note 11")
searchIcon = driver.find_element(By.ID, "nav-search-submit-button")
searchIcon.click()

# dropDown = Select(searchDropdown)
# dropDown.select_by_visible_text("Electronics")
