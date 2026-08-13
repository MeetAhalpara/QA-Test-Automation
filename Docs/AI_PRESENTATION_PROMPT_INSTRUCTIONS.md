# Master Prompt for Gamma AI Free Plan (10 Cards / Slides Maximum)
## Project: CST8513 Quality Assurance & Testing - Final Presentation (Project I, II, & III Synthesis)

**Target Platform:** [Gamma.app](https://gamma.app) (Free Tier Optimized - Exactly 10 Cards)

---

## ⚡ Gamma AI Free Plan Setup Instructions:

1. Open **[gamma.app](https://gamma.app)**.
2. Click **"Create with AI"** -> **"Paste in text"**.
3. Set **Card Count** to **10 Cards** (Fits Gamma Free Tier limit).
4. Under **Image Settings**:
   - **Style:** `Minimalist Tech` / `3D Tech Illustration`.
   - **Model:** `FLUX` / `DALL-E 3`.
5. Paste the **10-Card Master Prompt** below and click **Generate**!

---

### 📋 10-Card Master Prompt (Copy-Paste Ready into Gamma AI)

```text
You are an expert Presentation Design & QA Engineering AI. Generate a professional, highly readable 10-card presentation deck based on the project specifications below. For each card, include the text content AND generate matching AI visuals using the provided [AI IMAGE PROMPT] tags.

### Presentation Context:
- Submission & Presentation Date: August 13, 2026
- Card Count: Exactly 10 Cards (Gamma Free Plan Optimized).
- Mandatory Demo: Card 9 features the step-by-step Live Demonstration Guide with exact terminal commands.
- Students: Devangbhai Pandit & Meet Ahalpara
- Professor: Prof. Sharmista Datta
- Course: CST8513 – Quality Assurance and Testing (Algonquin College)
- Application: SauceDemo (Swag Labs e-commerce) - https://www.saucedemo.com/
- Theme: Navy Blue (#003366), Teal Accent (#008080), Dark Slate (#222222), and Soft Gray containers (#F4F6F9). NO random clipart or emojis.

---

#### CARD 1: Title Slide
- [AI IMAGE PROMPT]: A sleek 3D render of a futuristic software quality assurance shield and laptop displaying glowing green code pass badges, navy blue background, modern tech aesthetic, 8k resolution.
- Title: SauceDemo Test Automation & Quality Assurance Project
- Subtitle: Comprehensive Synthesis of Project I, Project II & Project III (Automation & CI/CD)
- Metadata: CST8513 – Quality Assurance and Testing | Prof. Sharmista Datta | August 13, 2026
- Presented By: Devangbhai Pandit & Meet Ahalpara | Algonquin College – School of Advanced Technology
- GitHub Repository: https://github.com/MeetAhalpara/QA-Test-Automation
- Speaker Notes: Good morning/afternoon Professor Datta and classmates. Today Devangbhai and I are presenting our complete Quality Assurance project for SauceDemo, covering our end-to-end journey across Phase 1 Proposal, Phase 2 Manual Testing, and Phase 3 Automated Testing.

#### CARD 2: Executive Summary & Project Progression
- [AI IMAGE PROMPT]: A 3-step digital roadmap diagram showing software evolution from manual testing checklist to automated testing robot to cloud CI/CD server, teal and navy gradient, ultra-clean UI style.
- Card 1 (Phase 1 Scope): Analyzed SauceDemo e-commerce architecture. Defined 14 Core Functional Requirements (FR-01 to FR-14) covering Auth, Catalog, Sorting, Cart, Checkout Math, & Logout.
- Card 2 (Phase 2 Manual Testing): Executed 14 manual test cases (TC-01 to TC-14). Achieved 85.7% Manual Pass Rate. Documented 2 Defects: D-01 (Empty Cart Checkout) & D-02 (Weak Input Rules).
- Card 3 (Phase 3 Automation & CI/CD): Automated 100% of test cases using Selenium WebDriver (Page Object Model) & Robot Framework. 100% Pass Rate (36/36 tests passing). Reduced regression time by 89.8% (18 mins to 1 min 50s). Configured Jenkins & GitHub Actions pipelines.
- Speaker Notes: This slide shows our 3-phase journey. In Phase 1 we mapped requirements, in Phase 2 we manually found defects, and in Phase 3 we turned those manual tests into a fully automated CI/CD pipeline running in under 2 minutes.

#### CARD 3: Project I Summary – Requirements Scope
- [AI IMAGE PROMPT]: A modern e-commerce website interface mockup on a tablet screen showing product grid, shopping cart icon, and secure checkout badge, clean minimalist corporate style.
- Left Column (Auth & Catalog):
  - FR-01: Valid standard_user login & redirection to /inventory.html.
  - FR-02: Clear error messages for invalid/locked credentials.
  - FR-03: Inventory grid rendering all 6 products with specs.
  - FR-04: Dynamic 4-way product sorting (A-Z, Z-A, Price Lo-Hi, Hi-Lo).
  - FR-05: Product details page specs, $29.99 price, & back button.
  - FR-06: Add to Cart increments shopping cart badge count.
  - FR-07: Remove from Cart decrements shopping cart badge count.
- Right Column (Cart, Checkout & Session):
  - FR-08: Shopping cart review page displaying items & prices.
  - FR-09: Submitting blank checkout info blocks flow with First Name error.
  - FR-10: Incomplete information input triggers field validation.
  - FR-11: Order overview verifies Subtotal + 8% Tax == Total math.
  - FR-12: Order completion renders 'Thank you for your order!' header.
  - FR-13: Cancel checkout returns cleanly to cart or inventory.
  - FR-14: Secure logout ends session & blocks unauthorized URL access.
- Speaker Notes: In Project I, we thoroughly analyzed SauceDemo and established 14 functional requirements covering the end-to-end e-commerce purchasing workflow from authentication to order confirmation.

#### CARD 4: Project II Summary – Manual Testing & Defects
- [AI IMAGE PROMPT]: 3D illustration of a red bug icon and warning sign next to a digital shopping cart with zero items, dark slate background, high contrast QA defect visual.
- Manual Execution Scope: Authored and executed 14 manual test cases (TC-01 to TC-14) in Chrome. Manual execution required 18 full minutes (~1,080 seconds).
- Manual Results: 12 Passed, 2 Failed (85.7% Manual Pass Rate).
- Formally Logged Defects:
  - Defect D-01 (Severity: High): Empty Cart Checkout Allowed — Users can navigate to /cart.html with 0 items and proceed through the entire checkout flow.
  - Defect D-02 (Severity: Medium): Inadequate Input Field Validation — Checkout fields accept single-character inputs ('a', '1', '!') without format or length rules.
- Speaker Notes: Manual testing uncovered 2 key application defects: D-01, where an empty cart can proceed to checkout, and D-02, where checkout forms accept single-character inputs. These formed our baseline for Phase 3 automation.

#### CARD 5: Project III Strategy – Tech Stack & POM Architecture
- [AI IMAGE PROMPT]: A clean 3D isometric diagram showing software design pattern layers: BasePage at the bottom, Page Objects in the middle, and Test Suites at the top, navy and cyan colors.
- Technology Stack: Python 3.11, Selenium WebDriver 4.47, Pytest 9.1, Robot Framework 7.4, Pytest-HTML, and JUnit XML reporting.
- Page Object Model (POM) Layers:
  - BasePage (base_page.py): Foundation parent class containing explicit waits (WebDriverWait), safe JavaScript clicks, React event dispatching, and screenshot capture.
  - 7 Encapsulated Page Classes (pages/*.py): LoginPage, InventoryPage, ProductDetailsPage, CartPage, CheckoutStepOnePage, CheckoutStepTwoPage, CheckoutCompletePage.
  - Pure Test Suites (tests/*.py): Assertion test files containing zero hardcoded locators.
- Speaker Notes: Our Selenium architecture follows the Page Object Model strictly. Locators are isolated inside Page classes. If an HTML ID changes tomorrow, we update one line in the Page class and zero test files break.

#### CARD 6: Project III Execution Results – 100% Pass Rate
- [AI IMAGE PROMPT]: A digital dashboard display showing 100 percent pass rate green checkmarks, test summary pie charts, and 36 passed test indicators, futuristic corporate UI dashboard.
- Consolidated Execution Summary:
  - Selenium WebDriver (Pytest): 22 Scenarios Executed | 22 Passed | 0 Failed | 100% Pass Rate (110.58s)
  - Robot Framework Suite: 14 Scenarios Executed | 14 Passed | 0 Failed | 100% Pass Rate (45.22s)
  - CONSOLIDATED TOTAL: 36 Scenarios | 36 Passed | 0 Failed | 100% Pass Rate
- Key Highlights:
  - Full Feature Coverage: Automated TC-01 to TC-14 across login, catalog, sorting, cart, and checkout math.
  - Tax Calculation Verification (TC-11): Programmatically verified Subtotal ($45.98) + 8% Tax ($3.68) == Total ($49.66).
  - E2E Purchase Workflow: Automated complete 13-step purchase lifecycle in 3.45 seconds.
- Speaker Notes: We automated all 14 functional test cases plus negative parameterizations and a full E2E workflow. Both our Selenium and Robot Framework test suites achieved a 100% pass rate across 36 test runs.

#### CARD 7: Discrepancies Analysis & Technical Resolutions
- [AI IMAGE PROMPT]: A split-screen comparison visual showing a slow analog stopwatch on the left (18 mins) versus a glowing fast digital timer on the right (1 min 50s), high-tech performance comparison.
- Execution Speed Discrepancy:
  - Manual Execution (Phase 2): 18 minutes (1,080 seconds).
  - Automated Execution (Phase 3): 1 minute 50 seconds (110.58 seconds).
  - Variance: 89.8% Time Reduction (9.8x Faster Execution).
- Key Technical Resolutions:
  - React Virtual DOM Mutation (TC-04): Resolved StaleElementReferenceException by evaluating live DOM arrays atomically via JavaScript in BasePage.
  - Controlled Input Sync (TC-09, TC-10): Resolved headless Chrome send_keys() state bypass by dispatching synthetic 'input' and 'change' events.
  - Headless Text Rendering: Resolved empty string text extraction by standardizing on direct textContent JavaScript extraction.
- Speaker Notes: Comparing manual vs automated testing shows an 89.8% time reduction. We also resolved technical React virtual DOM stale element issues and controlled input state desynchronization using custom JavaScript helpers.

#### CARD 8: Continuous Integration (CI/CD) Pipelines
- [AI IMAGE PROMPT]: A futuristic continuous integration pipeline visualization showing code commit triggering Jenkins build server and GitHub Actions automated test runner, network nodes glowing green.
- Jenkins Pipeline (ci_cd/Jenkinsfile):
  - Declarative Multi-Stage Pipeline: Checkout -> Setup Virtualenv -> Selenium Pytest Stage -> Robot Framework Stage -> Archive Artifacts & JUnit XML.
- GitHub Actions Workflow (.github/workflows/):
  - Automatically triggers on every push and pull_request to main.
  - Executed on Windows runner with Python 3.11 and Headless Chrome.
  - Uploads interactive HTML test reports and failure screenshots as GitHub workflow run artifacts.
  - Verified building green on GitHub repository (MeetAhalpara/QA-Test-Automation).
- Speaker Notes: We integrated our automation suite into both Jenkins and GitHub Actions. Every time code is pushed to GitHub, our full regression suite executes automatically and publishes test artifacts.

#### CARD 9: Mandatory Live Demonstration Guide
- [AI IMAGE PROMPT]: A command line terminal window displaying live pytest output with passing green text and Chrome browser opening automatically in the background, sleek dark developer setup.
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

#### CARD 10: Project ROI, Recommendations & Conclusion
- [AI IMAGE PROMPT]: A sleek minimalist thank-you screen with GitHub logo, QR code concept, and Algonquin College modern campus backdrop, professional studio lighting.
- Quantifiable ROI & Value: 89.8% time savings on regression testing (reduced from 18 minutes to 1 min 50 seconds), saving significant manual QA hours per release cycle.
- Quality Assurance Guardrails: Continuous automated regression guardrails for Phase 2 defects D-01 (Empty Cart Checkout) and D-02 (Weak Input Rules).
- Developer Recommendations: Recommend SauceDemo development team implement client-side empty cart validation (#checkout button disable) and postal code regex format constraints.
- GitHub Repository: https://github.com/MeetAhalpara/QA-Test-Automation
- Thank you Professor Datta and class! We are happy to answer any questions.
- Speaker Notes: Thank you Professor Datta and class for your attention. All project code, documents, and reports are published on our GitHub repository. We are now happy to answer any questions!
```
