# This is content of conftest.py
from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    # driver = webdriver.Firefox()
    # Headless - test mode without a graphical interface
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    # --
    driver.delete_all_cookies()
    driver.maximize_window()
    yield driver
    
    driver.close()
   