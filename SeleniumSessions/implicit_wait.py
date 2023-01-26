from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def setURL():

    # get google.com
    current_url = driver.get("https://www.google.com")
    driver.maximize_window()

def search_google():

    driver.implicitly_wait(5)

    # end text in searchbar
    add_text = driver.find_element(By.NAME, 'q')
    add_text.send_keys('First Selenium Session')
    add_text.send_keys(Keys.RETURN)
    print('Search successfully')

setURL()
search_google()
























