ID Case Test - TC-UI-0220232
Testing the correctness of displaying product information on the product page.

This is a user interface test to check the functionality and correctness of displaying product information on the product page in the demo.nopcommerce.com online store. The test includes content compliance with the content of individual product records from the product database.
Elements list: name, short_description, sku, price, add_to_cart, long_description

<!-- Test details -->
    Scenario name - Testing the correctness of displaying product information on the product page.
    Description of the test case - Testing the correctness of displaying product information on the product page for fields: name, short_description, sku, price, add_to_cart, long_description.
    Expected Value/Expected Result: The expected result of this test case is that all the fields (name, short_description, sku, price, add_to_cart, and long_description) on the product page are correctly displayed and their values are accurate from db.

    Test test steps: 
    Step 1. Go to the product page https://demo.nopcommerce.com/adidas-consortium-campus-80s-running-shoes
    Step 2. Check that this is the correct page.
    Step 3. Validate the content of a name field.  
    Step 4. Validate the content of a short_description field. 
    Step 5. Validate the content of a sku field. 
    Step 6. Validate the content of a price field. 
    Step 7. Validate the content of a button add to cart.  
    Step 8. Validate the content of a long description field. 
    Step 9. A screenshot product page, and save it as a png.

    These initial conditions are necessary to execute the test case - deployed.

<!-- Requirements -->

    Python 3.x
    Selenium WebDriver
    Pytest
    Pytest-html
    Pandas

<!-- Configuration -->

    To configure the testing environment, follow these steps:

    Install Python 3.x
    Install Selenium WebDriver
    Install Pytest, Pytest-html, Pandas
    Download the latest version of Firefox nad install 
    The configuration of the test environment is in the conftest.py file. The new user's login data is transferred via the @pytest.fixture mechanism, and the user's test data is stored in the data_user.csv file.

<!-- Running the tests -->

    Clone the repository and navigate to the project directory.
    Run the command pytest -v test_product_page_elems_content or 
    Pytest will execute the test case and provide a summary of the results.

<!-- Reporting -->

    Pytest generates a test report in the command line interface. This report provides details on the number of tests executed, the number of tests passed, and the number of tests failed.
    To generate an HTML report, run the tests with the --html=report.html option. The report file report.html is located in the tests directory.

<!-- Limitations -->

    These tests were executed on the demo.nopcommerce.com website, and the results may differ on other instances of the website.
    These tests were executed using the Chrome and Firefox browsers, and the results may differ on other browsers.
    These tests verify the successful registration of a user, but do not test the subsequent login or purchase process.
    These tests do not cover negative test cases (e.g., entering incorrect or incomplete data into the registration form).
    These tests do not cover edge cases, such as registering a user with a pre-existing email address or password.

