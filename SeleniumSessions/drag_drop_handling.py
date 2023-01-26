import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def setURL():
    current_url = driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
    driver.maximize_window()

def draganddrop():

    drag1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box1")))
    drag2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box2")))
    drag3 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box3")))
    drag4 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box4")))
    drag5 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box5")))
    drag6 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box6")))
    drag7 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box7")))

    drop1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box101")))

    drop2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box102")))

    drop3 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box103")))

    drop4 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box104")))

    drop5 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box105")))

    drop6 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box106")))

    drop7 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "box107")))

    ActionChains(driver).drag_and_drop(drag1, drop1).perform()
    ActionChains(driver).drag_and_drop(drag2, drop2).perform()
    ActionChains(driver).drag_and_drop(drag3, drop3).perform()
    ActionChains(driver).drag_and_drop(drag4, drop4).perform()
    ActionChains(driver).drag_and_drop(drag5, drop5).perform()
    ActionChains(driver).drag_and_drop(drag6, drop6).perform()
    ActionChains(driver).drag_and_drop(drag7, drop7).perform()

    time.sleep(2)

def capturescreenshot():

    driver.save_screenshot("yourpath")

setURL()
draganddrop()
capturescreenshot()
























