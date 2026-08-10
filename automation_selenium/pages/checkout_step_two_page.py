"""
CheckoutStepTwoPage module representing the order summary and overview page in SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    """Encapsulates locators and actions for Checkout Step Two: Overview."""

    # UI Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_at_step_two_page(self) -> bool:
        """Verifies if user is on the checkout overview page."""
        return "checkout-step-two.html" in self.get_current_url() and self.is_element_visible(self.FINISH_BUTTON)

    def get_item_count(self) -> int:
        """Returns number of items in checkout overview."""
        return len(self.find_elements(self.CART_ITEMS))

    def get_item_names(self) -> list[str]:
        """Returns list of item names displayed in overview."""
        return self.driver.execute_script(
            "return Array.from(document.querySelectorAll('.cart_item .inventory_item_name')).map(e => e.innerText.trim());"
        )

    def _extract_dollar_amount(self, locator: tuple[str, str]) -> float:
        """Helper to extract float number from text string (e.g. 'Item total: $29.99' -> 29.99)."""
        text = self.get_element_text(locator)
        match = re.search(r"\$([0-9]+\.[0-9]{2})", text)
        if match:
            return float(match.group(1))
        return 0.0

    def get_subtotal_amount(self) -> float:
        """Returns item subtotal amount."""
        return self._extract_dollar_amount(self.SUBTOTAL_LABEL)

    def get_tax_amount(self) -> float:
        """Returns tax calculation amount."""
        return self._extract_dollar_amount(self.TAX_LABEL)

    def get_total_amount(self) -> float:
        """Returns total order amount."""
        return self._extract_dollar_amount(self.TOTAL_LABEL)

    def click_finish(self) -> None:
        """Clicks the Finish button to complete order."""
        self.click_element(self.FINISH_BUTTON)
        time.sleep(0.3)

    def click_cancel(self) -> None:
        """Clicks the Cancel button to return to Inventory."""
        self.click_element(self.CANCEL_BUTTON)
        time.sleep(0.3)
