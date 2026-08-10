"""
InventoryPage module representing the product catalog page of SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage


class InventoryPage(BasePage):
    """Encapsulates locators and actions for the Product Inventory Page."""

    # UI Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_DESCRIPTIONS = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_IMAGES = (By.CSS_SELECTOR, ".inventory_item_img img")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ACTIVE_SORT_LABEL = (By.CLASS_NAME, "active_option")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # Sidebar Navigation Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ALL_ITEMS_LINK = (By.ID, "inventory_sidebar_link")
    RESET_APP_STATE_LINK = (By.ID, "reset_sidebar_link")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_at_inventory_page(self) -> bool:
        """Verifies if the user is on the inventory page."""
        return "inventory.html" in self.get_current_url() and self.is_element_visible(self.PAGE_TITLE)

    def get_header_title(self) -> str:
        """Returns the page title heading text (e.g. 'Products')."""
        return self.get_element_text(self.PAGE_TITLE)

    def get_product_count(self) -> int:
        """Returns the total number of product items displayed."""
        items = self.find_elements(self.INVENTORY_ITEMS)
        return len(items)

    def get_all_product_names(self) -> list[str]:
        """Returns a list of all product names visible on the inventory grid."""
        return self.driver.execute_script(
            "return Array.from(document.querySelectorAll('.inventory_item_name')).map(e => (e.textContent || '').trim());"
        )

    def get_all_product_prices(self) -> list[float]:
        """Returns a list of all product prices parsed as floats."""
        return self.driver.execute_script(
            "return Array.from(document.querySelectorAll('.inventory_item_price')).map(e => parseFloat((e.textContent || '').replace('$', '').trim()));"
        )

    def click_product_by_name(self, product_name: str) -> None:
        """Clicks a product's name link to navigate to its details page."""
        locator = (By.XPATH, f"//div[contains(@class, 'inventory_item_name') and text()='{product_name}']")
        self.click_element(locator)
        time.sleep(0.3)

    def sort_by(self, option_value: str) -> None:
        """
        Sorts the inventory items by value:
        - 'az' : Name (A to Z)
        - 'za' : Name (Z to A)
        - 'lohi': Price (low to high)
        - 'hilo': Price (high to low)
        """
        self.select_dropdown_by_value(self.SORT_DROPDOWN, option_value)
        time.sleep(0.4)

    def get_active_sort_text(self) -> str:
        """Returns the currently active sort option label."""
        return self.driver.execute_script(
            "return (document.querySelector('.active_option')?.textContent || '').trim();"
        )

    def add_product_to_cart_by_name(self, product_name: str) -> None:
        """Adds a specific product to cart using its name."""
        locator = (By.XPATH, f"//div[contains(text(),'{product_name}')]/ancestor::div[@class='inventory_item']//button")
        self.click_element(locator)
        time.sleep(0.2)

    def add_product_to_cart_by_index(self, index: int = 0) -> None:
        """Adds product to cart by item index (0-based)."""
        buttons = self.find_elements((By.CSS_SELECTOR, ".inventory_item button"))
        if buttons and len(buttons) > index:
            self.driver.execute_script("arguments[0].click();", buttons[index])
            time.sleep(0.2)

    def remove_product_from_cart_by_name(self, product_name: str) -> None:
        """Removes a specific product from cart on inventory page."""
        locator = (By.XPATH, f"//div[contains(text(),'{product_name}')]/ancestor::div[@class='inventory_item']//button[contains(text(),'Remove')]")
        self.click_element(locator)
        time.sleep(0.2)

    def get_cart_badge_count(self) -> int:
        """Returns the integer count displayed on the shopping cart badge, or 0 if absent."""
        count_str = self.driver.execute_script(
            "return (document.querySelector('.shopping_cart_badge')?.textContent || '').trim();"
        )
        return int(count_str) if count_str.isdigit() else 0

    def click_cart_icon(self) -> None:
        """Clicks the shopping cart icon to open the cart page."""
        self.click_element(self.CART_ICON)
        time.sleep(0.3)

    def open_sidebar_menu(self) -> None:
        """Opens the hamburger sidebar navigation menu."""
        self.click_element(self.MENU_BUTTON)
        time.sleep(0.5)

    def click_logout(self) -> None:
        """Opens sidebar and clicks the Logout link."""
        self.open_sidebar_menu()
        self.click_element(self.LOGOUT_LINK)
        time.sleep(0.5)
