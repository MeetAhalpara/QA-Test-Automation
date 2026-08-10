"""
Automated Test Cases for Checkout & Order Lifecycle (TC-09, TC-10, TC-11, TC-12, TC-13).
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import pytest
from automation_selenium.config.config import (
    SAMPLE_FIRST_NAME,
    SAMPLE_LAST_NAME,
    SAMPLE_POSTAL_CODE,
)
from automation_selenium.pages.inventory_page import InventoryPage
from automation_selenium.pages.cart_page import CartPage
from automation_selenium.pages.checkout_step_one_page import CheckoutStepOnePage
from automation_selenium.pages.checkout_step_two_page import CheckoutStepTwoPage
from automation_selenium.pages.checkout_complete_page import CheckoutCompletePage


@pytest.mark.checkout
class TestCheckout:
    """Covers Functional Requirements FR-09, FR-10, FR-11, FR-12, and FR-13."""

    def test_tc09_checkout_empty_fields_validation(self, authenticated_driver):
        """
        TC-09 / FR-09: Verify required fields validation on checkout step 1.
        Precondition: Item is in cart, user is at checkout-step-one.html.
        Steps:
            1. Add item to cart and proceed to checkout.
            2. Leave all fields empty.
            3. Click 'Continue'.
        Expected Result:
            - Form submission is blocked.
            - Error banner displays 'Error: First Name is required'.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.click_cart_icon()

        cart_page = CartPage(authenticated_driver)
        cart_page.click_checkout()

        step_one = CheckoutStepOnePage(authenticated_driver)
        assert step_one.is_at_step_one_page()

        step_one.click_continue()

        assert step_one.is_error_displayed()
        assert "Error: First Name is required" in step_one.get_error_message()

    @pytest.mark.parametrize(
        "first_name, last_name, postal_code, expected_error",
        [
            ("Meet", "", "", "Error: Last Name is required"),
            ("Meet", "Ahalpara", "", "Error: Postal Code is required"),
        ],
    )
    def test_tc10_checkout_input_validation(
        self, authenticated_driver, first_name, last_name, postal_code, expected_error
    ):
        """
        TC-10 / FR-10: Verify field-by-field validation when mandatory fields are omitted.
        Precondition: Item in cart, user at checkout step 1.
        Steps:
            1. Enter partial information into checkout fields.
            2. Click 'Continue'.
        Expected Result:
            - User is blocked with a specific error message.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.click_cart_icon()

        cart_page = CartPage(authenticated_driver)
        cart_page.click_checkout()

        step_one = CheckoutStepOnePage(authenticated_driver)
        step_one.fill_information(first_name, last_name, postal_code)
        step_one.click_continue()

        assert step_one.is_error_displayed()
        assert expected_error in step_one.get_error_message()

    def test_tc11_order_overview_calculations(self, authenticated_driver):
        """
        TC-11 / FR-11: Verify items, tax calculation (8%), and total price on overview.
        Precondition: Two items added to cart ($29.99 and $15.99).
        Steps:
            1. Add 'Sauce Labs Backpack' ($29.99) and 'Sauce Labs Bolt T-Shirt' ($15.99).
            2. Navigate through Cart -> Checkout Step 1 -> Enter valid info -> Continue.
            3. On Checkout Step 2 (Overview), verify item summary, subtotal, tax, and total.
        Expected Result:
            - Subtotal = $45.98.
            - Tax = $3.68 (8% tax rounded).
            - Total = $49.66.
            - Math is strictly verified: Subtotal + Tax == Total.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.add_product_to_cart_by_name("Sauce Labs Bolt T-Shirt")
        inventory_page.click_cart_icon()

        cart_page = CartPage(authenticated_driver)
        cart_page.click_checkout()

        step_one = CheckoutStepOnePage(authenticated_driver)
        step_one.fill_information(SAMPLE_FIRST_NAME, SAMPLE_LAST_NAME, SAMPLE_POSTAL_CODE)
        step_one.click_continue()

        step_two = CheckoutStepTwoPage(authenticated_driver)
        assert step_two.is_at_step_two_page()
        assert step_two.get_item_count() == 2

        subtotal = step_two.get_subtotal_amount()
        tax = step_two.get_tax_amount()
        total = step_two.get_total_amount()

        assert subtotal == 45.98, f"Expected subtotal 45.98, got {subtotal}"
        assert tax == 3.68, f"Expected tax 3.68, got {tax}"
        assert total == 49.66, f"Expected total 49.66, got {total}"
        assert round(subtotal + tax, 2) == total, "Subtotal + Tax does not match Total."

    def test_tc12_finish_order_confirmation(self, authenticated_driver):
        """
        TC-12 / FR-12: Verify order completion and confirmation screen.
        Precondition: User is at Checkout Step 2 (Overview).
        Steps:
            1. Fill checkout info and reach Step 2.
            2. Click the 'Finish' button.
        Expected Result:
            - Redirected to checkout-complete.html.
            - Header displays 'Thank you for your order!'.
            - Pony express badge image is displayed.
            - Clicking 'Back Home' safely returns user to inventory catalog.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Onesie")
        inventory_page.click_cart_icon()

        cart_page = CartPage(authenticated_driver)
        cart_page.click_checkout()

        step_one = CheckoutStepOnePage(authenticated_driver)
        step_one.fill_information(SAMPLE_FIRST_NAME, SAMPLE_LAST_NAME, SAMPLE_POSTAL_CODE)
        step_one.click_continue()

        step_two = CheckoutStepTwoPage(authenticated_driver)
        step_two.click_finish()

        complete_page = CheckoutCompletePage(authenticated_driver)
        assert complete_page.is_at_complete_page()
        assert "Thank you for your order!" in complete_page.get_complete_header()
        assert complete_page.is_pony_image_displayed()

        # Click Back Home
        complete_page.click_back_home()
        assert inventory_page.is_at_inventory_page()

    def test_tc13_cancel_checkout_redirection(self, authenticated_driver):
        """
        TC-13 / FR-13: Verify checkout cancellation flow.
        Precondition: Item in cart.
        Steps:
            1. Go to Checkout Step 1, click 'Cancel' -> Verify returns to Cart (/cart.html).
            2. Go to Checkout Step 2, click 'Cancel' -> Verify returns to Inventory (/inventory.html).
        Expected Result:
            - Cancellation cleanly navigates user back without corrupting cart state.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        inventory_page.click_cart_icon()

        cart_page = CartPage(authenticated_driver)
        cart_page.click_checkout()

        step_one = CheckoutStepOnePage(authenticated_driver)
        # Cancel from Step 1
        step_one.click_cancel()
        assert cart_page.is_at_cart_page(), "Cancelling Step 1 should return to Cart page."

        # Proceed again to Step 2
        cart_page.click_checkout()
        step_one.fill_information(SAMPLE_FIRST_NAME, SAMPLE_LAST_NAME, SAMPLE_POSTAL_CODE)
        step_one.click_continue()

        step_two = CheckoutStepTwoPage(authenticated_driver)
        # Cancel from Step 2
        step_two.click_cancel()
        assert inventory_page.is_at_inventory_page(), "Cancelling Step 2 should return to Inventory catalog."
