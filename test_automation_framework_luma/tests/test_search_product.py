import pytest
from selenium import webdriver

from pages import create_account_page
from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage
import json
import os
import time

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")
    yield driver
    driver.quit()

def load_test_data(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)

@pytest.mark.parametrize("test_data", load_test_data(os.path.join(os.path.dirname(__file__), '..', 'test_data', 'search_product_data.json')))
def test_search_product(driver, test_data):
    search_results_page = SearchResultsPage(driver)
    time.sleep(4)
    popup = HomePage(driver)
    popup.click_button_agree()  # popup
    search_results_page.search_for_product(test_data["product_name"])
    assert search_results_page.is_product_visible(test_data["product_name"]), f"Produkt {test_data['product_name']} nie został znaleziony."