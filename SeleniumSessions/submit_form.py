import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

s= Service(r"F:\ChromeDRIVER\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
    current_url = driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()

def submitform():

    i=0
    j=1
    firstname=['farhan', 'Soha', 'Gohar', 'Basit', 'Mohsin', 'Zeeshan', 'Shair']
    lastname= ['Sharif', 'Manzoor', 'Ali', 'Scientist', 'Riaz', 'Shah', 'Ali']
    email= ['farhan@yopmail.com', 'soha@yopmail.com', 'gohar@yopmail.com', 'basit@yopmail.com', 'mohsin@yopmail.com', 'zeeshan@yopmail.com', 'shair@yopmail.com']
    mobileno= ['1234567890', '12345673890', '1234567890', '1234567890', '1234567890', '1234567890', '1234567890']

    name= print(len(firstname))
    while str(i) < str(name):

       #name field
       first_name=WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID,'firstName')))
       first_name= driver.find_element(By.ID,'firstName').send_keys(firstname[i])

       last_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'lastName')))
       last_name=driver.find_element(By.ID, 'lastName').send_keys(lastname[i])

       user_email = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID,'userEmail')))
       driver.find_element(By.ID,'userEmail').send_keys(email[i])

       male_radio = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Male')]")))

       driver.execute_script("window.scrollTo(100,document.body.scrollHeight)")

       if i == 1:
          female_radio = driver.find_element(By.XPATH, "//label[contains(text(),'Female')]")
          driver.execute_script('arguments[0].click()', female_radio)

       else:
          male_radio1= driver.find_element(By.XPATH, "//label[contains(text(),'Male')]")
          driver.execute_script('arguments[0].click()', male_radio1)

       user_number=driver.find_element(By.ID,'userNumber').send_keys(mobileno[i])

       dob=driver.find_element(By.ID,'dateOfBirthInput')
       driver.execute_script('arguments[0].click()', dob)

       #calendar popup

       select_month=Select(driver.find_element(By.CLASS_NAME,"react-datepicker__month-select"))
       select_month.select_by_index(1)

       time.sleep(1)

       select_year=Select(driver.find_element(By.CLASS_NAME,"react-datepicker__year-select"))
       select_year.select_by_value('1996')

       time.sleep(1)

       select_day= driver.find_element(By.CLASS_NAME, "react-datepicker__day--007")
       driver.execute_script('arguments[0].click()', select_day)

       subject=driver.find_element(By.ID,'subjectsInput').send_keys('Computer Science')
       driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.RETURN)

       hobbies=driver.find_element(By.XPATH,"//label[contains(text(),'Sports')]")
       driver.execute_script('arguments[0].click()', hobbies)

       upload_pic=driver.find_element(By.ID,'uploadPicture').send_keys("F://NFT_s//lifejoke//12.png")

       current_address=driver.find_element(By.ID,'currentAddress').send_keys('Rawalpindi, Isb')

       driver.execute_script("document.body.style.zoom='50%'")

       driver.find_element(By.ID, 'currentAddress').send_keys(Keys.TAB)
       state_name= driver.find_element(By.ID,'react-select-3-input').send_keys('Haryana')
       driver.find_element(By.ID, 'react-select-3-input').send_keys(Keys.RETURN)
       driver.find_element(By.ID, 'react-select-3-input').send_keys(Keys.TAB)

      # city=driver.find_element(By.XPATH,"//div[contains(text(),'Select City')]")
      # driver.execute_script('arguments[0].click()', city)


       select_city=driver.find_element(By.ID,"react-select-4-input").send_keys("Karnal")

       driver.find_element(By.ID, 'react-select-4-input').send_keys(Keys.RETURN)

       time.sleep(1)

       WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='submit']")))

       submit_btn=driver.find_element(By.XPATH,"//button[@id='submit']")
       driver.execute_script('arguments[0].click()', submit_btn)

       time.sleep(2)

       close_btn=driver.find_element(By.ID,'closeLargeModal')
       driver.execute_script('arguments[0].click()', close_btn)

       i+=1
       j+=1
       time.sleep(2)

setURL()
submitform()
























