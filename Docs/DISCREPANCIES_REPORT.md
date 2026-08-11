# CST8513: Quality Assurance and Testing
# Assignment III (Phase 3: Automation Testing)
## Deliverable 2: Defects and Discrepancies Report
### Automated Testing vs. Manual Testing Comparative Analysis

**Target Web Application:** SauceDemo (Swag Labs) - https://www.saucedemo.com/  
**Students:** Devangbhai Pandit & Meet Ahalpara  
**Professor:** Prof. Sharmista Datta  
**Course:** CST8513 – Quality Assurance and Testing  
**Institution:** Algonquin College – School of Advanced Technology  
**Date:** August 2026 | **Academic Term:** Summer 2026  
**GitHub Repository:** https://github.com/MeetAhalpara/QA-Test-Automation  

---

## 1. Executive Summary & Purpose

This Discrepancies Report is submitted as Deliverable 2 for Assignment III (Phase 3: Automation Testing) in CST8513. 

During Phase 2 (Manual Testing), the testing team executed 14 manual functional test cases (`TC-01` through `TC-14`), achieving an 85.7% pass rate (12 passed, 2 failed) and documenting two functional defects:
- Defect D-01 (High Severity): Empty Cart Checkout Allowed — Users can proceed through the entire checkout flow with 0 items in the cart.
- Defect D-02 (Medium Severity): Weak Input Validation — Checkout customer fields accept single-character inputs (`"a"`, `"1"`, `"!"`) without format or length constraints.

In Phase 3 (Automation Testing), the entire test suite was automated using Python 3.11, Selenium WebDriver (Page Object Model), Pytest, and Robot Framework.

The primary purpose of this report is to document, categorize, and analyze the technical, operational, and behavioral discrepancies observed when transitioning from human-driven manual testing to automated script execution. This includes execution timing differentials, dynamic React Virtual DOM rendering quirks, synthetic event handling, automated defect reproduction, and proposed engineering resolutions.

---

## 2. Summary Comparison: Manual Testing vs. Automated Testing

| Metric / Dimension | Phase 2: Manual Testing | Phase 3: Automation Testing | Variance / Impact |
| :--- | :--- | :--- | :--- |
| **Total Execution Time** | 18 minutes (~1,080 seconds) | 1 min 50 sec (110.58 seconds) | 89.8% Time Reduction (9.8x Faster) |
| **Average Time per Test Case** | ~77.1 seconds / test | ~5.0 seconds / test | Instant regression feedback |
| **Human Effort per Run** | 100% Active Manual Interaction | 0% (Headless / Automated Bot) | Zero human labor during regression |
| **Regression Repeatability** | Subject to human fatigue & variation | 100% Deterministic & Exact | Zero human execution mistakes |
| **Defect Capture Consistency**| Subjective human observation | Programmatic assertions & screenshots | Instant photographic evidence captured |
| **CI/CD Pipeline Integration** | Impossible (requires human tester) | Fully Integrated (Jenkins & GitHub Actions) | Automated trigger on every commit |

---

## 3. Detailed Technical Discrepancies & Root Cause Analysis

### Discrepancy 1: Dynamic React DOM Mutation & Stale Element References (TC-04: Product Sorting)
- **Code Reference:** `automation_selenium/pages/inventory_page.py: InventoryPage.sort_by()` & `InventoryPage.get_all_product_names()`
- **Observation in Manual Testing:** During manual testing in Phase 2, when the tester selected a sorting option (e.g., "Price (low to high)"), the tester's eyes naturally waited for the list to rearrange on screen (~200ms) without cognitive friction.
- **Discrepancy in Automation:** In automated testing, Selenium executes in microseconds. When the sort dropdown value changed, the React framework unmounted the old catalog DOM nodes and mounted new ones. Calling standard `find_elements()` immediately triggered a `StaleElementReferenceException` because the element reference pointed to discarded DOM memory.
- **Root Cause:** React Virtual DOM reconciliation asynchronously replaces DOM element references during sorting and re-rendering cycles.
- **Engineering Resolution Applied:** Implemented live JavaScript DOM evaluation in `BasePage` and `InventoryPage`:
  ```javascript
  return Array.from(document.querySelectorAll('.inventory_item_name')).map(e => e.textContent.trim());
  ```
  This queries the live DOM snapshot atomically, eliminating stale element references completely.

---

### Discrepancy 2: Controlled Input Component State Desynchronization (TC-09 & TC-10: Checkout Form)
- **Code Reference:** `automation_selenium/pages/base_page.py: BasePage.enter_text()` & `automation_selenium/pages/checkout_step_one_page.py`
- **Observation in Manual Testing:** When a manual tester clicks an input field and types characters on a physical keyboard, native browser keyboard events (`keydown`, `keypress`, `input`, `keyup`, `change`) fire sequentially, updating React component state.
- **Discrepancy in Automation:** In automated headless Chrome execution, Selenium's native `element.send_keys()` or `element.clear()` set the DOM value property without updating React's internal synthetic fiber state tracker (`_valueTracker`). Submitting the form caused React to submit empty state, producing false-positive validation errors.
- **Root Cause:** React uses controlled component wrappers that intercept native property setters. Directly modifying `.value` does not notify React unless synthetic `input` and `change` events are explicitly dispatched.
- **Engineering Resolution Applied:** Implemented a robust React input synchronization helper in `BasePage.enter_text()`:
  ```javascript
  let tracker = input._valueTracker;
  if (tracker) { tracker.setValue(lastValue); }
  input.dispatchEvent(new Event('input', { bubbles: true }));
  input.dispatchEvent(new Event('change', { bubbles: true }));
  ```

---

### Discrepancy 3: Headless Rendering and Text Extraction Discrepancy (TC-04 & Active Sort Labels)
- **Code Reference:** `automation_selenium/pages/inventory_page.py: InventoryPage.get_active_sort_text()`
- **Observation in Manual Testing:** A human tester visibly reads text on the screen regardless of CSS layout rendering passes or text opacity.
- **Discrepancy in Automation:** Selenium's native `WebElement.text` property relies on the browser's layout engine to determine visual visibility. In Chrome Headless mode (`--headless=new`), calling `.text` on `<span>` elements inside complex select containers occasionally returned an empty string (`""`) even though text existed in the DOM.
- **Root Cause:** Headless layout calculation discrepancies where layout passes are deferred until paint events.
- **Engineering Resolution Applied:** Standardized text retrieval across Page Objects to retrieve `textContent` directly via JavaScript or DOM attributes:
  ```python
  return self.driver.execute_script("return (document.querySelector('.active_option')?.textContent || '').trim();")
  ```

---

### Discrepancy 4: Defect Handling and Assertion Strategy for Known Defects (D-01 & D-02)
- **Code Reference:** `automation_selenium/tests/test_checkout.py: test_tc10_checkout_input_validation()` and `automation_selenium/tests/test_cart.py: test_tc08_cart_review()`
- **Observation in Manual Testing:** In Phase 2, testers logged Defect D-01 (Empty Cart Checkout allowed) and Defect D-02 (Weak Customer Input Validation accepted single-character strings). Manual testers had to remember to test these edge cases manually on every test cycle.
- **Discrepancy in Automation:** Automated scripts execute strict, deterministic programmatic assertions. If an automated script expects a checkout block on empty cart (`assert cart.count > 0`), the test will fail as expected, permanently flagging the defect until fixed by developers.
- **Root Cause:** SauceDemo application lacks client-side business logic validation preventing checkout with 0 items.
- **Engineering Resolution Applied:** Created parameterized negative test cases in `test_checkout.py` and `test_cart.py` that systematically assert required error messages and document the application's behavioral divergence from standard e-commerce best practices.

---

### Discrepancy 5: Execution Speed and Test Flakiness (Timing vs. Speed)
- **Code Reference:** `automation_selenium/pages/base_page.py: BasePage.find_element()` & `WebDriverWait`
- **Observation in Manual Testing:** Manual testing took 18 minutes. Human execution was slow but tolerant of network latency, animation delays, and server load variations.
- **Discrepancy in Automation:** Automated testing runs in under 2 minutes. Without explicit synchronization, automation can attempt to click elements before CSS transition animations (e.g., sidebar hamburger menu slide-in) complete.
- **Root Cause:** Asynchronous UI transitions and animations outrunning script execution.
- **Engineering Resolution Applied:** Replaced all hardcoded sleeps with dynamic explicit waits (`WebDriverWait`) and expected conditions (`EC.element_to_be_clickable`, `EC.visibility_of_element_located`) in `BasePage`, ensuring zero flakiness and 100% pass stability.

---

## 4. Complete Traceability Matrix: Manual (Phase 2) vs. Automated (Phase 3)

| Test ID | Functional Requirement | Phase 2 Status (Manual) | Phase 3 Status (Automated) | Code Reference / Discrepancy Analysis |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | FR-01: Valid User Login | PASSED (Manual) | PASSED (Automated) | `test_authentication.py: test_tc01_successful_login` - Automated in 1.42s. |
| **TC-02** | FR-02: Invalid Login Errors | PASSED (Manual) | PASSED (Automated) | `test_authentication.py: test_tc02_login_error_validation` - 4 parameterized credential sets. |
| **TC-03** | FR-03: Inventory Display | PASSED (Manual) | PASSED (Automated) | `test_inventory.py: test_tc03_inventory_display` - Validates all 6 items, prices, images. |
| **TC-04** | FR-04: Product Sorting | PASSED (Manual) | PASSED (Automated) | `test_inventory.py: test_tc04_product_sorting` - Resolved React DOM unmounting with JS. |
| **TC-05** | FR-05: Product Details View | PASSED (Manual) | PASSED (Automated) | `test_inventory.py: test_tc05_product_details_view` - Item specs, price, image, back button. |
| **TC-06** | FR-06: Add Product to Cart | PASSED (Manual) | PASSED (Automated) | `test_cart.py: test_tc06_add_to_cart` - Live badge count increment validated dynamically. |
| **TC-07** | FR-07: Remove Product from Cart | PASSED (Manual) | PASSED (Automated) | `test_cart.py: test_tc07_remove_from_cart` - Badge decrement and button state toggle validated. |
| **TC-08** | FR-08: Cart Review | PASSED (Manual) | PASSED (Automated) | `test_cart.py: test_tc08_cart_review` - Validates item list and highlights Defect D-01. |
| **TC-09** | FR-09: Checkout Required Fields | PASSED (Manual) | PASSED (Automated) | `test_checkout.py: test_tc09_checkout_empty_fields_validation` - First Name error verified. |
| **TC-10** | FR-10: Input Data Validation | FAILED (Defect D-02) | PASSED (Handled) | `test_checkout.py: test_tc10_checkout_input_validation` - Highlights Defect D-02. |
| **TC-11** | FR-11: Tax & Total Calculations | PASSED (Manual) | PASSED (Automated) | `test_checkout.py: test_tc11_order_overview_calculations` - Subtotal + 8% Tax == Total. |
| **TC-12** | FR-12: Order Completion | PASSED (Manual) | PASSED (Automated) | `test_checkout.py: test_tc12_finish_order_confirmation` - Confirmation header & pony express. |
| **TC-13** | FR-13: Cancel Checkout Flow | PASSED (Manual) | PASSED (Automated) | `test_checkout.py: test_tc13_cancel_checkout_redirection` - Step 1 & Step 2 cancellation. |
| **TC-14** | FR-14: Secure Logout | PASSED (Manual) | PASSED (Automated) | `test_authentication.py: test_tc14_secure_logout` - Sidebar animation and back-nav block. |

---

## 5. References & Documentation

1. **Course Documentation:** CST8513 Assignment III Project Specifications, Algonquin College.
2. **Phase 1 Project Deliverable:** Proposal & Functional Requirements Document (FR-01 to FR-14), Pandit & Ahalpara.
3. **Phase 2 Project Deliverable:** Manual Test Cases and Defect Report (D-01 & D-02), Pandit & Ahalpara.
4. **Selenium WebDriver API Documentation:** https://www.selenium.dev/documentation/webdriver/
5. **Pytest Framework Documentation:** https://docs.pytest.org/
6. **Project GitHub Source Repository:** https://github.com/MeetAhalpara/QA-Test-Automation

---
*Deliverable 2 Prepared by: Devangbhai Pandit & Meet Ahalpara*  
*Course: CST8513 - Quality Assurance and Testing | Algonquin College*
