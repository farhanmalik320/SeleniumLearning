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
    current_url = driver.get("https://demo.guru99.com/test/simple_context_menu.html")
    driver.maximize_window()

def right_click():

    right_click_btn = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
    action = ActionChains(driver)
    action.context_click(right_click_btn).perform()

    copy_option = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
    obj = driver.switch_to.alert
    msg = obj.text
    print("Alert shows following message: " + msg)
    obj.accept()

def double_click():

    double_click_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
    action = ActionChains(driver)
    action.double_click(double_click_btn).perform()
    obj = driver.switch_to.alert
    msg = obj.text
    print("Alert shows following message: " + msg)
    obj.accept()

def capturescreenshot():

    driver.save_screenshot("C:\\Users\\cva\\PycharmProjects\\SeleniumLearning\\1.png")

setURL()
#right_click()
double_click()
capturescreenshot()
























