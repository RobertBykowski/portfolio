# Validation of a browser refers to the process of verifying that 
# a web browser is working correctly and meets the requirements 
# for displaying web content. 

# Negative search engine test, with the correct message. 
# "No products were found that matched your criteria."
# Click on the "search" button.

from conftest import browser as browser #testing environment
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
   

def test_shop_browser(browser):
    # Step 1. Open the store's website. https://demo.nopcommerce.com
    browser.get("https://demo.nopcommerce.com")

    # Step 2. Check that the store homepage is loading and that it is the correct page.
    assert "demo.nopcommerce.com" in browser.current_url

    # Step 3. Find the search box on the store homepage.
    # Step 4. Enter the keyword "<key1>" into the search box.
    # Entering the keyword you are looking for in the search engine
    # id="small-searchterms"
    search_box = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
    search_box.clear()
    search_box.send_keys("home")



    # Step 5. Click on the "search" button.
    # <button type="submit" class="button-1 search-box-button">Search</button>
    button_search = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    button_search.click()

    # Step 6. Check if the search results page contains products related to "<key1>".
    # assert Check if search results are displayed
    assert "search" in browser.current_url

    # Step 7.The appearance of the message "No products were found that matched your criteria."

    message = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH,
    "//div[@class='no-result']")))

    assert message.text == "No products were found that matched your criteria."

        
    # Step 8. Take a screenshot of the result list, and save it as screenshot png
    browser.get_screenshot_as_file("screenshot/ss_res_inv_inp_btn.png")
    
   
