from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_INPUT = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.action.search")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "li.product-item a.product-item-link")

    def search_for_product(self, product_name):
        """Wpisanie nazwy produktu w pole wyszukiwania i kliknięcie przycisku."""
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click_element(self.SEARCH_BUTTON)

    def is_product_visible(self, product_name):
        """Sprawdzenie, czy produkt pojawia się na liście wyników."""
        products = self.find_elements(self.PRODUCT_TITLES)
        return any(product_name.lower() in product.text.lower() for product in products)