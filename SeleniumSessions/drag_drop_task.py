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
    current_url = driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-1.html")
    driver.maximize_window()
    #driver.execute_script("document.body.style.zoom='75%'")

def draganddrop():

    driver.find_element(By.XPATH,"//div[@id='mainContainer']").click()

    name= driver.find_element(By.XPATH, "//h2[contains(text(),'Drag and drop - demo 1')]")
    print(name.text)

    dropbox = driver.find_element(By.XPATH, "//div[@id='dropBox']").click()
    drag1 = driver.find_element(By.ID, 'box1')
    drag2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box2")))
    drag3 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box3")))
    drag4 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box4")))


    dropbox1 = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.ID, "dropBox")))

    dropbox2 = WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.ID, "dropBox2")))

    ActionChains(driver).drag_and_drop(drag1, dropbox1).perform()
    time.sleep(1)
    ActionChains(driver).drag_and_drop(drag2, dropbox1).perform()
    time.sleep(1)
    ActionChains(driver).drag_and_drop(drag3, dropbox1).perform()
    time.sleep(1)
    ActionChains(driver).drag_and_drop(drag4, dropbox1).perform()
    time.sleep(1)
    ActionChains(driver).drag_and_drop(drag1, dropbox2).perform()
    time.sleep(1)
    ActionChains(driver).drag_and_drop(drag2, dropbox2).perform()
    time.sleep(1)
    ActionChains(driver).drag_and_drop(drag3, dropbox2).perform()
    time.sleep(1)
    ActionChains(driver).drag_and_drop(drag4, dropbox2).perform()

    time.sleep(2)
    driver.quit()

setURL()
draganddrop()
























