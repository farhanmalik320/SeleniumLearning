from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


#driver = webdriver.Chrome(ChromeDriverManager().install())

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)
url = "https://www.google.com/recaptcha/api2/demo"
page = driver.get(url)

time.sleep(5)