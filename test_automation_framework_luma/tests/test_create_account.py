import time
from telnetlib import EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_automation_framework_luma.pages.create_account_page import CreateAccountPage
import csv
import os
from pathlib import Path


@pytest.fixture(scope="function")
def driver():
    # Uruchomienie przeglądarki
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    yield driver
    driver.quit()


def load_test_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]




@pytest.mark.parametrize("test_data", load_test_data(os.path.join(os.path.dirname(__file__), '..', 'test_data', 'create_account_data.csv')))
def test_create_account(driver, test_data):
    create_account_page = CreateAccountPage(driver)
    time.sleep(4)
    create_account_page.click_button_agree() # popup
    create_account_page.enter_first_name(test_data["first_name"])
    create_account_page.enter_last_name(test_data["last_name"])
    create_account_page.enter_email(test_data["email"])
    create_account_page.enter_password(test_data["password"])
    create_account_page.confirm_password(test_data["password"])
    create_account_page.click_create_account()
    # To wiadomość, która zostanie wyświetlona, jeśli asercja nie powiedzie się (czyli jeśli is_registration_successful() zwróci False).
    assert create_account_page.is_registration_successful(), "Rejestracja nie powiodła się."


