"""
CheckoutCompletePage module representing the order confirmation page in SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Encapsulates locators and actions for Checkout Complete confirmation."""

    # UI Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    PONY_EXPRESS_IMG = (By.CLASS_NAME, "pony_express")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_at_complete_page(self) -> bool:
        """Verifies if the user is on the order complete confirmation screen."""
        return "checkout-complete.html" in self.get_current_url() and self.is_element_visible(self.COMPLETE_HEADER)

    def get_complete_header(self) -> str:
        """Returns the confirmation header text (e.g., 'Thank you for your order!')."""
        return self.get_element_text(self.COMPLETE_HEADER)

    def get_complete_text(self) -> str:
        """Returns the confirmation body message."""
        return self.get_element_text(self.COMPLETE_TEXT)

    def is_pony_image_displayed(self) -> bool:
        """Verifies if the pony express graphic is visible."""
        return self.is_element_visible(self.PONY_EXPRESS_IMG)

    def click_back_home(self) -> None:
        """Clicks the 'Back Home' button to return to the product catalog."""
        self.click_element(self.BACK_HOME_BUTTON)
        time.sleep(0.3)
