import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

# get google.com
current_url = driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#click on radio button
radio_btn=driver.find_elements(By.CLASS_NAME,'radioButton')
length= len(radio_btn)
print('*************************')
print('The Length of the radio buttons are ' + str(length))
radio_btn[1].click()
print('*************************')
status= radio_btn[1].is_selected()
print(status)

print('*************************')
print('The name of the radio buttons are')

label1 = driver.find_element(By.CSS_SELECTOR, "label[for='radio1']")
label2 = driver.find_element(By.CSS_SELECTOR, "label[for='radio2']")
label3 = driver.find_element(By.CSS_SELECTOR, "label[for='radio3']")

print(label1.text)
print(label2.text)
print(label3.text)
print('*************************')

time.sleep(2)

#auto complete drop down
autocomplete=driver.find_element(By.ID,'autocomplete').send_keys('Au')

time.sleep(5)

resultclass=driver.find_elements(By.CLASS_NAME,'ui-menu-item-wrapper')
print('The name of the Auto suggested countries are')
for suggestionlist in resultclass:
    print(suggestionlist.text)
    print('*************************')
resultclass[4].click()

time.sleep(5)

#dropdown list
dropdown=Select(driver.find_element(By.ID,'dropdown-class-example'))
dropdown.select_by_visible_text('Option1')
time.sleep(2)
dropdown.select_by_index(2)

time.sleep(2)
dropdown.select_by_value('option3')

#checkbox
checkbox1=driver.find_element(By.NAME,'checkBoxOption1')
checkbox1.click()

checkbox2=driver.find_element(By.NAME,'checkBoxOption2')
checkbox2.click()

checkbox3=driver.find_element(By.NAME,'checkBoxOption3')
checkbox3.click()

time.sleep(2)
driver.close()


















