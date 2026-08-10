"""
CartPage module representing the shopping cart interface in SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage


class CartPage(BasePage):
    """Encapsulates locators and actions for the Shopping Cart Page."""

    # UI Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QUANTITIES = (By.CLASS_NAME, "cart_quantity")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_at_cart_page(self) -> bool:
        """Verifies if the user is on the cart review page."""
        return "cart.html" in self.get_current_url() and self.is_element_visible(self.PAGE_TITLE)

    def get_cart_item_count(self) -> int:
        """Returns number of items currently in the cart list."""
        return len(self.find_elements(self.CART_ITEMS, timeout=2))

    def get_cart_item_names(self) -> list[str]:
        """Returns a list of item names present in the cart."""
        return self.driver.execute_script(
            "return Array.from(document.querySelectorAll('.cart_item .inventory_item_name')).map(e => e.innerText.trim());"
        )

    def get_cart_item_prices(self) -> list[float]:
        """Returns a list of item prices in the cart."""
        return self.driver.execute_script(
            "return Array.from(document.querySelectorAll('.cart_item .inventory_item_price')).map(e => parseFloat(e.innerText.replace('$', '').trim()));"
        )

    def remove_item_by_name(self, product_name: str) -> None:
        """Removes an item from cart by its name."""
        locator = (By.XPATH, f"//div[contains(text(),'{product_name}')]/ancestor::div[@class='cart_item']//button[contains(text(),'Remove')]")
        self.click_element(locator)
        time.sleep(0.2)

    def click_continue_shopping(self) -> None:
        """Clicks the 'Continue Shopping' button to return to inventory."""
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)
        time.sleep(0.3)

    def click_checkout(self) -> None:
        """Clicks the 'Checkout' button to proceed to Step 1."""
        self.click_element(self.CHECKOUT_BUTTON)
        time.sleep(0.3)
