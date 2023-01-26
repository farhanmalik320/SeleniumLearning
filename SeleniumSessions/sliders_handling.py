from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def setURL():

    current_url = driver.get("https://jqueryui.com/slider/")

    driver.maximize_window()

def slider_handling():

    frame= driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    slider= driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")

    actions= ActionChains(driver)

    actions.move_to_element(slider).drag_and_drop_by_offset(slider, 550,0).perform()

    actions.move_to_element(slider).drag_and_drop_by_offset(slider, -250,0).perform()

setURL()
slider_handling()
























