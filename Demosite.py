import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")
# time.sleep(3)

# inputText = driver.find_element(By.ID, "myTextInput")
# inputText.send_keys("Rohit Patil")
# # time.sleep(3)
#
# inputTextarea = driver.find_element(By.ID, "myTextarea")
# inputTextarea.send_keys("787, Plot No 10,B Ward,Ramanand Nagar,Kolhapur-416007")
# # time.sleep(3)
#
# getText = driver.find_element(By.NAME, "preText2")
# print(getText.get_attribute("value"))
# getText.send_keys("ABCD")
# time.sleep(3)
#
# btnColor = driver.find_element(By.ID, "myButton")
# btnColor.click()
# # time.sleep(3)
#
# placeHolder = driver.find_element(By.ID, "placeholderText")
# print(placeHolder.is_displayed())
# placeHolder.send_keys("Hi Rohit")
#
# element = driver.find_element(By.ID, "mySelect")
# dropdown = Select(element)
# time.sleep(3)
# dropdown.select_by_index(2)
# time.sleep(3)
# dropdown.select_by_value("25%")
# time.sleep(3)
# dropdown.select_by_visible_text("Set to 100%")

# dropdown.options
# all_options = dropdown.options
# print(all_options)
#
# for option in all_options:
#     print(option.text)
#     print(option.get_attribute("innerHTML"))
#     print(option.get_attribute('value'))

# elements = driver.find_elements(By.TAG_NAME, "a")
# for element in elements:
#     print(element.text)

# elements = driver.find_element(By.XPATH, '//*[@id="myLink2"]')
# elements.click()

elements = driver.find_element(By.PARTIAL_LINK_TEXT, ".io")
elements.click()



# for element in elements:
#     print(element.text)



