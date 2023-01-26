import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
    current_url = driver.get("https://www.google.com")
    driver.maximize_window()

    #end text in searchbar
    element=WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.NAME,'q')))
    add_text= driver.find_element(By.NAME, 'q')
    add_text.send_keys('First Selenium Session')
    add_text.send_keys(Keys.RETURN)

def multipletabs():
    #open google.com
    current_url = driver.get("https://www.google.com")
    driver.maximize_window()
    driver.execute_script("window.open('about:blank', 'tab2');")

    driver.switch_to.window('tab2')
    tab2=driver.get("https://www.gmail.com")

    driver.execute_script("window.open('about:blank', 'tab3');")
    driver.switch_to.window('tab3')
    tab2 = driver.get("https://www.fb.com")

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[2])

    driver.close()
    driver.quit()

#setURL()
multipletabs()
























