# CST8513: Quality Assurance and Testing - Assignment III (Automation Testing)

**Course:** CST8513 - Quality Assurance and Testing (Summer 2026)  
**Target Application:** [SauceDemo (Swag Labs)](https://www.saucedemo.com/)  
**Authors:** Devangbhai Pandit & Meet Ahalpara  
**Professor:** Prof. Sharmista Datta  
**Institution:** Algonquin College – School of Advanced Technology  

---

## 🚀 Quick Links & User Guide
- 📖 **[Comprehensive User & Tester Manual](USER_MANUAL.md)** *(Step-by-step testing guide for Devang and the team)*
- 📄 **[Deliverable 3: Final Automation Test Report (DOCX)](Docs/Project%203%20-%20Final%20Automation%20Test%20Report%20-%20Devangbhai%20%26%20Meet.docx)** | **[(Markdown)](Docs/FINAL_AUTOMATION_TEST_REPORT.md)**
- 📄 **[Deliverable 2: Defects & Discrepancies Report (DOCX)](Docs/Project%203%20-%20Defects%20and%20Discrepancies%20Report%20-%20Devangbhai%20%26%20Meet.docx)** | **[(Markdown)](Docs/DISCREPANCIES_REPORT.md)**
- 🌐 **[Interactive Selenium HTML Report](reports/selenium_test_report.html)**
- 🌐 **[Robot Framework HTML Report](reports/robot_logs/report.html)**
- 📝 **[Project Notes & Q&A](NOTES.txt)**

---

## 📌 Project Overview

This repository contains the complete automated regression testing framework for **Assignment III (Phase 3: Automation Testing)** of the CST8513 Quality Assurance and Testing course. The project transitions manual functional test cases (`TC-01` through `TC-14` mapping to requirements `FR-01` through `FR-14`) into automated test scripts using the **Page Object Model (POM)** design pattern.

### Key Highlights:
- **Selenium WebDriver (Python + Pytest)** with complete Page Object Model architecture.
- **Robot Framework Test Suite** with reusable keyword abstractions and SeleniumLibrary.
- **Continuous Integration (CI/CD)** pipeline configuration for both **Jenkins** (`ci_cd/Jenkinsfile`) and **GitHub Actions** (`.github/workflows/automation-tests.yml`).
- **Comprehensive Reports**: Self-contained HTML test reports, JUnit XML artifacts, and failure screenshots.
- **100% Test Pass Rate**: All 22 Selenium test scenarios and all 14 Robot Framework test cases pass consistently.
- **89.8% Time Reduction**: Regression test execution time dropped from 18 minutes (manual) to **1 minute 50 seconds (automated)**.

---

## ⚡ Quick Start: How to Run the Tests (Under 2 Minutes)

### 1. Activate the Virtual Environment
Open your terminal in this directory (`Assignment3`):

- **PowerShell (VS Code default):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(If you see an execution policy error, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first)*

- **Command Prompt (cmd):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

---

### 2. Run Test Commands

#### A. Watch the Browser Open & Click on Screen (Visual Headed Mode):
```powershell
python -m pytest automation_selenium/tests/ --headed -v
```

#### B. Run the Unified Test Runner (Selenium + Robot + Generates Reports):
```powershell
python run_tests.py
```

#### C. Run a Specific Test Category:
```powershell
# Authentication & Logout (TC-01, TC-02, TC-14):
python -m pytest automation_selenium/tests/test_authentication.py --headed -v

# Catalog Display & Sorting (TC-03, TC-04, TC-05):
python -m pytest automation_selenium/tests/test_inventory.py --headed -v

# Shopping Cart (TC-06, TC-07, TC-08):
python -m pytest automation_selenium/tests/test_cart.py --headed -v

# Checkout & Tax Calculations (TC-09 to TC-13):
python -m pytest automation_selenium/tests/test_checkout.py --headed -v

# Full End-to-End Shopping Journey (E2E):
python -m pytest automation_selenium/tests/test_e2e_workflow.py --headed -v
```

#### D. Run the Robot Framework Test Suite:
```powershell
python -m robot --outputdir reports/robot_logs automation_robot/tests/saucedemo_suite.robot
```

---

## 🏗️ Architecture & Page Object Model (POM) Structure

The framework strictly follows the **Page Object Model** design pattern, decoupling element locators and UI interaction logic from test assertions.

```
Assignment3/
├── Docs/                                       # Project documentation & requirements
│   ├── Project 3 - Final Automation Test Report - Devangbhai & Meet.docx  <-- DELIVERABLE 3 (Word)
│   ├── FINAL_AUTOMATION_TEST_REPORT.md         <-- DELIVERABLE 3 (Markdown source)
│   ├── Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.docx <-- DELIVERABLE 2 (Word)
│   ├── DISCREPANCIES_REPORT.md                 <-- DELIVERABLE 2 (Markdown source)
│   ├── Assignment III.docx                     <-- Course Assignment Instructions
│   ├── Project 1 - QAQT Devangbhai & Meet.docx <-- Phase 1 Proposal
│   ├── Project 2 - Test Cases - Devangbhai & Meet.docx <-- Phase 2 Manual Test Cases
│   ├── Project 2 - DefectsReport - Devangbhai & Meet.docx <-- Phase 2 Defect Report (D-01, D-02)
│   └── Project 2 - Final Test Report - Devangbhai & Meet.docx <-- Phase 2 Final Report
│
├── automation_selenium/                        # DELIVERABLE 1: Selenium WebDriver Framework (Python + Pytest)
│   ├── config/
│   │   └── config.py                           # App URLs, user credentials, timeouts, paths
│   ├── pages/                                  # Page Object Model (POM) Page Classes
│   │   ├── base_page.py                        # Common wrapper (waits, clicks, React sync, screenshots)
│   │   ├── login_page.py                       # Login interface & credential validations (FR-01, FR-02)
│   │   ├── inventory_page.py                   # Catalog grid, sorting & cart badge (FR-03, FR-04, FR-06)
│   │   ├── product_details_page.py             # Single item specifications & back navigation (FR-05)
│   │   ├── cart_page.py                        # Cart review, item removal & checkout action (FR-07, FR-08)
│   │   ├── checkout_step_one_page.py           # Customer info input & validation rules (FR-09, FR-10)
│   │   ├── checkout_step_two_page.py           # Order overview, subtotal, 8% tax & total (FR-11)
│   │   └── checkout_complete_page.py           # Confirmation screen & home redirection (FR-12, FR-13)
│   └── tests/                                  # Automated Test Cases
│       ├── conftest.py                         # Pytest fixtures (driver lifecycle, screenshot hooks)
│       ├── test_authentication.py              # TC-01, TC-02, TC-14 (Auth & Logout)
│       ├── test_inventory.py                   # TC-03, TC-04, TC-05 (Catalog & Sorting)
│       ├── test_cart.py                        # TC-06, TC-07, TC-08 (Cart Operations)
│       ├── test_checkout.py                    # TC-09 to TC-13 (Checkout & Calculations)
│       └── test_e2e_workflow.py                # Full End-to-End user purchase lifecycle
│
├── automation_robot/                           # Robot Framework Test Suite
│   ├── resources/
│   │   ├── variables.resource                  # Variables, URLs, locators, test data
│   │   └── common.resource                     # Reusable keywords and browser actions
│   └── tests/
│       └── saucedemo_suite.robot               # Automated test cases TC-01 to TC-14
│
├── ci_cd/                                      # Continuous Integration / Continuous Deployment
│   ├── Jenkinsfile                             # Declarative Jenkins CI pipeline
│   └── .github/workflows/automation-tests.yml  # GitHub Actions CI workflow
│
├── reports/                                    # Generated test artifacts & reports
│   ├── selenium_test_report.html               # Pytest HTML visual report
│   ├── junit_selenium.xml                      # JUnit XML test result format
│   ├── screenshots/                            # Failure screenshots directory
│   └── robot_logs/                             # Robot Framework report.html & log.html
│
├── run_tests.py                                # Unified test runner CLI
├── pytest.ini                                  # Pytest configuration, CLI flags, markers
├── requirements.txt                            # Python dependencies
├── NOTES.txt                                   # Detailed course and project notes
└── USER_MANUAL.md                              # Complete Step-by-Step User & Tester Manual
```

---

## 📋 Test Traceability Matrix (TC-01 through TC-14)

| Test ID | FR ID | Feature Area | Automated Test Method | Automated Verification |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | FR-01 | Authentication | `test_tc01_successful_login` | Valid login redirects to `/inventory.html`, catalog loads 6 products |
| **TC-02** | FR-02 | Authentication | `test_tc02_login_error_validation` | Error banner verified for invalid, locked, and blank credentials |
| **TC-03** | FR-03 | Inventory Display | `test_tc03_inventory_display` | Exactly 6 items verified with title, image, price, and descriptions |
| **TC-04** | FR-04 | Sorting | `test_tc04_product_sorting` | Validates all 4 sort options: `A-Z`, `Z-A`, `Low-High`, `High-Low` |
| **TC-05** | FR-05 | Product Details | `test_tc05_product_details_view` | Item page displays title, $29.99 price, image, and back button |
| **TC-06** | FR-06 | Shopping Cart | `test_tc06_add_to_cart` | Adding items from catalog & details increments cart badge dynamically |
| **TC-07** | FR-07 | Shopping Cart | `test_tc07_remove_from_cart` | Removing items decrements badge count and updates button state |
| **TC-08** | FR-08 | Cart Review | `test_tc08_cart_review` | Navigating to `/cart.html` verifies item list, pricing, and continue shopping |
| **TC-09** | FR-09 | Checkout Info | `test_tc09_checkout_empty_fields_validation` | Submitting empty form blocks checkout with "First Name is required" |
| **TC-10** | FR-10 | Input Validation | `test_tc10_checkout_input_validation` | Missing last name & postal code triggers specific error messages |
| **TC-11** | FR-11 | Order Overview | `test_tc11_order_overview_calculations` | Verifies Subtotal ($45.98) + Tax ($3.68) == Total ($49.66) strictly |
| **TC-12** | FR-12 | Order Complete | `test_tc12_finish_order_confirmation` | Order confirmed with "Thank you for your order!" and pony express badge |
| **TC-13** | FR-13 | Checkout Cancel | `test_tc13_cancel_checkout_redirection` | Cancelling from Step 1 returns to Cart; Step 2 returns to Inventory |
| **TC-14** | FR-14 | User Logout | `test_tc14_secure_logout` | Sidebar logout ends session and blocks direct inventory URL access |
| **E2E** | Full Flow | E-Commerce Journey | `test_complete_e2e_shopping_workflow` | Login -> Sort -> Add 3 Items -> Cart -> Checkout -> Overview -> Finish -> Logout |

---

## 🔄 Re-generating Word Documents (.docx) with `pypandoc`

If you make edits to the Markdown files in `Docs/` and want to update the `.docx` documents, run:
```powershell
python -c "import pypandoc; pypandoc.convert_file('Docs/FINAL_AUTOMATION_TEST_REPORT.md', 'docx', outputfile='Docs/Project 3 - Final Automation Test Report - Devangbhai & Meet.docx'); pypandoc.convert_file('Docs/DISCREPANCIES_REPORT.md', 'docx', outputfile='Docs/Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.docx'); print('Word documents updated!')"
```

---
*Created for Devangbhai Pandit & Meet Ahalpara | CST8513 Quality Assurance and Testing | Algonquin College*
