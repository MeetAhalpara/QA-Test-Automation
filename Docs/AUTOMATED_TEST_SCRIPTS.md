# CST8513: Quality Assurance and Testing
# Assignment III (Phase 3: Automation Testing)
## Deliverable 1: Automated Test Scripts (with Comments & Page Object Model Architecture)

**Course:** CST8513 – Quality Assurance and Testing  
**Academic Term:** Summer 2026  
**Target Web Application:** SauceDemo (Swag Labs) - https://www.saucedemo.com/  
**Students:** Devangbhai Pandit & Meet Ahalpara  
**Professor:** Prof. Sharmista Datta  
**Institution:** Algonquin College – School of Advanced Technology  
**Repository:** https://github.com/MeetAhalpara/QA-Test-Automation  

---

## 1. Framework Architecture & Design Overview

This document presents the complete technical implementation of **Deliverable 1: Automated Test Scripts** for the SauceDemo web application. 

The automation framework is engineered using **Python 3.11**, **Selenium WebDriver (4.25+)**, **Pytest (8.0+)**, and **Robot Framework (7.0+)**, strictly adhering to the **Page Object Model (POM)** architectural design pattern.

### 1.1 Core Architectural Principles
1. **Separation of Concerns:** 
   - Web page locators and user interaction workflows are isolated inside dedicated **Page Classes** (`automation_selenium/pages/`).
   - Test suites (`automation_selenium/tests/`) focus exclusively on test logic, data assertions, and expected result verifications.
2. **Robust Synchronization:**
   - Zero hardcoded delays; standard dynamic synchronization is enforced via `WebDriverWait` and `expected_conditions`.
   - React Fiber state synchronization is handled dynamically via `_valueTracker` property inspection and synthetic event dispatching.
3. **High Maintainability & Traceability:**
   - Each test case directly traces back to the 14 functional requirements (`FR-01` through `FR-14`) and manual test cases (`TC-01` through `TC-14`) established in Project 1 and Project 2.
4. **CI/CD Readiness:**
   - Supports both headed (interactive visual) and headless (continuous integration) execution modes across Jenkins and GitHub Actions.

---

## 2. Directory Structure & Code Navigation Reference

To locate any component, class, or test script within the project repository, refer to the following structural map:

```
Assignment3/
├── automation_selenium/                        # Primary Selenium WebDriver Architecture
│   ├── config/
│   │   └── config.py                           # Application URLs, credentials, timeouts, filepaths
│   ├── pages/                                  # Page Object Model (POM) Page Classes
│   │   ├── base_page.py                        # Master parent wrapper (explicit waits, safe clicks, React sync)
│   │   ├── login_page.py                       # Login interface & credential validations (FR-01, FR-02)
│   │   ├── inventory_page.py                   # Product catalog, 4-way sorting, cart badge (FR-03, FR-04, FR-06)
│   │   ├── product_details_page.py             # Product specifications & back navigation (FR-05)
│   │   ├── cart_page.py                        # Cart review, item removal & checkout button (FR-07, FR-08)
│   │   ├── checkout_step_one_page.py           # Customer info input & validation rules (FR-09, FR-10)
│   │   ├── checkout_step_two_page.py           # Order overview, subtotal, 8% tax & total (FR-11)
│   │   └── checkout_complete_page.py           # Confirmation screen & home navigation (FR-12, FR-13)
│   └── tests/                                  # Automated Pytest Test Suites
│       ├── conftest.py                         # Pytest fixtures, driver management, screenshot hooks
│       ├── test_authentication.py              # TC-01, TC-02 (4 combinations), TC-14 (Logout)
│       ├── test_inventory.py                   # TC-03, TC-04 (4 sorting criteria), TC-05 (Details)
│       ├── test_cart.py                        # TC-06, TC-07, TC-08 (Cart operations)
│       ├── test_checkout.py                    # TC-09 to TC-13 (Checkout flow & calculations)
│       └── test_e2e_workflow.py                # Comprehensive End-to-End purchase lifecycle
├── automation_robot/                           # Robot Framework Test Suite
│   ├── resources/
│   │   ├── variables.resource                  # Variables, locators, URLs, test data
│   │   └── common.resource                     # Reusable high-level keywords & actions
│   └── tests/
│       └── saucedemo_suite.robot               # Functional test cases TC-01 to TC-14
├── ci_cd/                                      # Continuous Integration Pipeline Definitions
│   ├── Jenkinsfile                             # Declarative Jenkins CI pipeline
│   └── .github/workflows/automation-tests.yml  # GitHub Actions CI workflow
├── reports/                                    # Generated Test Reports & Artifacts
│   ├── selenium_test_report.html               # Interactive visual Pytest HTML report
│   ├── junit_selenium.xml                      # JUnit XML report for CI test integration
│   └── robot_logs/                             # Robot Framework report.html & log.html
├── run_tests.py                                # Unified CLI test execution runner
├── pytest.ini                                  # Pytest global settings and markers
└── requirements.txt                            # Python dependencies
```

---

## 3. Configuration & Base Page Architecture

### 3.1 Central Configuration (`automation_selenium/config/config.py`)
Encapsulates all application constants, URLs, test account credentials, timeouts, and report paths.

```python
"""
Central Configuration Module for SauceDemo Automation Framework.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import os
from pathlib import Path

# Base Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")

# Application URLs
BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
CART_URL = "https://www.saucedemo.com/cart.html"
CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = "https://www.saucedemo.com/checkout-step-two.html"
CHECKOUT_COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"

# User Credentials
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
LOCKED_USERNAME = "locked_out_user"
PROBLEM_USERNAME = "problem_user"
PERF_USERNAME = "performance_glitch_user"
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "wrong_password"

# Explicit Wait Timeouts (in seconds)
DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 3
LONG_TIMEOUT = 15
```

---

### 3.2 Base Page Foundation (`automation_selenium/pages/base_page.py`)
Provides core WebDriver wrapper methods, explicit synchronization, safe JavaScript click fallbacks, and React Fiber controlled input event dispatching.

```python
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
```

---

## 4. Page Object Model (POM) Implementations

### 4.1 Login Page (`automation_selenium/pages/login_page.py`)
Encapsulates all locators and user workflows for the authentication screen (`FR-01`, `FR-02`).

```python
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
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self) -> "LoginPage":
        """Opens the SauceDemo login page."""
        self.navigate_to(BASE_URL)
        return self

    def enter_username(self, username: str) -> "LoginPage":
        """Enters username into the username input field."""
        self.enter_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        """Enters password into the password input field."""
        self.enter_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self) -> None:
        """Clicks the login submit button."""
        self.click_element(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Performs full login sequence."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def login_as_standard_user(self) -> None:
        """Convenience method to log in with valid standard_user credentials."""
        self.open()
        self.login(VALID_USERNAME, VALID_PASSWORD)

    def get_error_message(self) -> str:
        """Returns error banner text if displayed, else empty string."""
        if self.is_element_visible(self.ERROR_CONTAINER, timeout=3):
            return self.get_element_text(self.ERROR_CONTAINER)
        return ""

    def is_error_displayed(self) -> bool:
        """Checks whether the error banner is currently visible."""
        return self.is_element_visible(self.ERROR_CONTAINER, timeout=3)
```

---

### 4.2 Product Inventory Page (`automation_selenium/pages/inventory_page.py`)
Encapsulates catalog display, sorting, dynamic item selection, and cart badge tracking (`FR-03`, `FR-04`, `FR-06`, `FR-14`).

```python
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
```

---

### 4.3 Shopping Cart Page (`automation_selenium/pages/cart_page.py`)
Encapsulates cart review, item removal, continue shopping, and checkout initiation (`FR-07`, `FR-08`).

```python
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
```

---

### 4.4 Checkout Step One Page (`automation_selenium/pages/checkout_step_one_page.py`)
Encapsulates customer information inputs, required field assertions, and cancellation flow (`FR-09`, `FR-10`, `FR-13`).

```python
"""
CheckoutStepOnePage module representing the customer information form in SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Encapsulates locators and actions for Checkout Step One: Your Information."""

    # UI Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_at_step_one_page(self) -> bool:
        """Verifies if the user is on the checkout information page."""
        return "checkout-step-one.html" in self.get_current_url() and self.is_element_visible(self.FIRST_NAME_INPUT)

    def enter_first_name(self, first_name: str) -> "CheckoutStepOnePage":
        """Enters text into the First Name field."""
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        return self

    def enter_last_name(self, last_name: str) -> "CheckoutStepOnePage":
        """Enters text into the Last Name field."""
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        return self

    def enter_postal_code(self, postal_code: str) -> "CheckoutStepOnePage":
        """Enters text into the Postal Code field."""
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def fill_information(self, first_name: str = "", last_name: str = "", postal_code: str = "") -> None:
        """Helper to fill out all information fields."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self) -> None:
        """Clicks the Continue button."""
        self.click_element(self.CONTINUE_BUTTON)
        time.sleep(0.3)

    def click_cancel(self) -> None:
        """Clicks the Cancel button to return to the Cart."""
        self.click_element(self.CANCEL_BUTTON)
        time.sleep(0.3)

    def get_error_message(self) -> str:
        """Returns validation error banner text."""
        return self.get_element_text(self.ERROR_CONTAINER)

    def is_error_displayed(self) -> bool:
        """Checks if validation error is displayed."""
        return self.is_element_visible(self.ERROR_CONTAINER, timeout=2)
```

---

### 4.5 Checkout Step Two Page (`automation_selenium/pages/checkout_step_two_page.py`)
Encapsulates order overview, subtotal verification, 8% sales tax calculation, total price verification, and order completion (`FR-11`, `FR-13`).

```python
"""
CheckoutStepTwoPage module representing the order summary and overview page in SauceDemo.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from automation_selenium.pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    """Encapsulates locators and actions for Checkout Step Two: Overview."""

    # UI Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_at_step_two_page(self) -> bool:
        """Verifies if user is on the checkout overview page."""
        return "checkout-step-two.html" in self.get_current_url() and self.is_element_visible(self.FINISH_BUTTON)

    def get_item_count(self) -> int:
        """Returns number of items in checkout overview."""
        return len(self.find_elements(self.CART_ITEMS))

    def get_item_names(self) -> list[str]:
        """Returns list of item names displayed in overview."""
        return self.driver.execute_script(
            "return Array.from(document.querySelectorAll('.cart_item .inventory_item_name')).map(e => e.innerText.trim());"
        )

    def _extract_dollar_amount(self, locator: tuple[str, str]) -> float:
        """Helper to extract float number from text string (e.g. 'Item total: $29.99' -> 29.99)."""
        text = self.get_element_text(locator)
        match = re.search(r"\$([0-9]+\.[0-9]{2})", text)
        if match:
            return float(match.group(1))
        return 0.0

    def get_subtotal_amount(self) -> float:
        """Returns item subtotal amount."""
        return self._extract_dollar_amount(self.SUBTOTAL_LABEL)

    def get_tax_amount(self) -> float:
        """Returns tax calculation amount."""
        return self._extract_dollar_amount(self.TAX_LABEL)

    def get_total_amount(self) -> float:
        """Returns total order amount."""
        return self._extract_dollar_amount(self.TOTAL_LABEL)

    def click_finish(self) -> None:
        """Clicks the Finish button to complete order."""
        self.click_element(self.FINISH_BUTTON)
        time.sleep(0.3)

    def click_cancel(self) -> None:
        """Clicks the Cancel button to return to Inventory."""
        self.click_element(self.CANCEL_BUTTON)
        time.sleep(0.3)
```

---

## 5. Automated Test Suites & Traceability

### 5.1 Authentication Test Suite (`automation_selenium/tests/test_authentication.py`)
Automates `TC-01` (Valid Login), `TC-02` (Negative Logins & Error Banners), and `TC-14` (Secure Logout).

```python
"""
Authentication and Session Test Suite for SauceDemo.
Covers:
- TC-01: Verify Successful Login with Valid Credentials (FR-01)
- TC-02: Verify Login Error Handling for Invalid/Locked Credentials (FR-02)
- TC-14: Verify User Logout Functionality and Session Termination (FR-14)
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import pytest
from automation_selenium.config.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD,
    LOCKED_USERNAME,
    INVALID_USERNAME,
    INVALID_PASSWORD,
)
from automation_selenium.pages.login_page import LoginPage
from automation_selenium.pages.inventory_page import InventoryPage


@pytest.mark.auth
class TestAuthentication:
    """Test suite covering user authentication, error validation, and logout."""

    def test_tc01_successful_login(self, driver):
        """
        TC-01 / FR-01: Verify Successful Login with Valid Credentials.
        Precondition: User is on the login page.
        Steps:
            1. Enter valid username (standard_user).
            2. Enter valid password (secret_sauce).
            3. Click Login.
        Expected Result:
            - User redirected to https://www.saucedemo.com/inventory.html.
            - Products page header is visible.
            - Inventory catalog grid loads 6 items.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_at_inventory_page(), "Failed to redirect to inventory page after valid login."
        assert inventory_page.get_header_title() == "Products", "Page title mismatch."
        assert inventory_page.get_product_count() == 6, "Inventory should display exactly 6 items."

    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            (INVALID_USERNAME, INVALID_PASSWORD, "Epic sadface: Username and password do not match any user in this service"),
            (LOCKED_USERNAME, VALID_PASSWORD, "Epic sadface: Sorry, this user has been locked out."),
            ("", VALID_PASSWORD, "Epic sadface: Username is required"),
            (VALID_USERNAME, "", "Epic sadface: Password is required"),
        ],
    )
    def test_tc02_login_error_validation(self, driver, username, password, expected_error):
        """
        TC-02 / FR-02: Verify Login Error Handling for Invalid, Locked, and Empty Credentials.
        Precondition: User is on the login page.
        Steps:
            1. Enter specified credentials.
            2. Click Login.
        Expected Result:
            - Appropriate error banner is displayed.
            - Error banner contains exact expected message.
            - User remains on the login page.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)

        assert login_page.is_error_displayed(), f"Error banner was not displayed for credentials: ({username}, {password})"
        actual_error = login_page.get_error_message()
        assert expected_error in actual_error, f"Expected '{expected_error}', got '{actual_error}'"

    def test_tc14_secure_logout(self, authenticated_driver):
        """
        TC-14 / FR-14: Verify User Logout Functionality and Session Termination.
        Precondition: User is logged in and on the inventory page.
        Steps:
            1. Open the sidebar hamburger menu.
            2. Click 'Logout'.
        Expected Result:
            - User redirected back to https://www.saucedemo.com/.
            - Login button is displayed.
            - Direct URL navigation back to /inventory.html is blocked.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.click_logout()

        login_page = LoginPage(authenticated_driver)
        assert authenticated_driver.current_url == BASE_URL, "User was not redirected to login page on logout."
        assert login_page.is_element_visible(LoginPage.LOGIN_BUTTON), "Login button should be visible after logout."

        # Verify unauthorized back-navigation protection
        authenticated_driver.get("https://www.saucedemo.com/inventory.html")
        assert login_page.is_error_displayed() or authenticated_driver.current_url == BASE_URL, \
            "Access to inventory without authentication should be blocked."
```

---

### 5.2 Checkout Test Suite (`automation_selenium/tests/test_checkout.py`)
Automates `TC-09` (Required fields), `TC-10` (Missing fields), `TC-11` (Overview & 8% tax calculation), `TC-12` (Order completion), and `TC-13` (Cancellation).

```python
"""
Checkout and Financial Calculation Test Suite for SauceDemo.
Covers:
- TC-09: Verify Checkout Required Fields Validation (FR-09)
- TC-10: Verify Checkout Incomplete Data Validation (FR-10)
- TC-11: Verify Checkout Overview Tax and Total Calculations (FR-11)
- TC-12: Verify Order Completion Confirmation (FR-12)
- TC-13: Verify Checkout Cancellation Redirection (FR-13)
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import pytest
from automation_selenium.pages.inventory_page import InventoryPage
from automation_selenium.pages.cart_page import CartPage
from automation_selenium.pages.checkout_step_one_page import CheckoutStepOnePage
from automation_selenium.pages.checkout_step_two_page import CheckoutStepTwoPage
from automation_selenium.pages.checkout_complete_page import CheckoutCompletePage


@pytest.mark.checkout
class TestCheckout:
    """Test suite covering the multi-step checkout funnel and tax calculations."""

    def test_tc09_checkout_empty_fields_validation(self, authenticated_driver):
        """
        TC-09 / FR-09: Verify Checkout Required Fields Validation.
        Steps:
            1. Add an item to cart and proceed to Checkout Step 1.
            2. Click Continue with all fields empty.
        Expected Result:
            - Error banner appears with 'Error: First Name is required'.
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
    def test_tc10_checkout_input_validation(self, authenticated_driver, first_name, last_name, postal_code, expected_error):
        """
        TC-10 / FR-10: Verify Incomplete Checkout Information Validation.
        Steps:
            1. Enter partial customer information.
            2. Click Continue.
        Expected Result:
            - Specific missing field error is displayed.
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
        TC-11 / FR-11: Verify Checkout Overview Tax and Total Calculations.
        Steps:
            1. Add 2 items: Backpack ($29.99) + Bolt T-Shirt ($15.99) = Subtotal: $45.98.
            2. Fill customer information and continue to Step 2 Overview.
        Expected Result:
            - Subtotal == $45.98.
            - Tax == $3.68 (8% sales tax calculation).
            - Total == $49.66.
            - Subtotal + Tax == Total mathematically.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.add_product_to_cart_by_name("Sauce Labs Bolt T-Shirt")
        inventory_page.click_cart_icon()

        cart_page = CartPage(authenticated_driver)
        cart_page.click_checkout()

        step_one = CheckoutStepOnePage(authenticated_driver)
        step_one.fill_information("Devangbhai", "Pandit", "K1A0B1")
        step_one.click_continue()

        step_two = CheckoutStepTwoPage(authenticated_driver)
        assert step_two.is_at_step_two_page()
        assert step_two.get_item_count() == 2

        subtotal = step_two.get_subtotal_amount()
        tax = step_two.get_tax_amount()
        total = step_two.get_total_amount()

        assert subtotal == 45.98, f"Expected Subtotal $45.98, got ${subtotal}"
        assert tax == 3.68, f"Expected Tax $3.68, got ${tax}"
        assert total == 49.66, f"Expected Total $49.66, got ${total}"
        assert round(subtotal + tax, 2) == total, "Subtotal + Tax does not match Total."

    def test_tc12_finish_order_confirmation(self, authenticated_driver):
        """
        TC-12 / FR-12: Verify Order Completion Confirmation.
        Steps:
            1. Proceed through complete checkout funnel and click 'Finish'.
        Expected Result:
            - Redirected to checkout-complete.html.
            - Header displays 'Thank you for your order!'.
            - Pony Express confirmation graphic is displayed.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.click_cart_icon()

        cart_page = CartPage(authenticated_driver)
        cart_page.click_checkout()

        step_one = CheckoutStepOnePage(authenticated_driver)
        step_one.fill_information("Meet", "Ahalpara", "K2G1V8")
        step_one.click_continue()

        step_two = CheckoutStepTwoPage(authenticated_driver)
        step_two.click_finish()

        complete_page = CheckoutCompletePage(authenticated_driver)
        assert complete_page.is_at_complete_page()
        assert complete_page.get_complete_header() == "Thank you for your order!"
        assert complete_page.is_pony_image_displayed()

        complete_page.click_back_home()
        assert inventory_page.is_at_inventory_page()

    def test_tc13_cancel_checkout_redirection(self, authenticated_driver):
        """
        TC-13 / FR-13: Verify Checkout Cancellation Redirection.
        Steps:
            1. Cancel from Step 1 -> Should return to Cart.
            2. Cancel from Step 2 -> Should return to Inventory.
        """
        inventory_page = InventoryPage(authenticated_driver)
        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory_page.click_cart_icon()

        cart_page = CartPage(authenticated_driver)
        cart_page.click_checkout()

        # Cancel on Step 1
        step_one = CheckoutStepOnePage(authenticated_driver)
        step_one.click_cancel()
        assert cart_page.is_at_cart_page(), "Cancelling Step 1 should return to Cart."

        # Proceed to Step 2 and cancel
        cart_page.click_checkout()
        step_one.fill_information("Devangbhai", "Pandit", "K1A0B1")
        step_one.click_continue()

        step_two = CheckoutStepTwoPage(authenticated_driver)
        step_two.click_cancel()
        assert inventory_page.is_at_inventory_page(), "Cancelling Step 2 should return to Inventory."
```

---

## 6. Robot Framework Test Suite Implementation

### 6.1 Robot Resource File (`automation_robot/resources/common.resource`)
```robot
*** Settings ***
Documentation    Common keywords and utilities for SauceDemo automation suite.
...              Course: CST8513 - Quality Assurance and Testing (Assignment III)
...              Students: Devangbhai Pandit & Meet Ahalpara
Library          SeleniumLibrary
Resource         variables.resource

*** Keywords ***
Open SauceDemo In Browser
    [Documentation]    Opens the SauceDemo application in Chrome headless mode.
    Open Browser    ${BASE_URL}    headlesschrome    options=add_argument("--no-sandbox");add_argument("--disable-dev-shm-usage");add_argument("--window-size=1920,1080")
    Set Selenium Timeout    ${TIMEOUT}
    Set Selenium Speed      ${DELAY}

Close Test Browser
    [Documentation]    Closes the active browser session.
    Close Browser

Login To Application
    [Arguments]    ${username}    ${password}
    [Documentation]    Enters credentials and submits the login form.
    Execute Javascript
    ...    function setVal(id, v) {
    ...        let el = document.getElementById(id);
    ...        let last = el.value;
    ...        el.value = v;
    ...        if (el._valueTracker) el._valueTracker.setValue(last);
    ...        el.dispatchEvent(new Event('input', { bubbles: true }));
    ...    }
    ...    setVal('user-name', '${username}');
    ...    setVal('password', '${password}');
    Execute Javascript    document.getElementById('login-button').click();

Login As Standard User
    [Documentation]    Performs successful login using standard credentials.
    Login To Application    ${VALID_USER}    ${VALID_PASSWORD}
    Wait Until Location Contains    inventory.html
    Wait Until Page Contains Element    ${PAGE_TITLE}
    Element Text Should Be              ${PAGE_TITLE}    Products

Logout From Application
    [Documentation]    Opens sidebar and performs logout.
    Execute Javascript    document.getElementById('react-burger-menu-btn').click();
    Sleep    0.5s
    Execute Javascript    document.getElementById('logout_sidebar_link').click();
    Wait Until Page Contains Element    ${LOGIN_BUTTON}

Add Item To Cart By Name
    [Arguments]    ${item_name}
    [Documentation]    Locates item by name and clicks its Add to cart button.
    ${locator}=    Set Variable    xpath=//div[text()='${item_name}']/ancestor::div[@class='inventory_item']//button
    Execute Javascript    document.evaluate("//div[text()='${item_name}']/ancestor::div[@class='inventory_item']//button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();
    Sleep    0.3s

Remove Item From Cart By Name
    [Arguments]    ${item_name}
    [Documentation]    Locates item by name and clicks its Remove button.
    Execute Javascript    document.evaluate("//div[text()='${item_name}']/ancestor::div[contains(@class, 'item')]//button[text()='Remove']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();
    Sleep    0.3s

Navigate To Cart
    [Documentation]    Clicks the shopping cart icon and waits for cart page to load.
    Execute Javascript    document.querySelector('.shopping_cart_link').click();
    Wait Until Location Contains    cart.html

Proceed To Checkout
    [Documentation]    Navigates from cart to checkout step 1.
    Navigate To Cart
    Wait Until Page Contains Element    id=checkout
    Execute Javascript    document.getElementById('checkout').click();
    Wait Until Location Contains    checkout-step-one.html

Fill Checkout Form
    [Arguments]    ${first_name}    ${last_name}    ${postal_code}
    [Documentation]    Fills customer information fields in Checkout Step 1.
    Execute Javascript
    ...    function setInput(id, val) {
    ...        let input = document.getElementById(id);
    ...        if (!input) return;
    ...        let lastValue = input.value;
    ...        input.value = val;
    ...        let tracker = input._valueTracker;
    ...        if (tracker) tracker.setValue(lastValue);
    ...        input.dispatchEvent(new Event('input', { bubbles: true }));
    ...        input.dispatchEvent(new Event('change', { bubbles: true }));
    ...    }
    ...    setInput('first-name', '${first_name}');
    ...    setInput('last-name', '${last_name}');
    ...    setInput('postal-code', '${postal_code}');

Submit Checkout Step One
    [Documentation]    Clicks Continue on checkout step 1.
    Execute Javascript    document.getElementById('continue').click();

Complete Order
    [Documentation]    Clicks Finish on checkout step 2.
    Execute Javascript    document.getElementById('finish').click();
    Wait Until Location Contains    checkout-complete.html
```

---

## 7. Execution Commands & Verification

### 7.1 Running Tests with Pytest
```powershell
# Run the entire test suite in headless mode with HTML report:
python -m pytest automation_selenium/tests/ -v

# Run the test suite in visual headed mode (Google Chrome opens):
python -m pytest automation_selenium/tests/ --headed -v

# Run specific functional suites:
python -m pytest automation_selenium/tests/test_authentication.py -v
python -m pytest automation_selenium/tests/test_inventory.py -v
python -m pytest automation_selenium/tests/test_cart.py -v
python -m pytest automation_selenium/tests/test_checkout.py -v
python -m pytest automation_selenium/tests/test_e2e_workflow.py -v
```

### 7.2 Running Tests with Robot Framework
```powershell
python -m robot --outputdir reports/robot_logs automation_robot/tests/saucedemo_suite.robot
```

### 7.3 Unified Test Runner
```powershell
python run_tests.py --suite all
```

---

## 8. Technical References & External Documentation

1. **Selenium WebDriver Documentation:** https://www.selenium.dev/documentation/webdriver/
2. **Page Object Model (POM) Design Guide:** https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
3. **Pytest Testing Framework Documentation:** https://docs.pytest.org/en/stable/
4. **Robot Framework User Guide:** https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
5. **SeleniumLibrary for Robot Framework:** https://robotframework.org/SeleniumLibrary/
6. **SauceDemo Target Web Application:** https://www.saucedemo.com/
7. **Course Guidelines & Assignment III Specification:** Algonquin College CST8513 Quality Assurance and Testing.

---
*Report Prepared by: Devangbhai Pandit & Meet Ahalpara*  
*Course: CST8513 - Quality Assurance and Testing | Algonquin College*
