"""
Pytest configuration, fixtures, and hooks for the SauceDemo automation suite.
Provides WebDriver session management, headless/headed browser configuration,
automatic screenshot capture on test failure, and HTML report customization.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Ensure project root is always in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from automation_selenium.config.config import (
    BASE_URL,
    VALID_USERNAME,
    VALID_PASSWORD,
    DEFAULT_TIMEOUT,
    SCREENSHOTS_DIR,
    REPORTS_DIR,
)
from automation_selenium.pages.login_page import LoginPage


def pytest_addoption(parser):
    """Adds custom command-line options to pytest."""
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed (visible) browser mode.",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to execute tests against: chrome, firefox, edge.",
    )


@pytest.fixture(scope="session", autouse=True)
def setup_report_dirs():
    """Ensures required report and screenshot directories exist."""
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)


@pytest.fixture(scope="function")
def driver(request):
    """
    Initializes and provides a fresh Selenium WebDriver instance for each test function.
    Closes the browser cleanly during teardown.
    """
    is_headed = request.config.getoption("--headed")
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "chrome":
        chrome_options = Options()
        if not is_headed:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver_instance = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if not is_headed:
            firefox_options.add_argument("-headless")
        driver_instance = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver_instance.implicitly_wait(0)  # Using explicit waits throughout framework
    driver_instance.set_page_load_timeout(DEFAULT_TIMEOUT)

    # Attach driver to class if test is inside a class
    if request.cls is not None:
        request.cls.driver = driver_instance

    yield driver_instance

    driver_instance.quit()


@pytest.fixture(scope="function")
def authenticated_driver(driver):
    """
    Provides a WebDriver instance that is already logged into SauceDemo
    as the standard_user, located on the inventory products page.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture a screenshot automatically whenever a test fails,
    and attach it to the pytest-html report.
    """
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver") or item.funcargs.get("authenticated_driver")
        if driver_fixture:
            test_name = item.name.replace("/", "_").replace("::", "_").replace(" ", "_")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"FAILED_{test_name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)
            try:
                driver_fixture.save_screenshot(filepath)
                # Attach to HTML report
                if hasattr(pytest, "html"):
                    extra_img = pytest.html.extras.image(filepath)
                    extras.append(extra_img)
                report.extras = extras
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")


def pytest_html_report_title(report):
    """Customizes the title of the generated HTML report."""
    report.title = "SauceDemo QA Automation Report - CST8513 (Devangbhai & Meet)"
