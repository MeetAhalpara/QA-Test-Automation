"""
Base Page module implementing the Page Object Model (POM) foundation.
Provides common wrapper methods with explicit waits and React event dispatching for reliable UI interactions.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import os
import time
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from automation_selenium.config.config import DEFAULT_TIMEOUT, SCREENSHOTS_DIR


class BasePage:
    """Base class that all Page Objects inherit from."""

    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def navigate_to(self, url: str) -> None:
        """Navigates to the specified URL."""
        self.driver.get(url)

    def get_current_url(self) -> str:
        """Returns the current browser URL."""
        return self.driver.current_url

    def get_title(self) -> str:
        """Returns the current page title."""
        return self.driver.title

    def find_element(self, locator: tuple[str, str], timeout: int = None) -> WebElement:
        """Waits for an element to be present in the DOM and returns it."""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def find_visible_element(self, locator: tuple[str, str], timeout: int = None) -> WebElement:
        """Waits for an element to be visible on the page and returns it."""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator: tuple[str, str], timeout: int = None) -> list[WebElement]:
        """Waits for elements to be present in the DOM and returns the list."""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []

    def click_element(self, locator: tuple[str, str], timeout: int = None) -> None:
        """Waits until element is present and clicks it via JavaScript for seamless React compatibility."""
        element = self.find_element(locator, timeout=timeout)
        self.driver.execute_script("arguments[0].click();", element)

    def js_click(self, locator: tuple[str, str], timeout: int = None) -> None:
        """Clicks an element directly via JavaScript."""
        element = self.find_element(locator, timeout=timeout)
        self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator: tuple[str, str], text: str, clear_first: bool = True) -> None:
        """
        Enters text into an input field, ensuring React state synchronization.
        Uses React _valueTracker update and event dispatching for 100% reliable form state.
        """
        element = self.find_element(locator)
        script = """
        let input = arguments[0];
        let val = arguments[1];
        let lastValue = input.value;
        input.value = val;
        let tracker = input._valueTracker;
        if (tracker) {
            tracker.setValue(lastValue);
        }
        let inputEvent = new Event('input', { bubbles: true });
        input.dispatchEvent(inputEvent);
        let changeEvent = new Event('change', { bubbles: true });
        input.dispatchEvent(changeEvent);
        """
        self.driver.execute_script(script, element, text)

    def get_element_text(self, locator: tuple[str, str], timeout: int = None) -> str:
        """Returns the text content of an element."""
        element = self.find_element(locator, timeout=timeout)
        return element.text.strip()

    def is_element_visible(self, locator: tuple[str, str], timeout: int = 3) -> bool:
        """Checks if an element is visible within a short timeout without throwing."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def select_dropdown_by_value(self, locator: tuple[str, str], value: str) -> None:
        """Selects an option from a <select> element by its value attribute."""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)

    def select_dropdown_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        """Selects an option from a <select> element by visible text."""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def get_dropdown_selected_text(self, locator: tuple[str, str]) -> str:
        """Returns the currently selected visible text of a dropdown."""
        element = self.find_element(locator)
        select = Select(element)
        return select.first_selected_option.text.strip()

    def wait_for_url_contains(self, partial_url: str, timeout: int = None) -> bool:
        """Waits for current URL to contain a specific substring."""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_contains(partial_url))

    def take_screenshot(self, test_name: str = "screenshot") -> str:
        """Captures a PNG screenshot and saves it to the reports/screenshots directory."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(SCREENSHOTS_DIR, filename)
        self.driver.save_screenshot(filepath)
        return filepath
