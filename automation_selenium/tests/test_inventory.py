"""
Automated Test Cases for Product Inventory & Catalog (TC-03, TC-04, TC-05).
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import pytest
from automation_selenium.pages.inventory_page import InventoryPage
from automation_selenium.pages.product_details_page import ProductDetailsPage


@pytest.mark.inventory
class TestInventory:
    """Covers Functional Requirements FR-03, FR-04, and FR-05."""

    def test_tc03_inventory_display(self, authenticated_driver):
        """
        TC-03 / FR-03: Verify product inventory display.
        Precondition: User is logged in.
        Steps:
            1. Observe inventory grid on page load.
        Expected Result:
            - Exactly 6 items are displayed in the catalog.
            - Each item has a non-empty name, positive price, description, and visible image.
        """
        inventory_page = InventoryPage(authenticated_driver)
        assert inventory_page.get_product_count() == 6, "Expected 6 items in catalog."

        names = inventory_page.get_all_product_names()
        prices = inventory_page.get_all_product_prices()

        assert len(names) == 6, "Missing product names."
        assert len(prices) == 6, "Missing product prices."
        assert all(p > 0 for p in prices), "All product prices must be greater than zero."
        assert "Sauce Labs Backpack" in names, "Expected 'Sauce Labs Backpack' to be present."
        assert "Sauce Labs Fleece Jacket" in names, "Expected 'Sauce Labs Fleece Jacket' to be present."

    @pytest.mark.parametrize(
        "sort_value, sort_label, check_type",
        [
            ("az", "Name (A to Z)", "name_asc"),
            ("za", "Name (Z to A)", "name_desc"),
            ("lohi", "Price (low to high)", "price_asc"),
            ("hilo", "Price (high to low)", "price_desc"),
        ],
    )
    def test_tc04_product_sorting(self, authenticated_driver, sort_value, sort_label, check_type):
        """
        TC-04 / FR-04: Verify sorting functionality for all 4 options.
        Precondition: User is on the inventory page.
        Steps:
            1. Select sort option from dropdown.
        Expected Result:
            - Active sort label updates.
            - Products are re-ordered according to the selected criterion.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.sort_by(sort_value)

        assert inventory_page.get_active_sort_text() == sort_label

        if check_type == "name_asc":
            names = inventory_page.get_all_product_names()
            assert names == sorted(names), "Products are not sorted alphabetically (A to Z)."
        elif check_type == "name_desc":
            names = inventory_page.get_all_product_names()
            assert names == sorted(names, reverse=True), "Products are not sorted reverse alphabetically (Z to A)."
        elif check_type == "price_asc":
            prices = inventory_page.get_all_product_prices()
            assert prices == sorted(prices), "Products are not sorted by price low to high."
        elif check_type == "price_desc":
            prices = inventory_page.get_all_product_prices()
            assert prices == sorted(prices, reverse=True), "Products are not sorted by price high to low."

    def test_tc05_product_details_view(self, authenticated_driver):
        """
        TC-05 / FR-05: Verify product details page content and navigation.
        Precondition: User is on the inventory page.
        Steps:
            1. Click on a product name link ('Sauce Labs Backpack').
            2. Verify details page content (name, price, description, image).
            3. Click 'Back to products'.
        Expected Result:
            - Navigated to inventory-item.html.
            - Product name, price ($29.99), description, and image are clearly visible.
            - Clicking back returns user to the inventory catalog.
        """
        inventory_page = InventoryPage(authenticated_driver)
        target_item = "Sauce Labs Backpack"
        inventory_page.click_product_by_name(target_item)

        details_page = ProductDetailsPage(authenticated_driver)
        assert details_page.is_at_details_page(), "Expected navigation to product details page."
        assert details_page.get_product_name() == target_item
        assert details_page.get_product_price() == 29.99
        assert len(details_page.get_product_description()) > 10, "Product description is missing or too short."
        assert details_page.is_product_image_displayed(), "Product details image is not displayed."

        # Return to products
        details_page.click_back_to_products()
        assert inventory_page.is_at_inventory_page(), "Failed to navigate back to inventory catalog."
