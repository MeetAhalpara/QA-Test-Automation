"""
ProductDetailsPage module representing the single item view in SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    """Encapsulates locators and actions for the Product Details Page."""

    # UI Locators
    BACK_BUTTON = (By.ID, "back-to-products")
    ITEM_NAME = (By.CLASS_NAME, "inventory_details_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_details_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_details_price")
    ITEM_IMG = (By.CSS_SELECTOR, ".inventory_details_img")
    ACTION_BUTTON = (By.CSS_SELECTOR, ".inventory_details_desc_container button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_at_details_page(self) -> bool:
        """Verifies if the user is on the product details page."""
        return "inventory-item.html" in self.get_current_url() and self.is_element_visible(self.ITEM_NAME)

    def get_product_name(self) -> str:
        """Returns the product name heading."""
        return self.get_element_text(self.ITEM_NAME)

    def get_product_description(self) -> str:
        """Returns the product description text."""
        return self.get_element_text(self.ITEM_DESC)

    def get_product_price(self) -> float:
        """Returns the numeric price of the product."""
        price_text = self.get_element_text(self.ITEM_PRICE).replace("$", "").strip()
        return float(price_text)

    def is_product_image_displayed(self) -> bool:
        """Checks if product image is visible."""
        return self.is_element_visible(self.ITEM_IMG)

    def click_add_to_cart(self) -> None:
        """Clicks the Add to cart button."""
        self.click_element(self.ACTION_BUTTON)
        time.sleep(0.2)

    def click_remove_from_cart(self) -> None:
        """Clicks the Remove button."""
        self.click_element(self.ACTION_BUTTON)
        time.sleep(0.2)

    def get_action_button_text(self) -> str:
        """Returns button label (e.g., 'Add to cart' or 'Remove')."""
        return self.get_element_text(self.ACTION_BUTTON)

    def click_back_to_products(self) -> None:
        """Clicks the Back to products navigation button."""
        self.click_element(self.BACK_BUTTON)
        time.sleep(0.3)
