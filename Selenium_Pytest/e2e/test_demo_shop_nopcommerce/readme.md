# Description of tests

    End-to-end automated tests will be performed on the search functionality of the https://demo.nopcommerce.com online store. The tests will check the correct functioning of the search field in the form of a text box, the confirmation of the search, the display of the product list and the display of a message when no products are found.

# Requirements

    Python 3.x
    Pytest library
    Selenium library
    Web browser driver (Chrome or Firefox)

# Configuration

    Install Python 3.x
    Install the Pytest library by typing the command in the terminal: pip install pytest
    Install the Selenium library by typing the command in the terminal: pip install selenium
    Download is automated for  the Chrome or Firefox web browser driver.
    The file conftest.py is responsible for setting up the test environment for these tests.

# Running tests

    Open a terminal and navigate to the project folder.
    Type the command pytest and press Enter.
    The automated tests will run and the results will be displayed in the terminal.

# Reporting + screenshot

    A report of the tests will be generated automatically upon completion and will contain information on the number of cases tested, the number of cases successfully completed and the number of cases that failed.

    In "screenshot" directory you can find screenshots from result of search. For Step 8. Take a screenshot of the result list, and save it as screenshot png format.

# Limitations

    Tests cover only the search functionality of the https://demo.nopcommerce.com online store.
    Tests will be performed only on the Google Chrome or Mozilla Firefox web browser.
    Tests do not cover other functionalities of the online store besides the search function.
    Tests do not cover use cases where the entered keyword contains typos or spelling errors.

# Scenario ID | KeyWord	| Scenario name
    --
    ST1-12-2022	| Search	| Verify that entering the correct search term returns the expected search results.
    --
    ST1-12-2023	| Search	| Verify that entering the correct search term returns the expected search results.
    --
    ST1-12-2024	| Search	| Verify that entering an invalid search term returns no search results.
    --
    ST1-12-2025	|Search	    | Verify that entering an invalid search term returns no search results.

# Scenarios and test cases - much more
    If you want know more in file : Nopcommerce scenarios and test cases.xlsx