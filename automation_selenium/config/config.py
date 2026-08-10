"""
Configuration module for SauceDemo Selenium Test Automation.
Course: CST8513 - Quality Assurance and Testing (Assignment III)
Students: Devangbhai Pandit & Meet Ahalpara
"""

import os
from pathlib import Path

# Base Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent.resolve()
REPORTS_DIR = PROJECT_ROOT / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"

# Ensure output directories exist
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

# Application URLs
BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = f"{BASE_URL}inventory.html"
CART_URL = f"{BASE_URL}cart.html"
CHECKOUT_STEP_ONE_URL = f"{BASE_URL}checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = f"{BASE_URL}checkout-step-two.html"
CHECKOUT_COMPLETE_URL = f"{BASE_URL}checkout-complete.html"

# User Credentials
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
LOCKED_OUT_USERNAME = "locked_out_user"
PROBLEM_USERNAME = "problem_user"
PERF_GLITCH_USERNAME = "performance_glitch_user"
ERROR_USERNAME = "error_user"
VISUAL_USERNAME = "visual_user"

INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "wrong_password"

# Sample Checkout Data
SAMPLE_FIRST_NAME = "Meet"
SAMPLE_LAST_NAME = "Ahalpara"
SAMPLE_POSTAL_CODE = "K2G 1V8"

# Explicit Wait Timeouts (in seconds)
DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 3
LONG_TIMEOUT = 20

# Browser Execution Settings
HEADLESS = True  # Can be toggled to False for headed visual execution
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
