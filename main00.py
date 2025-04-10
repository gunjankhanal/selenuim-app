from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

input_element.send_keys("upwork devops")



time.sleep(20)

driver.quit()