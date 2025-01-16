from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Lokatory elementów na stronie głównej
    SEARCH_BAR = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.action.search")
    SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign In")
    CREATE_ACCOUNT_BUTTON = (By.LINK_TEXT, "Create an Account")
    SALE_MENU = (By.LINK_TEXT, "Sale")
    WOMEN_MENU = (By.LINK_TEXT, "Women")
    CART_ICON = (By.CSS_SELECTOR, "a.action.showcart")
    BUTTON_AGREE = (By.XPATH, "//button[span[text()='AGREE']]")

    def search_product(self, product_name):
        """Wyszukuje produkt na stronie."""
        self.enter_text(self.SEARCH_BAR, product_name)
        self.click_element(self.SEARCH_BUTTON)

    def click_sign_in(self):
        """Kliknięcie przycisku logowania."""
        self.click_element(self.SIGN_IN_BUTTON)

    def click_create_account(self):
        """Kliknięcie przycisku rejestracji."""
        self.click_element(self.CREATE_ACCOUNT_BUTTON)

    def navigate_to_sale(self):
        """Przejście do sekcji 'Sale'."""
        self.click_element(self.SALE_MENU)

    def navigate_to_women_section(self):
        """Przejście do sekcji 'Women'."""
        self.click_element(self.WOMEN_MENU)

    def open_cart(self):
        """Otwarcie koszyka zakupowego."""
        self.click_element(self.CART_ICON)

    def is_cart_visible(self):
        """Sprawdzenie, czy ikona koszyka jest widoczna."""
        return self.is_element_visible(self.CART_ICON)

    def click_button_agree(self):
        """Kliknięcie przycisku AGREE. - POPUP"""
        self.click_element(self.BUTTON_AGREE)
