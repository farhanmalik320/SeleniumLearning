from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select


#location of firefox driver
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

s = Service(r"C:\Users\cva\PycharmProjects\geckodriver.exe")
driver = webdriver.Firefox(service=s, options=options)

url = "https://demoqa.com/automation-practice-form"
driver.get(url)
driver.maximize_window()
driver.execute_script("document.body.style.zoom='75%'")

First_name = ['Basit', 'Owais', 'Ahmad', 'Ali', 'hamid' ]
Last_name = ['ABasit', 'AOwais', 'AAhmad', 'AAli', 'Ahamid' ]
EEmail = ['qwe@yopmail1.com','qwe@yopmail11.com','qwe@yopmail111.com','qwe@yopmail111.com','qwe@yopmail1111.com']
gender = [0, 1, 2, 1, 0]
Date = ['28 Nov 1995','23 Nov 1995','10 Nov 1995','3 Nov 1995','23 Nov 1995']
Subject =['Computer Science','Computer Science','Computer Science','Computer Science','Computer Science',]
#hoby = [0, 1, 2, 1, 0]
mobile = ['1234567891','1234567891','1234567891','1234567891','1234567891']
aaddress = ['qweyopmail1','qweyopmails1','qwesyopmail1','qweyosspmail1','qweyopssmail1']
x=0
name = print(len(First_name))
for x in range(0, len(First_name)):
    first_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'firstName')))
    F_name = driver.find_element(By.ID,'firstName')
    F_name.send_keys(First_name[x])

    #Last name Name
    L_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lastName"]')))
    L_name = driver.find_element(By.XPATH,'//*[@id="lastName"]')
    L_name.send_keys(Last_name[x])

    #Email
    Email = driver.find_element(By.XPATH,'//*[@id="userEmail"]')
    Email.send_keys(EEmail[x])
    time.sleep(1)
    #Gender
    Gender = driver.find_elements(By.CLASS_NAME,'custom-control-label')
    #Gender = driver.find_elements(By.NAME,'gender')
    Gender[gender[x]].click()


    upload = "F:\\NFT_s\\lifejoke\\12.png"
    driver.find_element(By.ID, "uploadPicture").send_keys (upload)
    # upload_pic = driver.find_element(By.ID, 'uploadPicture').send_keys("F://NFT_s//lifejoke//12.png")

    # Mobile Number 10 digits
    Mobile = driver.find_element(By.XPATH, '//*[@id="userNumber"]')
    Mobile.send_keys(mobile[x])
    time.sleep(2)

    # Date
    #Dat = driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]')
    #Dat.click()  # Focus input field
    #Dat.send_keys(Keys.CONTROL, "a")  # Select all pre-existing text/input value
    #Dat.send_keys(Date[x])
    #time.sleep(1)
    #dob = driver.find_element(By.ID, 'dateOfBirthInput')
    #driver.execute_script('arguments[0].click()', dob)
    dob = driver.find_element(By.ID, 'dateOfBirthInput')
    driver.execute_script('arguments[0].click()', dob)

    # calendar popup

    select_month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    select_month.select_by_index(1)

    time.sleep(1)

    select_year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    select_year.select_by_value('1996')

    time.sleep(1)

    select_day = driver.find_element(By.CLASS_NAME, "react-datepicker__day--007")
    driver.execute_script('arguments[0].click()', select_day)

    time.sleep(1)

    # Subject
    driver.find_element(By.XPATH, '//*[@id="subjectsInput"]').send_keys('Computer Science')
    enter_key = driver.find_element(By.XPATH, '//*[@id="subjectsInput"]').send_keys(Keys.ENTER)
    # Subj.send_keys(Subject[x])

    # to click on button with Javascript executor
    Hobbies = driver.find_element(By.ID,"hobbies-checkbox-1")
    driver.execute_script("arguments[0].click();", Hobbies)

    # Address
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="currentAddress"]')))
    Address = driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
    Address.send_keys(aaddress[x])
    time.sleep(1)

    # Select State
    driver.find_element(By.ID, 'currentAddress').send_keys(Keys.TAB)
    state_name = driver.find_element(By.ID, 'react-select-3-input').send_keys('Haryana')
    driver.find_element(By.ID, 'react-select-3-input').send_keys(Keys.RETURN)
    driver.find_element(By.ID, 'react-select-3-input').send_keys(Keys.TAB)

    # Select City
    select_city = driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.TAB)
    select_city = driver.find_element(By.ID, "react-select-4-input").send_keys("Karnal")
    driver.find_element(By.ID, 'react-select-4-input').send_keys(Keys.RETURN)

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']")))
    # Click on submitt Button
    submit = driver.find_element(By.XPATH, "//button[@id='submit']")
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(1)

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, "closeLargeModal")))
    # pop up cloce
    submit1 = driver.find_element(By.ID, 'closeLargeModal')
    driver.execute_script("arguments[0].click();", submit1)
    x+=1
    time.sleep(2)
