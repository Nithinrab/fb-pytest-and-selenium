import pytest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def setup():
    global product,driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.maximize_window()
    yield
    time.sleep()
    driver.close()
def test_searchproducts(setup):
    driver.get("https://www.facebook.com/")
    driver.find_element_by_name("email").send_keys("dbffdjf")
    driver.find_element_by_name("pass").send_keys("bshdbhbc")
    driver.find_element_by_name("login").click()
    time.sleep(5)
