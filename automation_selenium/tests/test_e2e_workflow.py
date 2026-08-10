"""
End-to-End (E2E) Test Suite simulating a complete user purchasing journey.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import pytest
from automation_selenium.config.config import (
    VALID_USERNAME,
    VALID_PASSWORD,
    SAMPLE_FIRST_NAME,
    SAMPLE_LAST_NAME,
    SAMPLE_POSTAL_CODE,
)
from automation_selenium.pages.login_page import LoginPage
from automation_selenium.pages.inventory_page import InventoryPage
from automation_selenium.pages.product_details_page import ProductDetailsPage
from automation_selenium.pages.cart_page import CartPage
from automation_selenium.pages.checkout_step_one_page import CheckoutStepOnePage
from automation_selenium.pages.checkout_step_two_page import CheckoutStepTwoPage
from automation_selenium.pages.checkout_complete_page import CheckoutCompletePage


@pytest.mark.e2e
@pytest.mark.smoke
class TestEndToEndWorkflow:
    """Simulates the entire e-commerce journey from login to purchase completion and logout."""

    def test_complete_e2e_shopping_workflow(self, driver):
        """
        E2E Full Journey:
            1. Authenticate as standard_user.
            2. Sort inventory products by price (low to high).
            3. Add lowest priced item ('Sauce Labs Onesie' - $7.99) to cart.
            4. Add second item ('Sauce Labs Bike Light' - $9.99) to cart.
            5. Open details of 'Sauce Labs Backpack' ($29.99) and add to cart.
            6. Verify cart badge displays '3'.
            7. Navigate to Cart and review item count & details.
            8. Proceed to Checkout Step 1 and submit customer information.
            9. On Checkout Step 2 (Overview), verify mathematical calculations:
               - Subtotal: $47.97
               - Tax (8%): $3.84
               - Total: $51.81
            10. Click 'Finish' and verify the 'Thank you for your order!' confirmation.
            11. Return to catalog via 'Back Home'.
            12. Open sidebar menu and securely log out.
            13. Verify redirection back to the login screen.
        """
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        # Step 2: Inventory verification & Sorting
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_at_inventory_page()
        inventory_page.sort_by("lohi")
        assert inventory_page.get_active_sort_text() == "Price (low to high)"

        # Step 3 & 4: Add items from inventory
        inventory_page.add_product_to_cart_by_name("Sauce Labs Onesie")
        inventory_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        assert inventory_page.get_cart_badge_count() == 2

        # Step 5: Add item from Product Details page
        inventory_page.click_product_by_name("Sauce Labs Backpack")
        details_page = ProductDetailsPage(driver)
        assert details_page.is_at_details_page()
        details_page.click_add_to_cart()
        details_page.click_back_to_products()

        # Step 6: Verify cart count
        assert inventory_page.get_cart_badge_count() == 3

        # Step 7: Cart Review
        inventory_page.click_cart_icon()
        cart_page = CartPage(driver)
        assert cart_page.is_at_cart_page()
        assert cart_page.get_cart_item_count() == 3

        # Step 8: Checkout Step 1 (Information)
        cart_page.click_checkout()
        step_one = CheckoutStepOnePage(driver)
        assert step_one.is_at_step_one_page()
        step_one.fill_information(SAMPLE_FIRST_NAME, SAMPLE_LAST_NAME, SAMPLE_POSTAL_CODE)
        step_one.click_continue()

        # Step 9: Checkout Step 2 (Overview & Math Calculation)
        step_two = CheckoutStepTwoPage(driver)
        assert step_two.is_at_step_two_page()
        assert step_two.get_item_count() == 3

        expected_subtotal = 7.99 + 9.99 + 29.99  # 47.97
        expected_tax = 3.84                     # 8% of 47.97
        expected_total = 51.81                  # 47.97 + 3.84

        assert step_two.get_subtotal_amount() == expected_subtotal
        assert step_two.get_tax_amount() == expected_tax
        assert step_two.get_total_amount() == expected_total

        # Step 10: Complete Purchase
        step_two.click_finish()
        complete_page = CheckoutCompletePage(driver)
        assert complete_page.is_at_complete_page()
        assert "Thank you for your order!" in complete_page.get_complete_header()

        # Step 11: Return Home
        complete_page.click_back_home()
        assert inventory_page.is_at_inventory_page()
        assert inventory_page.get_cart_badge_count() == 0

        # Step 12 & 13: Logout
        inventory_page.click_logout()
        assert login_page.is_at_login_page()
