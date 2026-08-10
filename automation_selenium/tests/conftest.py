"""
Pytest configuration and fixtures module for SauceDemo Selenium automation suite.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from automation_selenium.config.config import (
    HEADLESS,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    SCREENSHOTS_DIR,
    VALID_USERNAME,
    VALID_PASSWORD,
)
from automation_selenium.pages.login_page import LoginPage
from automation_selenium.pages.inventory_page import InventoryPage


def pytest_addoption(parser):
    """Adds custom command-line options for pytest execution."""
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser in visible (headed) mode",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Target browser: chrome, edge, firefox",
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Initializes and yields a WebDriver instance for a test.
    Automatically closes the browser session upon test completion.
    """
    headed_flag = request.config.getoption("--headed")
    is_headless = False if headed_flag else HEADLESS

    options = ChromeOptions()
    if is_headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
    options.add_argument("--disable-search-engine-choice-screen")

    driver_instance = webdriver.Chrome(options=options)
    driver_instance.maximize_window()

    yield driver_instance

    # Teardown: Quit driver session
    driver_instance.quit()


@pytest.fixture(scope="function")
def authenticated_driver(driver):
    """
    Provides a WebDriver instance that is already logged in as standard_user
    and positioned on the inventory page.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_at_inventory_page(), "Failed to authenticate and reach inventory page."
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook that captures screenshots on test failures
    and attaches them to the HTML report.
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("authenticated_driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("[", "_").replace("]", "_")
            file_name = f"FAILED_{test_name}_{timestamp}.png"
            file_path = os.path.join(SCREENSHOTS_DIR, file_name)
            driver.save_screenshot(file_path)

            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                # Add screenshot link to HTML report
                extra.append(pytest_html.extras.image(file_path))
        report.extra = extra


def pytest_html_report_title(report):
    """Sets a custom title for the generated pytest-html report."""
    report.title = "CST8513 Assignment III: SauceDemo Test Automation Report"
