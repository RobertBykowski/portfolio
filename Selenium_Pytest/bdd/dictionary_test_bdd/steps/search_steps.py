from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from behave import given, when, then

# set the word to be searched for on the website https://www.diki.pl/
word = "home"

@given ("User is on Diki online dictionary website")
def step_start_page (context):
    context.driver.get('https://www.diki.pl/')


@when("User fills in the search bar and submits it")
def step_set_login_in(context):
    
    # find the search field element using its CSS selector
    # click on the search field element to focus on it
    field = context.driver.find_element(By.CSS_SELECTOR, ".dikiSearchInputField")
    field.click()
    # type the word to be searched in the search field
    field.send_keys(word)

    # find the search button element using its CSS selector
    # click on the search button to submit the search
    context.driver.find_element(By.CSS_SELECTOR, ".dikiSearchMainPageSubmit").click()
   
   
    
@then('User can see correct word')
def step_valid_login(context):
    # find the element containing the search result using its CSS selector
    element =  context.driver.find_element(By.CSS_SELECTOR, ".hw")
    text = element.text
    # assert that the retrieved text is equal to the searched word
    assert text == word, f"Expected text 'home', got: '{text}'"