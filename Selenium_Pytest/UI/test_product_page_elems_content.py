# # ID Case Test - TC-UI-0220232
# The purpose of the test is to check the correct order in which important 
# elements are displayed on the product page. 
# Elements list: name, short_description, sku, price, add_to_cart, long_description


from conftest import browser as browser #testing environment
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Step 1. Go to the product page https://demo.nopcommerce.com/adidas-consortium-campus-80s-running-shoes
def test_product_page(browser, data_product):
    browser.get(data_product["http"])

# Step 2. Check that this is the correct page.
    assert data_product["http"] in browser.current_url


# Step 3. Validate the content of a name field.  
def test_name_content(browser, data_product):
    browser.get(data_product["http"])
    content_name = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-name")))
    assert content_name.text == data_product["name"]
    
# Step 4. Validate the content of a short_description field.  
def test_short_description_content(browser, data_product):
    browser.get(data_product["http"])
    content_short_description = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".short-description")))
    assert content_short_description.text ==  data_product["short_description"]

# Step 5. Validate the content of a sku field.  
def test_sku_content(browser, data_product):
    browser.get(data_product["http"])
    content_sku = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, "value")))
    assert content_sku.text == data_product["sku"]

# Step 6. Validate the content of a price field.  
def test_price(browser, data_product):
    browser.get(data_product["http"])
    price = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[id^='price-value-']")))
    assert price.text == data_product["price"]

# Step 7. Validate the content of a button add to cart.  
def test_button_add_to_cart(browser, data_product):
    browser.get(data_product["http"])
    content_add_to_cart = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-productid] ")))
    assert content_add_to_cart.text == data_product["add_to_cart"]

# Step 8. Validate the content of a long description field.  
def test_long_description_content(browser, data_product):
    browser.get(data_product["http"])
    content_long_description = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.full-description > p")))
    assert content_long_description.text in data_product["long_description"]
# Step 9. A screenshot product page, and save it as a png.
    # browser.save_screenshot("../../tests/UI/screenshots/ss_product_page.png")
    browser.set_window_size(1920, 1280)
    browser.get_screenshot_as_file("../../tests/UI/screenshots/ss_product_page1.png") 
    
                 