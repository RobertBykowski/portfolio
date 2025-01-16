from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        """Znajduje pojedynczy element na stronie."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element {locator} nie został znaleziony w ciągu {self.timeout} sekund.")
            return None

    def find_elements(self, locator):
        """Znajduje wszystkie elementy pasujące do lokatora."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f"Elementy {locator} nie zostały znalezione w ciągu {self.timeout} sekund.")
            return []

    def click_element(self, locator):
        """Kliknięcie w element wskazany przez lokator."""
        element = self.find_element(locator)
        if element:
            element.click()
        else:
            print(f"Nie można kliknąć w element {locator}.")

    def enter_text(self, locator, text):
        """Wpisuje tekst w pole wskazane przez lokator."""
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f"Nie można wpisać tekstu w element {locator}.")

    def get_element_text(self, locator):
        """Pobiera tekst z elementu wskazanego przez lokator."""
        element = self.find_element(locator)
        if element:
            return element.text
        else:
            print(f"Nie można pobrać tekstu z elementu {locator}.")
            return ""

    def hover_over_element(self, locator):
        """Najeżdża kursorem na element wskazany przez lokator."""
        element = self.find_element(locator)
        if element:
            ActionChains(self.driver).move_to_element(element).perform()
        else:
            print(f"Nie można najechać na element {locator}.")

    def is_element_visible(self, locator):
        """Sprawdza, czy element jest widoczny na stronie."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Element {locator} nie jest widoczny w ciągu {self.timeout} sekund.")
            return False

    def is_element_clickable(self, locator):
        """Sprawdza, czy element jest klikalny."""
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Element {locator} nie jest klikalny w ciągu {self.timeout} sekund.")
            return False

    def get_page_title(self):
        """Pobiera tytuł bieżącej strony."""
        return self.driver.title

    def navigate_to(self, url):
        """Nawiguje do podanego URL."""
        self.driver.get(url)
