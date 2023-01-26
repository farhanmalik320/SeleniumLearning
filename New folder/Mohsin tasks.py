from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(5)

openwindow = driver.find_element(By.XPATH, '//*[@id="openwindow"]')
openwindow.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.maximize_window()
time.sleep(5)
headercourses = driver.find_element(By.XPATH, '//*[@id="homepage"]/header/div[2]/div/nav/ul/li[2]/a')
headercourses.click()
time.sleep(5)

firstcourse = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/a/div/div[2]').text
print(firstcourse)






#driver.maximize_window()


#driver.get("http://www.qaclickacademy.com/")
#time.sleep(3)
#print(driver.title)




#courses = driver.find_elements(By.CLASS_NAME, 'upper-box')
#courses.click()
#time.sleep(3)
#print(len(courses))

#firstcourse = driver.find_elements(By.CLASS_NAME, 'upper-box')
#firstcourse.click()
#time.sleep(3)
#print(firstcourse.text)








#driver.close()
