import time

import self
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
    current_url = driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    #end text in searchbar

    element=WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'//button[@id="openwindow"]')))
    driver.find_element(By.XPATH, "//button[@id='openwindow']").click()

    handles = driver.window_handles
    size = len(handles)
    print(size)

    driver.switch_to.window(handles[1])
    print(driver.title)

    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header/div[2]/div[1]/nav[1]/ul[1]/li[2]/a[1]")))
    driver.find_element(By.XPATH, "//header/div[2]/div[1]/nav[1]/ul[1]/li[2]/a[1]").click()

    time.sleep(2)

    #course_name= driver.find_elements(By.CSS_SELECTOR, "a[href*='https://courses.rahulshettyacademy.com/p/']")
    course_name = driver.find_elements(By.CSS_SELECTOR, ".courses-block .inner-box .lower-content h2 a")
    print(len(course_name))
    global course_name1
    course_name1= course_name[1].text
    print("The Course name is" + course_name1)
    driver.close()

    driver.switch_to.window(handles[0])

def multipletabs():

    driver.execute_script("window.open('about:blank', 'tab2');")

    driver.switch_to.window('tab2')

    tab2 = driver.get("https://courses.rahulshettyacademy.com/courses")

    search_box = driver.find_element(By.ID, 'search-courses').send_keys(course_name1)
    time.sleep(1)

    driver.find_element(By.ID, 'search-courses').send_keys(Keys.RETURN)

    time.sleep(1)

    courseresult= driver.find_elements(By.CLASS_NAME, 'course-listing-title')
    result=courseresult[0].text
    print("The Actual result is" + result)

    assert result, course_name1
    print("Actual and Expected results are same")

    driver.quit()

    time.sleep(5)

setURL()
multipletabs()
























