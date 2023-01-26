import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

# get google.com
current_url = driver.get("https://www.makemytrip.com/")
driver.maximize_window()

time.sleep(5)

from_city=driver.find_element(By.ID,'fromCity').click()

#from text
from_text=driver.find_element(By.CLASS_NAME,'react-autosuggest__input--open').send_keys('PAK')

time.sleep(5)

#print suggestion class data
suggestion_list=driver.find_elements(By.CLASS_NAME, 'react-autosuggest__suggestions-list')
#suggestion_list[5].click()
print(len(suggestion_list))
print("From Suggestion list countries are ")
for suggestionslist in suggestion_list:
    print((suggestionslist.text))

    lst = []
    with open('Test.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(suggestionslist.text)
        #replace data with lst
        writer.writerow(lst)

click_isb=driver.find_elements(By.CLASS_NAME, 'react-autosuggest__suggestion')
click_isb[4].click()

time.sleep(2)

to_city= driver.find_element(By.ID,'toCity').click()

time.sleep(5)

#enter to text

to_text= driver.find_element(By.XPATH,"//input[@placeholder='To']").send_keys('Dubai')

to_suggestion_list=driver.find_elements(By.CLASS_NAME, 'react-autosuggest__suggestions-list')
print(len(to_suggestion_list))
print("To Suggestion list countries are ")
for suggestionslist in to_suggestion_list:
    print((suggestionslist.text))

time.sleep(5)

#select islamabad
to_city_name=driver.find_elements(By.CLASS_NAME,'react-autosuggest__suggestion')
to_city_name[0].click()

time.sleep(2)

search_btn= driver.find_element(By.XPATH,"//a[contains(text(),'Search')]").click()





