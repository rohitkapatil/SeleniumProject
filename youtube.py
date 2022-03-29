import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()

btnSearch = driver.find_element(By.NAME, "search_query")
btnSearch.click()
btnSearch.send_keys(" Srivalli hindi song")
driver.find_element(By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button").click()
a = driver.current_window_handle
time.sleep(3)

action = ActionChains(driver)
playSong = driver.find_element(By.XPATH, "//body/ytd-app/div[@id='content']/ytd-page-manager["
                                         "@id='page-manager']/ytd-search[@role='main']/div["
                                         "@id='container']/ytd-two-column-search-results-renderer[@class='style-scope "
                                         "ytd-search']/div[@id='primary']/ytd-section-list-renderer["
                                         "@class='style-scope ytd-two-column-search-results-renderer']/div["
                                         "@id='contents']/ytd-item-section-renderer[@class='style-scope "
                                         "ytd-section-list-renderer']/div[@id='contents']/ytd-video-renderer[1]/div["
                                         "1]/ytd-thumbnail[1]/a[1]/yt-img-shadow[1]/img[1]")
action.move_to_element(playSong).click().perform()
