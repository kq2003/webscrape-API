from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

path = '/Users/tonyqin/Downloads/chromedriver'
browser = webdriver.Chrome(executable_path=path)
link = 'https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/8618/Stages/19793/PlayerStatistics/England-Premier-League-2021-2022'
browser.get(link)


def print_elements():
    search = browser.find_element_by_id('statistics-table-summary')
    print(search.text)


def click_next():
    lynk = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#next"))
    )
    lynk.click()


print_elements()
time.sleep(5)
click_next()
time.sleep(5)
print_elements()




