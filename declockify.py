from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/matthew.gaiser/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://clockify.me/login")
assert "Log In" in driver.title
time.sleep(5)
username = driver.find_element_by_name("email")
password = driver.find_element_by_name("password")

username.send_keys("matthew.gaiser@calgaryparking.com")
password.send_keys("Kinelexz19")
time.sleep(2)
driver.find_element_by_class_name("cl-btn-primary").click()

#driver.close()