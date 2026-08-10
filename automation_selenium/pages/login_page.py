"""
LoginPage module representing the authentication interface of SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage
from automation_selenium.config.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD


class LoginPage(BasePage):
    """Encapsulates locators and actions for the SauceDemo Login Page."""

    # UI Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")
    ERROR_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.error-button")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self) -> "LoginPage":
        """Navigates to the SauceDemo login page."""
        self.navigate_to(BASE_URL)
        return self

    def is_at_login_page(self) -> bool:
        """Verifies if user is currently on the login page."""
        return self.is_element_visible(self.LOGIN_BUTTON) and self.is_element_visible(self.USERNAME_INPUT)

    def enter_username(self, username: str) -> "LoginPage":
        """Types username into the username field."""
        self.enter_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        """Types password into the password field."""
        self.enter_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self) -> None:
        """Clicks the login button."""
        self.click_element(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Helper method to fill credentials and submit login form."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def login_as_standard_user(self) -> None:
        """Direct helper to login with valid standard credentials."""
        self.open()
        self.login(VALID_USERNAME, VALID_PASSWORD)

    def get_error_message(self) -> str:
        """Retrieves text of the error notification banner."""
        return self.get_element_text(self.ERROR_CONTAINER)

    def is_error_displayed(self) -> bool:
        """Checks if the error banner is visible."""
        return self.is_element_visible(self.ERROR_CONTAINER, timeout=2)
