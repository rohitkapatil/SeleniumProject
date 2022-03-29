from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")
# element = driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th[1]")
# print(element.text)

# for col in range(1, 4):
#     element = driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th[" + str(col) + "]")
#     print(element.text, end=" ")

for row in range(2, 7):
    for col in range(1, 4):
        element = driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th[" + str(col) + "]")
        element1 = driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[" + str(row) + "]/td[" + str(col) + "]")
        print(element.text, end=" ")
        print(element1.text)

# //*[@id="customers"]/tbody/tr[1]/th[2]
# //*[@id="customers"]/tbody/tr[3]/td[1]
# //*[@id="customers"]/tbody/tr[2]/td[1]
