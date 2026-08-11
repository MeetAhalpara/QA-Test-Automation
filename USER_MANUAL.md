# CST8513 Assignment III - Complete User & Tester Manual

**Target Application:** SauceDemo (Swag Labs) - https://www.saucedemo.com/  
**Authors:** Devangbhai Pandit & Meet Ahalpara  
**Professor:** Prof. Sharmista Datta  
**Course:** CST8513 – Quality Assurance and Testing (Summer 2026)  
**Institution:** Algonquin College – School of Advanced Technology  
**GitHub Repository:** https://github.com/MeetAhalpara/QA-Test-Automation  

---

## 1. Quick Overview for Devang

This manual walks you through setting up, running, testing, and verifying everything in this test automation repository on any computer in under 3 minutes.

### Key Components:
1. **Selenium WebDriver Test Suite (Python 3.11 + Pytest)** with Page Object Model (POM) architecture covering all 14 functional requirements (`TC-01` to `TC-14` + parameter variations + full E2E workflow).
2. **Robot Framework Test Suite** using high-level keyword abstractions and SeleniumLibrary.
3. **Automated Visual HTML & XML Reports** generated directly into `reports/`.
4. **Continuous Integration (CI/CD)** pipelines for Jenkins (`ci_cd/Jenkinsfile`) and GitHub Actions (`.github/workflows/automation-tests.yml`).
5. **All Project Documentation** and Word reports (`.docx`) in `Docs/`.

---

## 2. Fast Setup (One-Time Setup)

### Step 1: Open the Project in VS Code / Terminal
Open your terminal (PowerShell, Command Prompt, or VS Code Terminal) in the `Assignment3` folder:
```powershell
cd Assignment3
```

### Step 2: Activate the Virtual Environment
A pre-configured virtual environment (`.venv`) is already included in this repository:

- **In PowerShell (VS Code default):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(Note: If PowerShell shows an Execution Policy error, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then re-run `.\.venv\Scripts\Activate.ps1`)*

- **In Command Prompt (cmd):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

*(You will see `(.venv)` in green at the start of your terminal prompt line).*

### Step 3 (Optional if creating a new venv on another machine):
If running on a fresh computer without `.venv`:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -c "import pypandoc; pypandoc.download_pandoc()"
```

---

## 3. How to Run the Automated Tests

### Option A: Watch the Browser Open & Click on Screen (Visual Headed Mode - BEST FOR DEMOS)
To watch Google Chrome launch, type credentials, click buttons, add items to cart, and finish orders live on your screen:

```powershell
python -m pytest automation_selenium/tests/ --headed -v
```

---

### Option B: Run All Test Suites & Generate Reports with 1 Command (Unified Test Runner)
To run both the Selenium (POM) suite (22 scenarios) and the Robot Framework suite (14 scenarios) in the background and generate all reports:

```powershell
python run_tests.py --suite all
```

---

### Option C: Run a Specific Test Suite
You can run individual test files to test specific feature areas:

```powershell
# 1. Test Login, Credential Errors & Logout (TC-01, TC-02, TC-14):
python -m pytest automation_selenium/tests/test_authentication.py --headed -v

# 2. Test Catalog Display, Sorting & Product Details (TC-03, TC-04, TC-05):
python -m pytest automation_selenium/tests/test_inventory.py --headed -v

# 3. Test Add/Remove to Cart & Cart Review (TC-06, TC-07, TC-08):
python -m pytest automation_selenium/tests/test_cart.py --headed -v

# 4. Test Checkout Forms, Tax Math & Order Finish (TC-09 to TC-13):
python -m pytest automation_selenium/tests/test_checkout.py --headed -v

# 5. Test Full End-to-End User Journey (E2E):
python -m pytest automation_selenium/tests/test_e2e_workflow.py --headed -v
```

---

### Option D: Run with Category Markers
You can run tests by feature tags:
```powershell
python -m pytest automation_selenium/tests/ -m auth -v
python -m pytest automation_selenium/tests/ -m inventory -v
python -m pytest automation_selenium/tests/ -m cart -v
python -m pytest automation_selenium/tests/ -m checkout -v
python -m pytest automation_selenium/tests/ -m smoke -v
```

---

### Option E: Run the Robot Framework Test Suite
To execute the Robot Framework test suite:
```powershell
python -m robot --outputdir reports/robot_logs automation_robot/tests/saucedemo_suite.robot
```

---

## 4. How to View the Test Reports

After running the tests, open the generated HTML reports in your web browser:

1. **Selenium Pytest Interactive Visual Report:**
   - Location: `reports/selenium_test_report.html`
   - How to open: Right-click the file in VS Code and select **"Open with Default Browser"**, or paste this path into Chrome:
     `file:///path-to-your-folder/reports/selenium_test_report.html`
   - *Features:* Pass/fail pie charts, individual execution durations, system metadata, and failure screenshot links.

2. **Robot Framework Log & Report:**
   - Locations: `reports/robot_logs/report.html` and `reports/robot_logs/log.html`
   - *Features:* Step-by-step keyword execution logs and timing stats.

3. **JUnit XML Report (for CI/CD):**
   - Location: `reports/junit_selenium.xml`

---

## 5. Where to Find Everything in the Project

```
Assignment3/
├── Docs/                                       # Official assignment submissions & Word documents
│   ├── Project 3 - Automated Test Scripts - Devangbhai & Meet.docx  <-- DELIVERABLE 1 (Word)
│   ├── AUTOMATED_TEST_SCRIPTS.md               <-- DELIVERABLE 1 (Markdown source)
│   ├── Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.docx <-- DELIVERABLE 2 (Word)
│   ├── DISCREPANCIES_REPORT.md                 <-- DELIVERABLE 2 (Markdown source)
│   ├── Project 3 - Final Automation Test Report - Devangbhai & Meet.docx  <-- DELIVERABLE 3 (Word)
│   ├── FINAL_AUTOMATION_TEST_REPORT.md         <-- DELIVERABLE 3 (Markdown source)
│   ├── Assignment III.docx                     <-- Course Assignment Instructions
│   ├── Project 1 - QAQT Devangbhai & Meet.docx <-- Phase 1 Proposal
│   ├── Project 2 - Test Cases - Devangbhai & Meet.docx <-- Phase 2 Manual Test Cases
│   ├── Project 2 - DefectsReport - Devangbhai & Meet.docx <-- Phase 2 Defect Report
│   └── Project 2 - Final Test Report - Devangbhai & Meet.docx <-- Phase 2 Final Report
│
├── automation_selenium/                        # DELIVERABLE 1: Selenium WebDriver POM Framework
│   ├── config/
│   │   └── config.py                           # App URLs, timeouts, usernames, passwords
│   ├── pages/                                  # PAGE OBJECTS (Web element locators & actions)
│   │   ├── base_page.py                        # Master parent wrapper (waits, clicks, React sync)
│   │   ├── login_page.py                       # Login elements & credential actions (FR-01, FR-02)
│   │   ├── inventory_page.py                   # Product catalog, 4-way sorting, cart badge (FR-03, FR-04)
│   │   ├── product_details_page.py             # Product detail specs & back button (FR-05)
│   │   ├── cart_page.py                        # Cart item review & checkout trigger (FR-07, FR-08)
│   │   ├── checkout_step_one_page.py           # Customer info form & error banners (FR-09, FR-10)
│   │   ├── checkout_step_two_page.py           # Order overview, subtotal, 8% tax & total (FR-11)
│   │   └── checkout_complete_page.py           # Confirmation header & home navigation (FR-12, FR-13)
│   └── tests/                                  # TEST SUITES (Clean assertions only)
│       ├── conftest.py                         # Browser fixtures & screenshot hooks
│       ├── test_authentication.py              # TC-01 (Login), TC-02 (Negative logins), TC-14 (Logout)
│       ├── test_inventory.py                   # TC-03 (Display), TC-04 (Sorting), TC-05 (Details)
│       ├── test_cart.py                        # TC-06 (Add to Cart), TC-07 (Remove), TC-08 (Review)
│       ├── test_checkout.py                    # TC-09 (Blank fields), TC-10 (Rules), TC-11 (Tax Math),
│       │                                       # TC-12 (Finish Order), TC-13 (Cancel Flow)
│       └── test_e2e_workflow.py                # Full End-to-End Shopping Journey
│
├── automation_robot/                           # Robot Framework Test Suite
│   ├── resources/
│   │   ├── variables.resource                  # Variables & test data
│   │   └── common.resource                     # Reusable keywords
│   └── tests/
│       └── saucedemo_suite.robot               # Automated test cases TC-01 to TC-14
│
├── ci_cd/                                      # CI/CD Continuous Integration
│   ├── Jenkinsfile                             # Declarative Jenkins CI pipeline
│   └── .github/workflows/automation-tests.yml  # GitHub Actions CI workflow
│
├── reports/                                    # Generated Reports Directory
│   ├── selenium_test_report.html               # Visual HTML test report
│   ├── junit_selenium.xml                      # JUnit XML artifact
│   └── robot_logs/                             # Robot Framework report.html & log.html
│
├── run_tests.py                                # Single CLI test runner script
├── pytest.ini                                  # Pytest configuration & markers
├── requirements.txt                            # Python dependencies
├── USER_MANUAL.md                              # This manual file
└── README.md                                   # GitHub repository overview
```

---

## 6. How to Re-generate Word Documents (.docx) with `pypandoc`

If you make any changes to the markdown files in `Docs/` and want to update the Word documents (`.docx`), run this single command:

```powershell
python -c "import pypandoc; pypandoc.convert_file('Docs/AUTOMATED_TEST_SCRIPTS.md', 'docx', outputfile='Docs/Project 3 - Automated Test Scripts - Devangbhai & Meet.docx'); pypandoc.convert_file('Docs/DISCREPANCIES_REPORT.md', 'docx', outputfile='Docs/Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.docx'); pypandoc.convert_file('Docs/FINAL_AUTOMATION_TEST_REPORT.md', 'docx', outputfile='Docs/Project 3 - Final Automation Test Report - Devangbhai & Meet.docx'); print('All Word documents updated successfully!')"
```

---

## 7. Troubleshooting & FAQ

### Q1: I see `Execution_Policies` error when activating the `.venv` in PowerShell.
**Fix:** Run this command once in PowerShell:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then run `.\.venv\Scripts\Activate.ps1` again.

---

### Q2: Do I need to manually download or update ChromeDriver?
**Answer:** **No.** Selenium 4 features native **Selenium Manager**, which automatically detects your installed Google Chrome version and downloads the matching driver in the background silently.

---

### Q3: How do the test cases map from Project 2 (Manual) to Project 3 (Automated)?
| Test ID | Feature Area | Automated Test Function & Code Location | Automated Verification |
| :--- | :--- | :--- | :--- |
| **TC-01** | Authentication | `test_authentication.py: test_tc01_successful_login` | Valid login redirects to `/inventory.html`, catalog loads 6 products |
| **TC-02** | Authentication | `test_authentication.py: test_tc02_login_error_validation` | Error banner verified for invalid, locked, and blank credentials |
| **TC-03** | Inventory Display | `test_inventory.py: test_tc03_inventory_display` | Exactly 6 items verified with title, image, price, and descriptions |
| **TC-04** | Sorting | `test_inventory.py: test_tc04_product_sorting` | Validates all 4 sort options: `A-Z`, `Z-A`, `Low-High`, `High-Low` |
| **TC-05** | Product Details | `test_inventory.py: test_tc05_product_details_view` | Item page displays title, $29.99 price, image, and back button |
| **TC-06** | Shopping Cart | `test_cart.py: test_tc06_add_to_cart` | Adding items from catalog & details increments cart badge dynamically |
| **TC-07** | Shopping Cart | `test_cart.py: test_tc07_remove_from_cart` | Removing items decrements badge count and updates button state |
| **TC-08** | Cart Review | `test_cart.py: test_tc08_cart_review` | Navigating to `/cart.html` verifies item list, pricing, and continue shopping |
| **TC-09** | Checkout Info | `test_checkout.py: test_tc09_checkout_empty_fields_validation` | Submitting empty form blocks checkout with "First Name is required" |
| **TC-10** | Input Validation | `test_checkout.py: test_tc10_checkout_input_validation` | Missing last name & postal code triggers specific error messages |
| **TC-11** | Order Overview | `test_checkout.py: test_tc11_order_overview_calculations` | Verifies Subtotal ($45.98) + Tax ($3.68) == Total ($49.66) strictly |
| **TC-12** | Order Complete | `test_checkout.py: test_tc12_finish_order_confirmation` | Order confirmed with "Thank you for your order!" and pony express badge |
| **TC-13** | Checkout Cancel | `test_checkout.py: test_tc13_cancel_checkout_redirection` | Cancelling from Step 1 returns to Cart; Step 2 returns to Inventory |
| **TC-14** | User Logout | `test_authentication.py: test_tc14_secure_logout` | Sidebar logout ends session and blocks direct inventory URL access |
| **E2E** | Full Flow | `test_e2e_workflow.py: test_complete_e2e_shopping_workflow` | Login -> Sort -> Add 3 Items -> Cart -> Checkout -> Overview -> Finish -> Logout |

---
*Created for Devangbhai Pandit & Meet Ahalpara | CST8513 Quality Assurance and Testing | Algonquin College*
