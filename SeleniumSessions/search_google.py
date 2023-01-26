import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

#s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# create webdriver object
#driver = webdriver.Chrome(service=s)

# get google.com
current_url = driver.get("https://www.google.com")
driver.maximize_window()

#end text in searchbar
add_text= driver.find_element(By.NAME, 'q')
add_text.send_keys('First Selenium Session')
add_text.send_keys(Keys.RETURN)
print('Search successfully')
driver.close()


