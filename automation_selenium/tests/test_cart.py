"""
Automated Test Cases for Shopping Cart Management (TC-06, TC-07, TC-08).
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import pytest
from automation_selenium.pages.inventory_page import InventoryPage
from automation_selenium.pages.cart_page import CartPage
from automation_selenium.pages.product_details_page import ProductDetailsPage


@pytest.mark.cart
class TestCart:
    """Covers Functional Requirements FR-06, FR-07, and FR-08."""

    def test_tc06_add_to_cart(self, authenticated_driver):
        """
        TC-06 / FR-06: Verify adding products to the shopping cart.
        Precondition: User is logged in and on inventory page.
        Steps:
            1. Click 'Add to cart' on 'Sauce Labs Backpack'.
            2. Verify cart badge displays '1'.
            3. Click 'Add to cart' on 'Sauce Labs Bike Light'.
            4. Verify cart badge displays '2'.
            5. Navigate to 'Sauce Labs Bolt T-Shirt' details page and add to cart.
            6. Verify cart badge displays '3'.
        Expected Result:
            - Cart badge updates dynamically with the exact number of selected products.
        """
        inventory_page = InventoryPage(authenticated_driver)
        assert inventory_page.get_cart_badge_count() == 0, "Cart should initially be empty."

        # Add first product from inventory
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        assert inventory_page.get_cart_badge_count() == 1, "Cart badge should be 1."

        # Add second product from inventory
        inventory_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        assert inventory_page.get_cart_badge_count() == 2, "Cart badge should be 2."

        # Add third product from product details page
        inventory_page.click_product_by_name("Sauce Labs Bolt T-Shirt")
        details_page = ProductDetailsPage(authenticated_driver)
        details_page.click_add_to_cart()
        assert details_page.get_action_button_text() == "Remove"
        assert inventory_page.get_cart_badge_count() == 3, "Cart badge should be 3."

    def test_tc07_remove_from_cart(self, authenticated_driver):
        """
        TC-07 / FR-07: Verify removing products from the shopping cart.
        Precondition: Items are added to the cart.
        Steps:
            1. Add 2 items from inventory page.
            2. Remove one item directly from the inventory page.
            3. Verify cart badge updates to 1.
            4. Open cart page and remove remaining item.
            5. Verify cart is now empty and badge disappears.
        Expected Result:
            - Cart count decrements immediately upon removal from both inventory and cart pages.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        assert inventory_page.get_cart_badge_count() == 2

        # Remove first item from inventory
        inventory_page.remove_product_from_cart_by_name("Sauce Labs Backpack")
        assert inventory_page.get_cart_badge_count() == 1

        # Navigate to cart page and remove second item
        inventory_page.click_cart_icon()
        cart_page = CartPage(authenticated_driver)
        assert cart_page.is_at_cart_page()
        assert cart_page.get_cart_item_count() == 1

        cart_page.remove_item_by_name("Sauce Labs Bike Light")
        assert cart_page.get_cart_item_count() == 0
        assert inventory_page.get_cart_badge_count() == 0

    def test_tc08_cart_review(self, authenticated_driver):
        """
        TC-08 / FR-08: Verify cart review page contents and navigation.
        Precondition: User adds items to the cart.
        Steps:
            1. Add 'Sauce Labs Backpack' ($29.99) and 'Sauce Labs Fleece Jacket' ($49.99).
            2. Click shopping cart icon.
            3. Verify item names, quantity, and individual prices.
            4. Click 'Continue Shopping'.
        Expected Result:
            - Navigated to cart.html.
            - Cart displays selected items with correct names and prices.
            - Clicking 'Continue Shopping' safely returns user to inventory.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.add_product_to_cart_by_name("Sauce Labs Fleece Jacket")

        inventory_page.click_cart_icon()
        cart_page = CartPage(authenticated_driver)
        assert cart_page.is_at_cart_page()
        assert cart_page.get_cart_item_count() == 2

        item_names = cart_page.get_cart_item_names()
        item_prices = cart_page.get_cart_item_prices()

        assert "Sauce Labs Backpack" in item_names
        assert "Sauce Labs Fleece Jacket" in item_names
        assert 29.99 in item_prices
        assert 49.99 in item_prices

        # Test continue shopping navigation
        cart_page.click_continue_shopping()
        assert inventory_page.is_at_inventory_page()
