# CST8513: Quality Assurance and Testing - Assignment III (Automation Testing)

**Course:** CST8513 - Quality Assurance and Testing (Summer 2026)  
**Target Application:** SauceDemo (Swag Labs) - https://www.saucedemo.com/  
**Authors:** Devangbhai Pandit & Meet Ahalpara  
**Professor:** Prof. Sharmista Datta  
**Institution:** Algonquin College – School of Advanced Technology  
**Presentation & Submission Date:** August 13, 2026  
**GitHub Repository:** https://github.com/MeetAhalpara/QA-Test-Automation  

---

## 1. Project Documentation, Reports & Presentation

All course deliverables, reports, and presentation slides are located in `Docs/` in both formal Microsoft formats (`.pptx`, `.docx`, `.pdf`) and Markdown source (`.md`):

1. **Presentation Slides (Mandatory Demo & Project 1, 2, 3 Synthesis - 14 Slides):**
   - PowerPoint Presentation: `Docs/Project 3 - Final Presentation - Devangbhai & Meet.pptx`
   - Markdown Source with Speaker Notes: `Docs/PRESENTATION_SLIDES.md`

2. **Deliverable 1: Automated Test Scripts (with Comments & POM Architecture)**
   - Word Document: `Docs/Project 3 - Automated Test Scripts - Devangbhai & Meet.docx`
   - PDF Document: `Docs/Project 3 - Automated Test Scripts - Devangbhai & Meet.pdf`
   - Markdown Source: `Docs/AUTOMATED_TEST_SCRIPTS.md`
   - Framework Code: `automation_selenium/` and `automation_robot/`

3. **Deliverable 2: Defects and Discrepancies Report**
   - Word Document: `Docs/Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.docx`
   - PDF Document: `Docs/Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.pdf`
   - Markdown Source: `Docs/DISCREPANCIES_REPORT.md`

4. **Deliverable 3: Final Automation Test Report**
   - Word Document: `Docs/Project 3 - Final Automation Test Report - Devangbhai & Meet.docx`
   - PDF Document: `Docs/Project 3 - Final Automation Test Report - Devangbhai & Meet.pdf`
   - Markdown Source: `Docs/FINAL_AUTOMATION_TEST_REPORT.md`

5. **User & Tester Manual:**
   - Markdown Manual: `USER_MANUAL.md`

6. **Visual Interactive Reports:**
   - Selenium Pytest Report: `reports/selenium_test_report.html`
   - Robot Framework Report: `reports/robot_logs/report.html`

---

## 2. Project Overview

This repository contains the complete automated regression testing framework for Assignment III (Phase 3: Automation Testing) in CST8513. The project transitions manual functional test cases (`TC-01` through `TC-14` mapping to requirements `FR-01` through `FR-14`) into automated test scripts using the Page Object Model (POM) design pattern.

### Key Highlights:
- **Selenium WebDriver (Python 3.11 + Pytest)** with complete Page Object Model architecture.
- **Robot Framework Test Suite** with reusable keyword abstractions and SeleniumLibrary.
- **Continuous Integration (CI/CD)** pipeline configuration for both Jenkins (`ci_cd/Jenkinsfile`) and GitHub Actions (`.github/workflows/automation-tests.yml`).
- **Comprehensive Reports**: Self-contained HTML test reports, JUnit XML artifacts, and failure screenshots.
- **100% Test Pass Rate**: All 22 Selenium test scenarios and all 14 Robot Framework test cases pass consistently.
- **89.8% Time Reduction**: Regression test execution time dropped from 18 minutes (manual) to 1 minute 50 seconds (automated).

---

## 3. Quick Start: How to Run the Live Demo

### Step 1: Activate the Virtual Environment
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

### Step 2: Live Demo Command Execution

#### A. Watch the Browser Open & Click on Screen (Mandatory Live Demo):
```powershell
python -m pytest automation_selenium/tests/ --headed -v
```

#### B. Run the Unified Test Runner (Selenium + Robot + Generates Reports):
```powershell
python run_tests.py --suite all
```

#### C. Inspect Interactive Visual HTML Reports:
Open `reports/selenium_test_report.html` or `reports/robot_logs/report.html` in Chrome.

---

## 4. Architecture & Page Object Model (POM) Structure

```
Assignment3/
├── Docs/                                       # Project documentation, deliverables, PPTX & PDFs
│   ├── Project 3 - Final Presentation - Devangbhai & Meet.pptx <-- 14 SLIDE PRESENTATION
│   ├── PRESENTATION_SLIDES.md                  <-- Presentation Source & Speaker Notes
│   ├── Project 3 - Automated Test Scripts - Devangbhai & Meet.docx  <-- DELIVERABLE 1 (Word)
│   ├── Project 3 - Automated Test Scripts - Devangbhai & Meet.pdf   <-- DELIVERABLE 1 (PDF)
│   ├── AUTOMATED_TEST_SCRIPTS.md               <-- DELIVERABLE 1 (Markdown)
│   ├── Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.docx <-- DELIVERABLE 2 (Word)
│   ├── Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.pdf  <-- DELIVERABLE 2 (PDF)
│   ├── DISCREPANCIES_REPORT.md                 <-- DELIVERABLE 2 (Markdown)
│   ├── Project 3 - Final Automation Test Report - Devangbhai & Meet.docx  <-- DELIVERABLE 3 (Word)
│   ├── Project 3 - Final Automation Test Report - Devangbhai & Meet.pdf   <-- DELIVERABLE 3 (PDF)
│   └── FINAL_AUTOMATION_TEST_REPORT.md         <-- DELIVERABLE 3 (Markdown)
│
├── automation_selenium/                        # DELIVERABLE 1: Selenium WebDriver POM Framework
│   ├── config/
│   │   └── config.py                           # App URLs, user credentials, timeouts, paths
│   ├── pages/                                  # Page Object Model (POM) Page Classes
│   │   ├── base_page.py                        # Common wrapper (waits, clicks, React sync)
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
│   └── robot_logs/                             # Robot Framework report.html & log.html
│
├── run_tests.py                                # Unified test runner CLI
├── pytest.ini                                  # Pytest configuration, CLI flags, markers
├── requirements.txt                            # Python dependencies
└── USER_MANUAL.md                              # Complete Step-by-Step User & Tester Manual
```

---

## 5. Re-generating Presentation & Reports with Python

If you make edits to `PRESENTATION_SLIDES.md` or any markdown report in `Docs/` and want to update the `.pptx`, `.docx`, and `.pdf` files, run:

```powershell
# Update PPTX presentation:
python generate_presentation_pptx.py

# Update DOCX documents:
python -c "import pypandoc; pypandoc.convert_file('Docs/AUTOMATED_TEST_SCRIPTS.md', 'docx', outputfile='Docs/Project 3 - Automated Test Scripts - Devangbhai & Meet.docx'); pypandoc.convert_file('Docs/DISCREPANCIES_REPORT.md', 'docx', outputfile='Docs/Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.docx'); pypandoc.convert_file('Docs/FINAL_AUTOMATION_TEST_REPORT.md', 'docx', outputfile='Docs/Project 3 - Final Automation Test Report - Devangbhai & Meet.docx'); print('All Word deliverables updated successfully!')"
```

---
*Created for Devangbhai Pandit & Meet Ahalpara | CST8513 Quality Assurance and Testing | Algonquin College*
