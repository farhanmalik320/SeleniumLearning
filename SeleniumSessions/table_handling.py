import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

def setURL():
    current_url = driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    #driver.execute_script("document.body.style.zoom='75%'")

def tablehandling():

    tablefirstrow= driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/fieldset[1]/table[1]/tbody[1]/tr[1]").text
    print(tablefirstrow)

    tablesecondrow=driver.find_element(By.XPATH,'/html[1]/body[1]/div[3]/div[1]/fieldset[1]/table[1]/tbody[1]/tr[2]').text
    print(tablesecondrow)

    totalrows= driver.find_elements(By.XPATH, '/html[1]/body[1]/div[3]/div[1]/fieldset[1]/table[1]/tbody[1]/tr')
    print(len(totalrows))

    totalcol=driver.find_elements(By.XPATH,'//body[1]/div[3]/div[1]/fieldset[1]/table[1]/tbody[1]/tr[2]/td')
    print(len(totalcol))

def mousehover():

    element_to_hover_over = driver.find_element(By.ID, "mousehover")

    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()

    driver.find_element(By.XPATH,"//a[contains(text(),'Reload')]").click()

setURL()
#tablehandling()
mousehover()
























