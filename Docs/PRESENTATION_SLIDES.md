# CST8513: Quality Assurance and Testing
## Comprehensive Project Presentation: Phase 1, Phase 2 & Phase 3 Synthesis
**Target Application:** SauceDemo (Swag Labs) - https://www.saucedemo.com/  
**Students:** Devangbhai Pandit & Meet Ahalpara  
**Professor:** Prof. Sharmista Datta  
**Course:** CST8513 – Quality Assurance and Testing  
**Institution:** Algonquin College – School of Advanced Technology  
**Presentation & Submission Date:** August 13, 2026  
**GitHub Repository:** https://github.com/MeetAhalpara/QA-Test-Automation  

---

## Slide 1: Title Slide
- **Title:** SauceDemo Test Automation & Quality Assurance Project
- **Subtitle:** Comprehensive Synthesis of Project I, Project II & Project III (Automation Testing)
- **Course:** CST8513 – Quality Assurance and Testing
- **Presented By:** Devangbhai Pandit & Meet Ahalpara
- **Submitted To:** Prof. Sharmista Datta
- **Institution:** Algonquin College, School of Advanced Technology
- **Date:** August 13, 2026
- **Speaker Notes:** "Good morning/afternoon Professor Datta and classmates. Today Devangbhai and I are presenting our complete Quality Assurance project for SauceDemo, covering our end-to-end journey across Phase 1 Proposal, Phase 2 Manual Testing, and Phase 3 Automated Testing."

---

## Slide 2: Executive Summary & Project Progression
- **Phase 1 (Requirements & Scope):** Identified e-commerce business flows and defined 14 functional requirements (FR-01 to FR-14).
- **Phase 2 (Manual Testing & Defects):** Developed 14 test cases (TC-01 to TC-14), executed manual tests achieving an 85.7% pass rate, and logged 2 functional defects (D-01 and D-02).
- **Phase 3 (Automation & CI/CD - Current):** Automated 100% of test cases using Selenium WebDriver (Page Object Model) and Robot Framework. Achieved a **100% Pass Rate (36/36 tests passing)** and reduced regression time by **89.8% (from 18 minutes to 1 min 50 sec)**.
- **Mandatory Live Demo:** Integrated command-line test runners, headed browser mode, and interactive HTML report generation.
- **Speaker Notes:** "This slide shows our 3-phase journey. In Phase 1 we mapped requirements, in Phase 2 we manually found defects, and in Phase 3 we turned those manual tests into a fully automated CI/CD pipeline running in under 2 minutes."

---

## Slide 3: Project I Summary – Requirements Analysis & Scope
- **Target Application:** SauceDemo (Swag Labs e-commerce platform by Sauce Labs).
- **14 Core Functional Requirements (FR-01 to FR-14):**
  - *Authentication:* User login (FR-01), error messaging (FR-02), secure session logout (FR-14).
  - *Catalog & Product Browsing:* Product grid display (FR-03), 4-way dynamic sorting (FR-04), detailed specifications view (FR-05).
  - *Cart Operations:* Add to cart from inventory/details (FR-06), remove from cart (FR-07), cart item review (FR-08).
  - *Checkout & Financial Calculation:* Required customer fields (FR-09), input validation rules (FR-10), Subtotal + 8% Tax == Total calculation (FR-11), order confirmation (FR-12), cancellation redirection (FR-13).
- **Speaker Notes:** "In Project I, we thoroughly analyzed SauceDemo and established 14 functional requirements covering the end-to-end e-commerce purchasing workflow from authentication to order confirmation."

---

## Slide 4: Project II Summary – Manual Testing Strategy
- **Manual Test Execution:** Executed 14 manual functional test cases (TC-01 to TC-14) in Google Chrome.
- **Traceability Mapping:** Every manual test case mapped 1-to-1 with functional requirements FR-01 through FR-14.
- **Manual Execution Duration:** Total execution time required **18 minutes (~1,080 seconds)** across all test cases (~77.1 seconds per test case).
- **Manual Verification Scope:** Manually verified text inputs, dropdown selections, cart badge counts, math tax calculations, button toggles, and URL redirections.
- **Speaker Notes:** "In Project II, we manually executed all 14 test cases. While manual testing allowed us to explore the UI, it required 18 full minutes of active human interaction for a single test cycle."

---

## Slide 5: Project II Findings – Manual Results & Defect Reporting
- **Manual Execution Results:**
  - Total Manual Test Cases: 14
  - Passed: 12 (85.7% Pass Rate)
  - Failed: 2 (14.3% Failure Rate)
- **Formally Documented Defects:**
  - **Defect D-01 (Severity: High):** *Empty Cart Checkout Allowed* — SauceDemo allows users to navigate to `/cart.html` with 0 items and proceed through the entire checkout workflow.
  - **Defect D-02 (Severity: Medium):** *Inadequate Input Field Validation* — Checkout customer information fields accept single-character inputs (`"a"`, `"1"`, `"!"`) without length or postal format validation.
- **Speaker Notes:** "Manual testing uncovered 2 key application defects: D-01, where an empty cart can proceed to checkout, and D-02, where checkout forms accept single-character inputs. These formed our baseline for Phase 3 automation."

---

## Slide 6: Project III Summary – Automation Strategy & Stack
- **Automation Tools & Frameworks:**
  - **Core Language:** Python 3.11
  - **Selenium WebDriver 4.47:** Core automation engine for web browser manipulation.
  - **Pytest 9.1:** Test runner, fixture management, parameterization, and reporting.
  - **Robot Framework 7.4:** Keyword-driven test automation suite with SeleniumLibrary.
  - **Pytest-HTML:** Self-contained interactive HTML test report generator.
- **Execution Modes:**
  - *Headed Mode:* Visible browser animation for live presentations and debugging.
  - *Headless Mode:* Background headless Chrome execution optimized for speed and CI/CD pipelines.
- **Speaker Notes:** "For Project III, we selected Python, Selenium WebDriver, Pytest, and Robot Framework. This dual-framework approach gave us both code-based Page Object Model testing and business-readable keyword testing."

---

## Slide 7: Page Object Model (POM) Architecture
- **Design Pattern Principles:** Decouples element locators and UI interaction methods from test assertions.
- **Core Architecture Layers:**
  - `BasePage` (`automation_selenium/pages/base_page.py`): Reusable parent class providing explicit waits (`WebDriverWait`), safe JavaScript clicks, React state synchronization, and screenshot capture.
  - `Page Object Classes` (`automation_selenium/pages/*.py`): 7 dedicated page classes (`LoginPage`, `InventoryPage`, `ProductDetailsPage`, `CartPage`, `CheckoutStepOnePage`, `CheckoutStepTwoPage`, `CheckoutCompletePage`).
  - `Test Suites` (`automation_selenium/tests/*.py`): Pure assertion test files containing zero hardcoded locators.
- **Key Advantage:** Single-point locator maintenance. If SauceDemo HTML changes, only 1 Page file is updated without touching test scripts.
- **Speaker Notes:** "Our Selenium architecture follows the Page Object Model strictly. Locators are isolated inside Page classes. If an HTML ID changes tomorrow, we update one line in the Page class and zero test files break."

---

## Slide 8: Project III Execution Results – 100% Pass Rate
- **Consolidated Automation Summary:**
  - **Selenium WebDriver (Pytest):** 22 Scenarios Executed | 22 Passed (100% Pass Rate) | Time: 110.58s
  - **Robot Framework:** 14 Scenarios Executed | 14 Passed (100% Pass Rate) | Time: 45.22s
  - **Total Automated Scenarios:** 36 Scenarios | **36 Passed (100% Pass Rate)**
- **Test Suite Breakdown:**
  - `test_authentication.py`: TC-01 (Valid Login), TC-02 (4 Negative Combinations), TC-14 (Logout).
  - `test_inventory.py`: TC-03 (Catalog Grid), TC-04 (4 Sort Options), TC-05 (Details View).
  - `test_cart.py`: TC-06 (Add to Cart), TC-07 (Remove from Cart), TC-08 (Cart Review).
  - `test_checkout.py`: TC-09 (Required Fields), TC-10 (Input Rules), TC-11 (Tax Calculation), TC-12 (Finish), TC-13 (Cancel).
  - `test_e2e_workflow.py`: Full 13-step End-to-End User Purchase Lifecycle.
- **Speaker Notes:** "We automated all 14 functional test cases plus negative parameterizations and a full E2E workflow. Both our Selenium and Robot Framework test suites achieved a 100% pass rate across 36 test runs."

---

## 9. Slide 9: Discrepancies Analysis – Manual vs. Automated
- **Execution Speed Comparison:**
  - Manual Testing (Phase 2): 18 minutes (~1,080 seconds).
  - Automated Testing (Phase 3): 1 minute 50 seconds (110.58 seconds).
  - **Variance:** **89.8% Time Reduction (9.8x Faster)**.
- **Comparative Analysis:**
  - *Human Labor Cost:* Manual requires human effort every run; Automation runs at 0% labor cost.
  - *Repeatability:* Manual is prone to human fatigue; Automation is 100% deterministic and exact.
  - *Defect Capture:* Manual relies on human memory; Automation provides instant assertions and failure screenshots.
  - *CI/CD Readiness:* Manual cannot integrate into CI/CD; Automation triggers automatically on code push.
- **Speaker Notes:** "Comparing manual vs automated testing shows an 89.8% time reduction. What took 18 minutes manually now runs automatically in under 2 minutes with zero human effort."

---

## Slide 10: Technical Discrepancies & Resolutions
- **Discrepancy 1: React Virtual DOM Mutation & Stale Elements (TC-04):**
  - *Issue:* Sorting triggered React DOM re-rendering, causing `StaleElementReferenceException`.
  - *Resolution:* Implemented live JavaScript DOM array evaluation in `BasePage` for atomic snapshot querying.
- **Discrepancy 2: Controlled Input Component State Sync (TC-09, TC-10):**
  - *Issue:* Native `send_keys()` in headless Chrome bypassed React internal state tracking (`_valueTracker`).
  - *Resolution:* Created React event helper dispatching synthetic `input` and `change` events in `BasePage.enter_text()`.
- **Discrepancy 3: Headless Text Extraction Discrepancy:**
  - *Issue:* Selenium `.text` returned empty string on styled select labels in headless mode.
  - *Resolution:* Standardized on direct `textContent` extraction via JavaScript.
- **Speaker Notes:** "Transitioning to automation revealed technical DOM quirks. We resolved React virtual DOM stale element issues and controlled input state desynchronization using custom JavaScript helpers."

---

## Slide 11: Continuous Integration (CI/CD) Pipelines
- **Jenkins Pipeline (`ci_cd/Jenkinsfile`):**
  - Multi-stage declarative pipeline: Checkout -> Virtualenv Setup -> Selenium Pytest Suite -> Robot Framework Suite -> Archive Reports & JUnit XML.
- **GitHub Actions Workflow (`.github/workflows/automation-tests.yml`):**
  - Automatically triggers on every `push` and `pull_request` to `main`.
  - Runs on Windows runner with Python 3.11 and headless Chrome.
  - Automatically uploads HTML reports and screenshots as workflow run artifacts.
- **Live Status:** Fully verified and building green on GitHub Actions repository (`MeetAhalpara/QA-Test-Automation`).
- **Speaker Notes:** "We integrated our automation suite into both Jenkins and GitHub Actions. Every time code is pushed to GitHub, our full regression suite executes automatically and publishes test artifacts."

---

## Slide 12: Live Demonstration Guide (Mandatory Demo)
- **Demo Step 1: Headed Visual Execution (Watch Chrome Run):**
  - Command: `python -m pytest automation_selenium/tests/ --headed -v`
  - *Action:* Launches Google Chrome live on screen, executing login, catalog sorting, cart management, checkout form submission, and tax math verification.
- **Demo Step 2: Unified Test Runner & Artifact Generation:**
  - Command: `python run_tests.py --suite all`
  - *Action:* Runs full Selenium and Robot Framework suites in background and compiles HTML reports.
- **Demo Step 3: Interactive HTML Test Report Inspection:**
  - Open `reports/selenium_test_report.html` & `reports/robot_logs/report.html` in Chrome browser.
  - *Action:* Showcase 100% Pass Rate, visual pie charts, test duration breakdown, and metadata.
- **Speaker Notes:** "Now we will perform our mandatory live demo. First, we will run our tests in headed mode so you can watch Chrome perform actions live. Then we will show our unified runner and interactive HTML test reports."

---

## Slide 13: Project ROI, Value Delivered & Recommendations
- **Business Value & ROI Delivered:**
  - **89.8% Time Savings:** Regression testing reduced from 18 mins to 110 seconds.
  - **100% Coverage & Consistency:** Eliminated human error across all 14 functional requirements.
  - **Automated Defect Guardrails:** Continuous regression guardrails for Phase 2 defects (D-01 and D-02).
- **Future Recommendations:**
  - *Cross-Browser Grid:* Expand execution to Firefox, Edge, and Safari using Docker Selenium Grid.
  - *Performance Testing:* Combine UI automation with load testing using Locust or JMeter.
  - *Form Validation Fixes:* Recommend backend validation for D-01 (Empty Cart Block) and D-02 (Input Format Constraints).
- **Speaker Notes:** "The ROI of our automation is clear: 9.8x faster regression testing, 100% repeatability, and immediate CI/CD feedback. We recommend SauceDemo developers fix defects D-01 and D-02 in upcoming releases."

---

## Slide 14: Conclusion & Q&A
- **Summary:**
  - Successfully synthesized Phase 1 requirements, Phase 2 manual testing, and Phase 3 automation.
  - Built a 100% passing Page Object Model framework in Selenium and Robot Framework.
  - Fully integrated CI/CD pipelines with interactive visual HTML reporting.
- **Academic & Technical References:**
  - CST8513 Quality Assurance & Testing Syllabus, Prof. Sharmista Datta, Algonquin College.
  - Selenium WebDriver Documentation (https://www.selenium.dev/documentation/)
  - Pytest & Robot Framework User Guides (https://docs.pytest.org/, https://robotframework.org/)
- **GitHub Project Repository:** https://github.com/MeetAhalpara/QA-Test-Automation
- **Questions & Answers:** Thank you! We welcome any questions.
- **Speaker Notes:** "Thank you Professor Datta and class for your attention. All project code, documents, and reports are published on our GitHub repository. We are now happy to answer any questions!"

---
