from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CreateAccountPage(BasePage):
    # Lokatory pól formularza rejestracji
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    EMAIL_INPUT = (By.ID, "email_address")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "password-confirmation")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button.action.submit.primary")
    BUTTON_AGREE = (By.XPATH,"//button[span[text()='AGREE']]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.message-success")


    def enter_first_name(self, first_name):
        """Wpisanie imienia."""
        self.enter_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        """Wpisanie nazwiska."""
        self.enter_text(self.LAST_NAME_INPUT, last_name)

    def enter_email(self, email):
        """Wpisanie adresu e-mail."""
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Wpisanie hasła."""
        self.enter_text(self.PASSWORD_INPUT, password)

    def confirm_password(self, password):
        """Potwierdzenie hasła."""
        self.enter_text(self.CONFIRM_PASSWORD_INPUT, password)

    def click_button_agree(self):
        """Kliknięcie przycisku AGREE. - POPUP"""
        self.click_element(self.BUTTON_AGREE)

    def click_create_account(self):
        """Kliknięcie przycisku rejestracji."""
        self.click_element(self.CREATE_ACCOUNT_BUTTON)

    def is_registration_successful(self):
        """Sprawdzenie, czy rejestracja zakończyła się sukcesem."""
        return self.is_element_visible(self.SUCCESS_MESSAGE)
