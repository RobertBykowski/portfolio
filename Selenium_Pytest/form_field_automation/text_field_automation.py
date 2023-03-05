
# Automation of filling in the form's text fields.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# Opening the browser
driver = webdriver.Firefox()
driver.maximize_window()

# Go to the contact form page
driver.get("https://skleptest.pl/test-contact-blablabla/")


# Typing the name in the form field
name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
 "//input[@class='wpcf7-form-control wpcf7-text wpcf7-validates-as-required']")))
name_field.send_keys("Jan Kowalski")

# Typing the email in the form field. [wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email]
email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
"//input[@class='wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email']")))
email_field.send_keys("jankowalski@example.com")

# Typing the title in the form field.  [wpcf7-form-control wpcf7-text]
subject_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
"//input[@class='wpcf7-form-control wpcf7-text']")))
subject_field.send_keys("Pytanie o produkt")

# Typing the content of a short message in the form field. [wpcf7-form-control wpcf7-textarea]
message_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
"//textarea[@class='wpcf7-form-control wpcf7-textarea']")))
message_field.send_keys("Czy można dostać dodatkowe informacje o produkcie?")

# Click "Send" button
submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
    "//input[@type='submit']")))
submit.click()

# Termination of the browser
driver.quit()
