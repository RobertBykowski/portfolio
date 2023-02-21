# BDD test logging into the website using access data in the form of 
# - correct username 
# - wrong password

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from behave import given, when, then

# Login details passed as variables
username = "ptx4567"
password = "Kot_75"


@given ("User is on WSB website")
def step_start_page (context):
    context.driver.get('https://login.wsb.pl/cas/login?service=https%3A%2F%2Fportal.wsb.pl%2Fc%2Fportal%2Flogin%3Fredirect%3D%252F%26refererPlid%3D3593%26p_l_id%3D60068')



@when("User fills in the Sign In form and submits it")
def step_set_login_in(context):
    context.driver.find_element(By.ID, 'username2').send_keys(username)
    context.driver.find_element(By.ID, 'password').send_keys(password)
    context.driver.find_element(By.ID, 'login_button').click()
    
@then('User can see email list')
def step_valid_login(context):
    context.driver.save_screenshot("screenshot-login.png")
    # context.driver.find_element(By.CSS_SELECTOR, " class=").click()
    context.driver.implicitly_wait(2)
    assert context.driver.find_element(By.CLASS_NAME,'user-info-album')

