import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

#opt= Options()
#opt.add_experimental_option("debuggerAddress", "localhost:8989")
# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    #current_url = driver.get("http://demo.guru99.com/test/delete_customer.php")
    driver.maximize_window()
    #driver.execute_script("document.body.style.zoom='75%'")

def handlealert():

    time.sleep(2)
    customer_id = driver.find_element(By.NAME, "cusid")
    customer_id.send_keys("53920")
    driver.find_element(By.NAME, "submit").submit()

    obj = driver.switch_to.alert

    msg = obj.text
    print("Alert shows following message: " + msg)

    obj.accept()

    time.sleep(2)
    customer_id = driver.find_element(By.NAME, "cusid")
    customer_id.send_keys("53920")
    driver.find_element(By.NAME, "submit").submit()

    obj = driver.switch_to.alert

    msg = obj.text
    print("Alert shows following message: " + msg)

    obj.dismiss()

def handlealert1():

    username= driver.find_element(By.ID, "name").send_keys("Farhan")
    driver.find_element(By.ID, "alertbtn").click()

    obj = driver.switch_to.alert

    msg = obj.text
    print("Alert shows following message: " + msg)

    time.sleep(2)

    obj.accept()

    time.sleep(2)

    username = driver.find_element(By.ID, "name").send_keys("Farhan")
    driver.find_element(By.ID, "confirmbtn").click()

    obj = driver.switch_to.alert

    msg = obj.text
    print("Alert shows following message: " + msg)

    time.sleep(2)

    obj.dismiss()

def elementvisible():
    text_box= driver.find_element(By.ID,'displayed-text').is_displayed()
    print(text_box)

    hide_btn=driver.find_element(By.ID,'hide-textbox').click()
    text_box = driver.find_element(By.ID, 'displayed-text').is_displayed()
    print(text_box)

    show_btn=driver.find_element(By.ID,'show-textbox').click()
    text_box = driver.find_element(By.ID, 'displayed-text').is_displayed()
    print(text_box)

def capturescreenshot():
    driver.save_screenshot("C://Users//cva//PycharmProjects//SeleniumLearning//1.png")

setURL()
#handlealert()
#handlealert1()
elementvisible()
#capturescreenshot()
























