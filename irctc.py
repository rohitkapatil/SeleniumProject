import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")

popUp = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div["
                                      "2]/div/form/div[2]/button")

popUp.click()

dateButton = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div["
                                           "1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div["
                                           "1]/p-calendar/span/input")
dateButton.click()

dateElement = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div["
                                            "1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div["
                                            "1]/p-calendar/span/div/div/div[2]/table/tbody/tr[3]/td[2]/a")
dateElement.click()

element = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div["
                                        "1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[2]/p-dropdown/div")
# dropdown = Select(element)
time.sleep(3)
# dropdown.select_by_visible_text("All Classes")
element.click()

# time.sleep(3)
AcElement = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div["
                                          "1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[2]/p-dropdown/div/div["
                                          "4]/div/ul/p-dropdownitem[3]/li/span")

AcElement.click()

btnFlexible = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div["
                                            "1]/div[1]/app-jp-input/div/form/div[4]/div/span[2]/label")

btnFlexible.click()
