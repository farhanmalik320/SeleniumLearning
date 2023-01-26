import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

opt= Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
# create webdriver object
driver = webdriver.Chrome(service=s, chrome_options=opt)

def setURL():
    current_url = driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    #driver.execute_script("document.body.style.zoom='75%'")

def submitform():

    i=0
    length=5
    while i < length:

       #name field
       first_name=WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID,'firstName')))
       first_name= driver.find_element(By.ID,'firstName').send_keys('Farhanm')

       last_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'lastName')))
       last_name=driver.find_element(By.ID, 'lastName').send_keys('Malik')

       last_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID,'userEmail')))
       email= driver.find_element(By.ID,'userEmail').send_keys('Farhan@yopmail.com')

       time.sleep(2)

       male_radio1= driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()

       user_number=driver.find_element(By.ID,'userNumber').send_keys('1234567891')

       dob=driver.find_element(By.ID,'dateOfBirthInput').click()

   # calendar=driver.find_element(By.CLASS_NAME, "react-datepicker__month-container").click()

       time.sleep(1)

    #calendar popup

       select_month=Select(driver.find_element(By.CLASS_NAME,"react-datepicker__month-select"))
       select_month.select_by_index(1)

       time.sleep(1)

       select_year=Select(driver.find_element(By.CLASS_NAME,"react-datepicker__year-select"))
       select_year.select_by_value('1996')

       time.sleep(1)

       select_day= driver.find_element(By.CLASS_NAME, "react-datepicker__day--007").click()

       subject=driver.find_element(By.ID,'subjectsInput').send_keys('Computer Science')
       driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.RETURN)

    #selectfirst=driver.find_element(By.CLASS_NAME,'css-1wy0on6').click()
   # selectfirst[0].click()

       hobbies=driver.find_element(By.XPATH,"//label[contains(text(),'Sports')]").click()

       upload_pic=driver.find_element(By.ID,'uploadPicture').send_keys("F://NFT_s//lifejoke//12.png")

       current_address=driver.find_element(By.ID,'currentAddress').send_keys('Rawalpindi, Isb')

       driver.find_element(By.ID, 'currentAddress').send_keys(Keys.TAB)

       time.sleep(2)

       current_state=driver.find_element(By.XPATH,"//div[contains(text(),'Select State')]").click()

       state_name= driver.find_element(By.ID,'react-select-3-input').send_keys('Haryana')

       driver.find_element(By.ID, 'react-select-3-input').send_keys(Keys.RETURN)
#   select_haryana=driver.find_element(By.XPATH,"//div[contains(text(),'Haryana')]").click()

       city=driver.find_element(By.XPATH,"//div[contains(text(),'Select City')]").click()


       select_city=driver.find_element(By.XPATH,"//div[contains(text(),'Karnal')]").click()

       time.sleep(1)

       WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='submit']")))

       submit_btn=driver.find_element(By.XPATH,"//button[@id='submit']").click()

       time.sleep(5)

       close_btn=driver.find_element(By.ID,'closeLargeModal').click()

       i+=1
       driver.quit()

setURL()
submitform()
























