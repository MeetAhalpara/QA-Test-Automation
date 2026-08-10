"""
CheckoutStepOnePage module representing the customer information form in SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Encapsulates locators and actions for Checkout Step One: Your Information."""

    # UI Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_at_step_one_page(self) -> bool:
        """Verifies if the user is on the checkout information page."""
        return "checkout-step-one.html" in self.get_current_url() and self.is_element_visible(self.FIRST_NAME_INPUT)

    def enter_first_name(self, first_name: str) -> "CheckoutStepOnePage":
        """Enters text into the First Name field."""
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        return self

    def enter_last_name(self, last_name: str) -> "CheckoutStepOnePage":
        """Enters text into the Last Name field."""
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        return self

    def enter_postal_code(self, postal_code: str) -> "CheckoutStepOnePage":
        """Enters text into the Postal Code field."""
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def fill_information(self, first_name: str = "", last_name: str = "", postal_code: str = "") -> None:
        """Helper to fill out all information fields."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self) -> None:
        """Clicks the Continue button."""
        self.click_element(self.CONTINUE_BUTTON)
        time.sleep(0.3)

    def click_cancel(self) -> None:
        """Clicks the Cancel button to return to the Cart."""
        self.click_element(self.CANCEL_BUTTON)
        time.sleep(0.3)

    def get_error_message(self) -> str:
        """Returns validation error banner text."""
        return self.get_element_text(self.ERROR_CONTAINER)

    def is_error_displayed(self) -> bool:
        """Checks if validation error is displayed."""
        return self.is_element_visible(self.ERROR_CONTAINER, timeout=2)
