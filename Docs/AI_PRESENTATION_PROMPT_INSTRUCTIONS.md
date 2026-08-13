# Detailed Master Prompt & Instructions for AI Slide Generators
## Project: CST8513 Quality Assurance & Testing - Final Presentation (Project I, II, & III Synthesis)

**Target Use Case:** Copy and paste the prompt below into any AI Presentation Generator (Gamma AI, Beautiful.ai, ChatGPT Plus / Canvas, Claude 3.5, Tome, Canva AI, or PowerPoint Copilot) to generate a high-end presentation deck.

---

### Master AI Prompt (Copy-Paste Ready)

```text
You are an expert Presentation Design & QA Engineering AI. Generate a professional, highly readable 14-slide presentation deck based on the detailed project specifications below.

### Presentation Context & Rules:
1. Submission & Presentation Date: August 13, 2026
2. Maximum Allowed Slides: 14 Slides (Strictly under the 15 slide limit).
3. Live Demo Requirement: Slide 12 must feature a step-by-step Mandatory Live Demonstration Guide with exact terminal commands.
4. Content Scope: Concise synthesis of Project I (Requirements Analysis), Project II (Manual Testing & Defects), and Project III (Automated Testing, POM Architecture, Robot Framework, CI/CD, and Discrepancies).
5. Student Names: Devangbhai Pandit & Meet Ahalpara
6. Professor: Prof. Sharmista Datta
7. Course: CST8513 – Quality Assurance and Testing (Algonquin College – School of Advanced Technology)
8. Target Application: SauceDemo (Swag Labs e-commerce) - https://www.saucedemo.com/
9. Design Style: Clean academic / enterprise QA theme. Palette: Navy Blue (#003366), Teal Accent (#008080), Dark Slate (#222222), and Light Gray containers (#F4F6F9). NO random emojis or clipart.

---

### SLIDE-BY-SLIDE CONTENT STRUCTURE:

#### SLIDE 1: Title Slide
- Title: SauceDemo Test Automation & Quality Assurance Project
- Subtitle: Comprehensive Synthesis of Project I, Project II & Project III (Automation & CI/CD)
- Metadata: CST8513 – Quality Assurance and Testing | Prof. Sharmista Datta | August 13, 2026
- Presented By: Devangbhai Pandit & Meet Ahalpara | Algonquin College – School of Advanced Technology
- GitHub Repository: https://github.com/MeetAhalpara/QA-Test-Automation
- Speaker Notes: Good morning/afternoon Professor Datta and classmates. Today Devangbhai and I are presenting our complete Quality Assurance project for SauceDemo, covering our end-to-end journey across Phase 1 Proposal, Phase 2 Manual Testing, and Phase 3 Automated Testing.

#### SLIDE 2: Executive Summary & Project Progression
- Layout: 3 Side-by-Side Phase Cards
- Card 1 (Phase 1 Scope): Analyzed SauceDemo e-commerce architecture. Defined 14 Core Functional Requirements (FR-01 to FR-14) covering Auth, Catalog, Sorting, Cart, Checkout Math, & Logout.
- Card 2 (Phase 2 Manual Testing): Executed 14 manual test cases (TC-01 to TC-14). Achieved 85.7% Manual Pass Rate. Documented 2 Defects: D-01 (Empty Cart Checkout) & D-02 (Weak Input Rules).
- Card 3 (Phase 3 Automation & CI/CD): Automated 100% of test cases using Selenium WebDriver (Page Object Model) & Robot Framework. 100% Pass Rate (36/36 tests passing). Reduced regression time by 89.8% (18 mins to 1 min 50s). Configured Jenkins & GitHub Actions pipelines.
- Speaker Notes: This slide shows our 3-phase journey. In Phase 1 we mapped requirements, in Phase 2 we manually found defects, and in Phase 3 we turned those manual tests into a fully automated CI/CD pipeline running in under 2 minutes.

#### SLIDE 3: Project I Summary – Requirements Analysis & Scope
- Layout: 2 Column Container (FR-01 to FR-07 vs FR-08 to FR-14)
- Left Column (Auth & Catalog):
  - FR-01: Valid standard_user authentication & redirection to /inventory.html.
  - FR-02: Clear validation error messages for invalid/locked credentials.
  - FR-03: Inventory grid rendering all 6 catalog items with details.
  - FR-04: Dynamic 4-way sorting (A-Z, Z-A, Price Low-High, Price High-Low).
  - FR-05: Product details view showing specs, $29.99 price, & back navigation.
  - FR-06: Add to Cart increments shopping cart badge count.
  - FR-07: Remove from Cart decrements shopping cart badge count.
- Right Column (Cart, Checkout & Session):
  - FR-08: Shopping cart review page displaying selected items & prices.
  - FR-09: Submitting blank checkout info blocks flow with First Name error.
  - FR-10: Incomplete information input triggers specific field validation.
  - FR-11: Order overview verifies Subtotal + 8% Tax == Total calculation.
  - FR-12: Order completion renders 'Thank you for your order!' confirmation.
  - FR-13: Cancel checkout returns cleanly to cart (Step 1) or inventory (Step 2).
  - FR-14: Secure logout ends user session & blocks unauthorized URL access.
- Speaker Notes: In Project I, we thoroughly analyzed SauceDemo and established 14 functional requirements covering the end-to-end e-commerce purchasing workflow from authentication to order confirmation.

#### SLIDE 4: Project II Summary – Manual Testing Strategy
- Title: Project II Summary: Manual Functional Testing Strategy
- Bullet Points:
  - 1-to-1 Traceability Mapping: Authored 14 detailed manual test cases (TC-01 to TC-14) corresponding directly to functional requirements FR-01 to FR-14.
  - Manual Execution Scope: Interacted with Google Chrome manually to execute login flows, credential boundary validations, dropdown sorting, cart add/remove, form inputs, math tax calculations, and session logout.
  - Execution Overhead & Timing: Executing all 14 test cases manually required 18 full minutes (~1,080 seconds), averaging ~77.1 seconds per test case.
  - Manual Verification Challenges: Human execution was susceptible to timing variation, required active mental calculation for tax verification, and depended on manual observation for defect recording.
- Speaker Notes: In Project II, we manually executed all 14 test cases. While manual testing allowed us to explore the UI, it required 18 full minutes of active human interaction for a single test cycle.

#### SLIDE 5: Project II Findings – Manual Results & Defect Reporting
- Layout: 2 Defect Cards (Red Header for High, Amber Header for Medium)
- Card 1 (DEFECT D-01 - SEVERITY: HIGH):
  - Title: Empty Cart Checkout Allowed
  - Impacted Requirement: FR-08 / TC-08 / TC-09
  - Behavior Observed: SauceDemo permits users to navigate to /cart.html with 0 items and click Checkout, proceeding through customer info & overview.
  - Risk: Causes unnecessary payment processing overhead & bad user experience.
  - Manual Status: FAILED (Logged in Defect Report)
- Card 2 (DEFECT D-02 - SEVERITY: MEDIUM):
  - Title: Inadequate Input Field Validation
  - Impacted Requirement: FR-10 / TC-10
  - Behavior Observed: Checkout customer fields accept single-character inputs ('a', '1', '!') without length or postal code regex validation.
  - Risk: Potential data integrity issues in fulfillment systems.
  - Manual Status: FAILED (Logged in Defect Report)
- Speaker Notes: Manual testing uncovered 2 key application defects: D-01, where an empty cart can proceed to checkout, and D-02, where checkout forms accept single-character inputs. These formed our baseline for Phase 3 automation.

#### SLIDE 6: Project III Summary – Automation Strategy & Tech Stack
- Title: Project III Summary: Test Automation Strategy & Tech Stack
- Bullet Points:
  - Python 3.11: Primary programming language selected for high readability, rich testing ecosystem, and seamless CI/CD integration.
  - Selenium WebDriver 4.47: Core browser automation library utilizing native Selenium Manager for automatic ChromeDriver management.
  - Pytest 9.1 Test Framework: Executes test suites, handles test parameterization, fixtures, marker filtering, and CLI flags.
  - Robot Framework 7.4: Keyword-driven test suite with SeleniumLibrary providing readable business-level test scripts.
  - Pytest-HTML & JUnit XML: Generates self-contained interactive visual HTML reports and structured JUnit XML for CI pipelines.
  - Dual Execution Modes: Supports Headed mode (--headed) for visual demonstration and Headless Chrome (--headless=new) for fast CI/CD execution.
- Speaker Notes: For Project III, we selected Python, Selenium WebDriver, Pytest, and Robot Framework. This dual-framework approach gave us both code-based Page Object Model testing and business-readable keyword testing.

#### SLIDE 7: Page Object Model (POM) Architecture
- Title: Page Object Model (POM) Architecture Breakdown
- Bullet Points:
  - 1. BasePage (base_page.py): Foundation parent class containing explicit waits (WebDriverWait), safe JavaScript clicks, React event dispatching, and screenshot capture.
  - 2. Encapsulated Page Classes (pages/*.py): 7 dedicated page objects (LoginPage, InventoryPage, ProductDetailsPage, CartPage, CheckoutStepOnePage, CheckoutStepTwoPage, CheckoutCompletePage) holding locators & action methods.
  - 3. Test Suites (tests/*.py): Pure assertion test files (test_authentication.py, test_inventory.py, test_cart.py, test_checkout.py, test_e2e_workflow.py) containing zero hardcoded locators.
  - 4. Architectural Benefits: High reusability, single-point locator maintenance, dynamic synchronization, and zero code duplication across test suites.
- Speaker Notes: Our Selenium architecture follows the Page Object Model strictly. Locators are isolated inside Page classes. If an HTML ID changes tomorrow, we update one line in the Page class and zero test files break.

#### SLIDE 8: Project III Execution Results – 100% Pass Rate
- Layout: Summary Table + Bullet Container
- Table Data:
  - Selenium WebDriver (Pytest): 22 Scenarios | 22 Passed | 0 Failed | 100% Pass Rate | 110.58s
  - Robot Framework Suite: 14 Scenarios | 14 Passed | 0 Failed | 100% Pass Rate | 45.22s
  - CONSOLIDATED TOTAL: 36 Scenarios | 36 Passed | 0 Failed | 100% Pass Rate | 155.80s
- Highlights below table:
  - Full Feature Coverage: TC-01 to TC-14 automated seamlessly across login, catalog grid, 4-way sorting, cart management, checkout forms, and math calculations.
  - Mathematical Verification (TC-11): Programmatically verified floating-point math: Subtotal ($45.98) + 8% Tax ($3.68) == Total ($49.66).
  - E2E Purchase Workflow: Automated complete 13-step user purchasing journey from authentication to order finish and secure logout in 3.45 seconds.
- Speaker Notes: We automated all 14 functional test cases plus negative parameterizations and a full E2E workflow. Both our Selenium and Robot Framework test suites achieved a 100% pass rate across 36 test runs.

#### SLIDE 9: Discrepancies Analysis – Manual vs. Automated
- Title: Discrepancies Analysis: Manual vs. Automated Execution
- Bullet Points:
  - Total Execution Duration: Manual testing required 18 minutes (1,080 seconds) vs. Automation running in 1 minute 50 seconds (110.58 seconds) — an 89.8% reduction in regression time (9.8x faster).
  - Average Time per Test Case: Reduced from ~77.1 seconds manually down to ~5.0 seconds per automated test case.
  - Human Labor Savings: 100% human labor savings during regression cycles. Bot handles execution headlessly without manual interaction.
  - Repeatability & Precision: Manual testing is subject to fatigue and human error; Automation provides 100% deterministic precision and instant screenshot evidence on failure.
- Speaker Notes: Comparing manual vs automated testing shows an 89.8% time reduction. What took 18 minutes manually now runs automatically in under 2 minutes with zero human effort.

#### SLIDE 10: Technical Discrepancies & Engineering Resolutions
- Title: Technical Discrepancies & Engineering Resolutions
- Bullet Points:
  - 1. React Virtual DOM Mutation (TC-04 Sorting): React unmounts old DOM nodes during re-sorting, causing StaleElementReferenceException. Resolved by evaluating live DOM arrays atomically via JavaScript in BasePage.
  - 2. Controlled Input Component Sync (TC-09, TC-10): Headless Chrome send_keys() bypassed React internal _valueTracker state. Resolved by dispatching synthetic 'input' and 'change' events in BasePage.enter_text().
  - 3. Headless Text Extraction Discrepancy: Selenium .text returned empty string on select span elements in headless mode. Resolved by standardizing on direct textContent JavaScript extraction.
  - 4. Transition Animation Sync (TC-14): Sidebar menu slide-out caused click interception. Resolved by adding explicit WebDriverWait conditions instead of hardcoded sleeps.
- Speaker Notes: Transitioning to automation revealed technical DOM quirks. We resolved React virtual DOM stale element issues and controlled input state desynchronization using custom JavaScript helpers.

#### SLIDE 11: Continuous Integration (CI/CD) Pipelines
- Layout: 2 Columns (Jenkins vs GitHub Actions)
- Left Column (JENKINS PIPELINE - ci_cd/Jenkinsfile):
  - Declarative Multi-Stage Pipeline:
  - 1. Checkout: Pulls latest code from git repository.
  - 2. Environment Setup: Installs requirements.txt.
  - 3. Selenium Pytest Stage: Runs headless test suite & outputs JUnit XML.
  - 4. Robot Framework Stage: Runs headless Robot suite.
  - 5. Archive Artifacts: Publishes HTML reports & test results.
- Right Column (GITHUB ACTIONS - .github/workflows/):
  - Automated Push & PR Workflow:
  - Triggers automatically on code push to main/master.
  - Runs on Windows runner with Python 3.11.
  - Executes both Selenium and Robot test suites.
  - Uploads HTML test reports and failure screenshots as GitHub workflow run artifacts.
  - Verified building green on GitHub repository.
- Speaker Notes: We integrated our automation suite into both Jenkins and GitHub Actions. Every time code is pushed to GitHub, our full regression suite executes automatically and publishes test artifacts.

#### SLIDE 12: Mandatory Live Demonstration Guide
- Title: Mandatory Live Demonstration Guide
- Content Boxes:
  - Step 1: Visual Headed Execution (Watch Chrome Run Live)
    - Command: python -m pytest automation_selenium/tests/ --headed -v
    - Demonstrates: Real-time browser automation of login, sorting, cart add/remove, form input, math tax validation, and logout.
  - Step 2: Unified Test Runner Execution
    - Command: python run_tests.py --suite all
    - Demonstrates: Sequential execution of Pytest POM suite and Robot Framework suite with summary console metrics.
  - Step 3: Interactive Visual HTML Report Inspection
    - Open in Browser: reports/selenium_test_report.html & reports/robot_logs/report.html
    - Demonstrates: 100% Pass Rate charts, individual test timings, system environment metadata, and failure screenshot hooks.
- Speaker Notes: Now we will perform our mandatory live demo. First, we will run our tests in headed mode so you can watch Chrome perform actions live. Then we will show our unified runner and interactive HTML test reports.

#### SLIDE 13: Project ROI, Value Delivered & Recommendations
- Title: Project ROI, Value Delivered & Recommendations
- Bullet Points:
  - 1. Quantifiable ROI: 89.8% time savings on regression testing (reduced from 18 minutes to 1 min 50 seconds), saving significant manual QA hours per release cycle.
  - 2. Quality Assurance Guardrails: Continuous automated regression guardrails for Phase 2 defects D-01 (Empty Cart Checkout) and D-02 (Weak Input Rules).
  - 3. Future Cross-Browser Grid: Expand test execution matrix across Firefox, Edge, and Safari using Selenium Grid / Docker containers.
  - 4. Application Development Recommendations: Recommend SauceDemo development team implement client-side empty cart validation (#checkout button disable) and postal code regex format constraints.
- Speaker Notes: The ROI of our automation is clear: 9.8x faster regression testing, 100% repeatability, and immediate CI/CD feedback. We recommend SauceDemo developers fix defects D-01 and D-02 in upcoming releases.

#### SLIDE 14: Conclusion & Q&A
- Title: Conclusion & Questions
- Content:
  - Project Conclusion Summary:
    - Successfully synthesized Phase 1 (Proposal & Scope), Phase 2 (Manual Testing & Defects), and Phase 3 (Automated Testing & CI/CD).
    - Achieved 100% Pass Rate across 36 test runs using Selenium Page Object Model & Robot Framework.
    - Full CI/CD integration established with Jenkins and GitHub Actions.
  - GitHub Repository: https://github.com/MeetAhalpara/QA-Test-Automation
  - Thank you Professor Datta and class! We are happy to answer any questions.
- Speaker Notes: Thank you Professor Datta and class for your attention. All project code, documents, and reports are published on our GitHub repository. We are now happy to answer any questions!
```

---

### Recommended AI Presentation Platforms & How to Use This Prompt:

1. **Gamma.app (Gamma AI - Recommended for instant visual layout):**
   - Go to [gamma.app](https://gamma.app).
   - Click **"Create with AI"** -> **"Paste in text"**.
   - Paste the Master Prompt above. Gamma will automatically generate a widescreen presentation deck.

2. **ChatGPT / Claude 3.5 (For Marp or VBA Script generation):**
   - Paste the prompt into ChatGPT or Claude.
   - Ask: *"Generate a PowerPoint VBA script"* or *"Generate Marp Markdown slides"* to export directly into PowerPoint or PDF.

3. **PowerPoint Copilot / Canva AI:**
   - In PowerPoint with Copilot enabled, click **"Create presentation from text"** and paste the Master Prompt text.
