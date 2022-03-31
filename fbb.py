import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(ChromeDriverManager().install())
print("Test Case Started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element_by_name("email").send_keys("dbffdjf")
time.sleep(1)
driver.find_element_by_name("pass").send_keys("bshdbhbc")
time.sleep(5)
driver.find_element_by_name("login").click()
time.sleep(50)
driver.close()
print("test is sucesfully")