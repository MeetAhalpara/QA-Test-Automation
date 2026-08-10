"""
Automated Test Cases for Authentication Module (TC-01, TC-02, TC-14).
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import pytest
from automation_selenium.config.config import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    LOCKED_OUT_USERNAME,
    INVENTORY_URL,
    BASE_URL,
)
from automation_selenium.pages.login_page import LoginPage
from automation_selenium.pages.inventory_page import InventoryPage


@pytest.mark.auth
@pytest.mark.smoke
class TestAuthentication:
    """Covers Functional Requirements FR-01, FR-02, and FR-14."""

    def test_tc01_successful_login(self, driver):
        """
        TC-01 / FR-01: Verify successful login with valid credentials.
        Precondition: User is at the login page.
        Steps:
            1. Enter valid username (standard_user).
            2. Enter valid password (secret_sauce).
            3. Click the 'Login' button.
        Expected Result:
            - User is redirected to the inventory catalog (/inventory.html).
            - The header title displays 'Products'.
            - Product catalog items are displayed.
        """
        login_page = LoginPage(driver)
        login_page.open()
        assert login_page.is_at_login_page(), "Precondition failed: Not on login page."

        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_at_inventory_page(), "Expected redirection to inventory.html upon valid login."
        assert inventory_page.get_header_title() == "Products", "Header title does not match 'Products'."
        assert inventory_page.get_product_count() == 6, "Expected 6 product items to load on inventory page."

    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            (
                INVALID_USERNAME,
                INVALID_PASSWORD,
                "Epic sadface: Username and password do not match any user in this service",
            ),
            (
                LOCKED_OUT_USERNAME,
                VALID_PASSWORD,
                "Epic sadface: Sorry, this user has been locked out.",
            ),
            (
                "",
                VALID_PASSWORD,
                "Epic sadface: Username is required",
            ),
            (
                VALID_USERNAME,
                "",
                "Epic sadface: Password is required",
            ),
        ],
    )
    def test_tc02_login_error_validation(self, driver, username, password, expected_error):
        """
        TC-02 / FR-02: Verify error messaging for invalid or missing credentials.
        Precondition: User is at the login page.
        Steps:
            1. Enter invalid, locked-out, or blank credentials.
            2. Click 'Login'.
        Expected Result:
            - User remains on the login page.
            - A clear, descriptive error banner is displayed with the expected text.
        """
        login_page = LoginPage(driver)
        login_page.open()

        login_page.login(username, password)

        assert login_page.is_error_displayed(), "Error banner was expected but not displayed."
        actual_error = login_page.get_error_message()
        assert expected_error in actual_error, f"Expected error '{expected_error}', got '{actual_error}'."

    def test_tc14_secure_logout(self, authenticated_driver):
        """
        TC-14 / FR-14: Verify secure logout and session termination.
        Precondition: User is authenticated and on the inventory page.
        Steps:
            1. Open the sidebar hamburger navigation menu.
            2. Click the 'Logout' link.
            3. Attempt to access /inventory.html directly.
        Expected Result:
            - User is securely redirected to the login page (/).
            - Direct URL access to /inventory.html without active session displays authorization error.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.click_logout()

        login_page = LoginPage(authenticated_driver)
        assert login_page.is_at_login_page(), "Expected user to return to login page after logout."

        # Verify session clearance: Navigate back to inventory directly
        login_page.navigate_to(INVENTORY_URL)
        assert login_page.is_error_displayed(), "Expected access restriction error when navigating to inventory while logged out."
        assert "You can only access '/inventory.html' when you are logged in" in login_page.get_error_message()
