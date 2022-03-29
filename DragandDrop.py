import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
action = ActionChains(driver)


# Drop1 = driver.find_element(By.ID, "box1")
# Drop2 = driver.find_element(By.ID, "box101")
# action.drag_and_drop(Drop1, Drop2).perform()
# time.sleep(3)
#
# Drop1a = driver.find_element(By.ID, "box2")
# Drop2a = driver.find_element(By.ID, "box102")
# action.drag_and_drop(Drop1a, Drop2a).perform()
#
# Drop1b = driver.find_element(By.ID, "box3")
# Drop2b = driver.find_element(By.ID, "box103")
# action.drag_and_drop(Drop1b, Drop2b).perform()
#
# Drop1c = driver.find_element(By.ID, "box4")
# Drop2c = driver.find_element(By.ID, "box104")
# action.drag_and_drop(Drop1c, Drop2c).perform()
#
# Drop1d = driver.find_element(By.ID, "box5")
# Drop2d = driver.find_element(By.ID, "box105")
# action.drag_and_drop(Drop1d, Drop2d).perform()
#
# Drop1e = driver.find_element(By.ID, "box6")
# Drop2e = driver.find_element(By.ID, "box106")
# action.drag_and_drop(Drop1e,Drop2e).perform()
#
# Drop1f = driver.find_element(By.ID, "box7")
# Drop2f = driver.find_element(By.ID, "box107")
# action.drag_and_drop(Drop1f, Drop2f).perform()

for n in range(1, 8):
    Drop1 = driver.find_element(By.ID, "box"+str(n)+"")
    Drop2 = driver.find_element(By.ID, "box10"+str(n)+"")
    action.drag_and_drop(Drop1, Drop2).perform()
