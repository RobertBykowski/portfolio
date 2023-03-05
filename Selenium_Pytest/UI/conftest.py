# This is content of conftest.py
from selenium import webdriver
import pandas as pd
import pytest
import pytest_trace

@pytest.fixture(params=pd.read_csv("data_product.csv").to_dict(orient="records"))
def data_product(request):
    return request.param


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    # Headless - test mode without a graphical interface
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Firefox(options=options)
    # --
    driver.delete_all_cookies()
    driver.maximize_window()
    
    
    yield driver
    
    driver.close()