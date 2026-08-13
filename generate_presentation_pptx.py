"""
Script to generate the formal Microsoft PowerPoint (.pptx) presentation for CST8513 Assignment III.
Target: 14 Widescreen (16:9) slides covering Project I, Project II, Project III, Discrepancies, and Live Demo.
Authors: Devangbhai Pandit & Meet Ahalpara
Professor: Prof. Sharmista Datta
Submission Date: August 13, 2026
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


def create_presentation():
    prs = Presentation()

    # Set slide dimensions to Widescreen 16:9 (13.333 x 7.5 inches)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_slide_layout = prs.slide_layouts[6]

    # Theme Colors
    COLOR_NAVY = RGBColor(0, 51, 102)        # #003366
    COLOR_TEAL = RGBColor(0, 128, 128)       # #008080
    COLOR_DARK = RGBColor(34, 34, 34)        # #222222
    COLOR_GRAY_BG = RGBColor(244, 246, 249)  # #F4F6F9
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_GREEN = RGBColor(0, 128, 0)
    COLOR_RED = RGBColor(180, 0, 0)

    def add_header(slide, title_text, category_text="CST8513: QUALITY ASSURANCE & TESTING"):
        # Header banner shape
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
        banner.fill.solid()
        banner.fill.fore_color.rgb = COLOR_NAVY
        banner.line.color.rgb = COLOR_NAVY

        # Accent stripe
        stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.1), Inches(13.333), Inches(0.08))
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = COLOR_TEAL
        stripe.line.color.rgb = COLOR_TEAL

        # Header Text Box
        tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.12), Inches(12.133), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_TEAL

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE

    def add_footer(slide, current_slide, total_slides=14):
        footer_tb = slide.shapes.add_textbox(Inches(0.6), Inches(7.1), Inches(12.133), Inches(0.35))
        tf = footer_tb.text_frame
        p = tf.paragraphs[0]
        p.text = f"SauceDemo QA Automation Project | Devangbhai Pandit & Meet Ahalpara | Prof. Sharmista Datta | Slide {current_slide} of {total_slides}"
        p.font.size = Pt(9)
        p.font.color.rgb = RGBColor(120, 120, 120)

    def set_speaker_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_slide_layout)

    # Main background rectangle
    bg = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_NAVY
    bg.line.color.rgb = COLOR_NAVY

    # Decorative Card
    card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_WHITE
    card.line.color.rgb = COLOR_TEAL

    tb1 = slide1.shapes.add_textbox(Inches(1.5), Inches(1.3), Inches(10.333), Inches(4.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "CST8513: QUALITY ASSURANCE & TESTING"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL

    p2 = tf1.add_paragraph()
    p2.text = "SauceDemo Test Automation Project"
    p2.alignment = PP_ALIGN.CENTER
    p2.font.size = Pt(32)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_NAVY

    p3 = tf1.add_paragraph()
    p3.text = "Comprehensive Synthesis of Project I, Project II & Project III (Automation & CI/CD)"
    p3.alignment = PP_ALIGN.CENTER
    p3.font.size = Pt(16)
    p3.font.italic = True
    p3.font.color.rgb = COLOR_DARK

    p4 = tf1.add_paragraph()
    p4.text = "\nPresented By: Devangbhai Pandit & Meet Ahalpara\nSubmitted To: Prof. Sharmista Datta\nAlgonquin College – School of Advanced Technology\nPresentation Date: August 13, 2026\nGitHub Repo: https://github.com/MeetAhalpara/QA-Test-Automation"
    p4.alignment = PP_ALIGN.CENTER
    p4.font.size = Pt(12)
    p4.font.color.rgb = RGBColor(80, 80, 80)

    set_speaker_notes(slide1, "Good morning/afternoon Professor Datta and classmates. Today Devangbhai and I are presenting our complete Quality Assurance project for SauceDemo, covering our end-to-end journey across Phase 1 Proposal, Phase 2 Manual Testing, and Phase 3 Automated Testing.")

    # =========================================================================
    # SLIDE 2: Executive Summary & Project Progression
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide2, "Executive Summary & Project Progression")
    add_footer(slide2, 2)

    # 3 Column Cards
    col_width = Inches(3.7)
    col_gap = Inches(0.3)
    left_margin = Inches(0.8)

    phases = [
        ("PROJECT I: SCOPE & PROPOSAL", "Requirements Analysis", [
            "Analyzed SauceDemo e-commerce architecture & business flows.",
            "Defined 14 Core Functional Requirements (FR-01 to FR-14).",
            "Covered Auth, Browsing, Sorting, Cart, Checkout Math, & Logout."
        ], COLOR_NAVY),
        ("PROJECT II: MANUAL TESTING", "Test Execution & Defects", [
            "Executed 14 manual test cases (TC-01 to TC-14) in Chrome.",
            "Achieved 85.7% Manual Pass Rate (12 Passed, 2 Failed).",
            "Logged 2 Defects: D-01 (Empty Cart Checkout) & D-02 (Weak Input Rules)."
        ], COLOR_TEAL),
        ("PROJECT III: AUTOMATION & CI/CD", "POM Framework & CI/CD", [
            "Automated 100% of test cases using Selenium WebDriver (POM) & Robot.",
            "100% Pass Rate across 36 test scenarios (22 Selenium + 14 Robot).",
            "Reduced regression time by 89.8% (18 mins -> 1 min 50s).",
            "CI/CD Pipeline set up with Jenkins & GitHub Actions."
        ], COLOR_NAVY)
    ]

    for idx, (title, sub, bullets, color) in enumerate(phases):
        x = left_margin + idx * (col_width + col_gap)
        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.5), col_width, Inches(5.3))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_GRAY_BG
        card.line.color.rgb = color

        tb = slide2.shapes.add_textbox(x + Inches(0.15), Inches(1.6), col_width - Inches(0.3), Inches(5.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = color

        p_sub = tf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(10)
        p_sub.font.italic = True
        p_sub.font.color.rgb = RGBColor(100, 100, 100)

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"• {b}"
            p_b.font.size = Pt(10)
            p_b.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide2, "This slide shows our 3-phase journey. In Phase 1 we mapped requirements, in Phase 2 we manually found defects, and in Phase 3 we turned those manual tests into a fully automated CI/CD pipeline running in under 2 minutes.")

    # =========================================================================
    # SLIDE 3: Project I Summary – Requirements Analysis & Scope
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide3, "Project I Summary: Application Analysis & Requirements Scope")
    add_footer(slide3, 3)

    # 2 Column Container
    box1 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3))
    box1.fill.solid()
    box1.fill.fore_color.rgb = COLOR_GRAY_BG
    box1.line.color.rgb = COLOR_NAVY

    tb_b1 = slide3.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.9))
    tf_b1 = tb_b1.text_frame
    tf_b1.word_wrap = True

    p = tf_b1.paragraphs[0]
    p.text = "Target Application & Core Requirements (FR-01 to FR-07)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    fr_part1 = [
        "FR-01: System authenticates standard_user and redirects to /inventory.html.",
        "FR-02: Displays specific error messages on invalid/locked credentials.",
        "FR-03: Renders all 6 product catalog items with titles, prices, & images.",
        "FR-04: Dynamic 4-way product sorting (A-Z, Z-A, Price Low-High, High-Low).",
        "FR-05: Product details page opens specs, $29.99 price, & back navigation.",
        "FR-06: Add to Cart increments shopping cart badge count dynamically.",
        "FR-07: Remove from Cart decrements shopping cart badge count."
    ]
    for item in fr_part1:
        p_item = tf_b1.add_paragraph()
        p_item.text = f"• {item}"
        p_item.font.size = Pt(10)
        p_item.font.color.rgb = COLOR_DARK

    box2 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.6), Inches(5.3))
    box2.fill.solid()
    box2.fill.fore_color.rgb = COLOR_GRAY_BG
    box2.line.color.rgb = COLOR_TEAL

    tb_b2 = slide3.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.2), Inches(4.9))
    tf_b2 = tb_b2.text_frame
    tf_b2.word_wrap = True

    p_b2 = tf_b2.paragraphs[0]
    p_b2.text = "Core Requirements Continued (FR-08 to FR-14)"
    p_b2.font.size = Pt(13)
    p_b2.font.bold = True
    p_b2.font.color.rgb = COLOR_TEAL

    fr_part2 = [
        "FR-08: Shopping cart review page displays selected items & prices.",
        "FR-09: Submitting blank checkout info blocks flow with First Name error.",
        "FR-10: Incomplete information input triggers specific field validation.",
        "FR-11: Order overview verifies Subtotal + 8% Tax == Total calculation.",
        "FR-12: Order completion renders 'Thank you for your order!' confirmation.",
        "FR-13: Cancel checkout returns cleanly to cart (Step 1) or inventory (Step 2).",
        "FR-14: Secure logout ends user session & blocks unauthorized URL access."
    ]
    for item in fr_part2:
        p_item = tf_b2.add_paragraph()
        p_item.text = f"• {item}"
        p_item.font.size = Pt(10)
        p_item.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide3, "In Project I, we thoroughly analyzed SauceDemo and established 14 functional requirements covering the end-to-end e-commerce purchasing workflow from authentication to order confirmation.")

    # =========================================================================
    # SLIDE 4: Project II Summary – Manual Testing Strategy
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide4, "Project II Summary: Manual Functional Testing Strategy")
    add_footer(slide4, 4)

    card4 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
    card4.fill.solid()
    card4.fill.fore_color.rgb = COLOR_GRAY_BG
    card4.line.color.rgb = COLOR_NAVY

    tb4 = slide4.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
    tf4 = tb4.text_frame
    tf4.word_wrap = True

    p = tf4.paragraphs[0]
    p.text = "Manual Execution Methodology & Parameters"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    m_points = [
        "1-to-1 Traceability Mapping: Authored 14 detailed manual test cases (TC-01 to TC-14) corresponding directly to functional requirements FR-01 to FR-14.",
        "Manual Execution Scope: Interacted with Google Chrome manually to execute login flows, credential boundary validations, dropdown sorting, cart add/remove, form inputs, math tax calculations, and session logout.",
        "Execution Overhead & Timing: Executing all 14 test cases manually required 18 full minutes (~1,080 seconds), averaging ~77.1 seconds per test case.",
        "Manual Verification Challenges: Human execution was susceptible to timing variation, required active mental calculation for tax verification, and depended on manual observation for defect recording."
    ]

    for pt in m_points:
        p_pt = tf4.add_paragraph()
        p_pt.text = f"• {pt}\n"
        p_pt.font.size = Pt(11)
        p_pt.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide4, "In Project II, we manually executed all 14 test cases. While manual testing allowed us to explore the UI, it required 18 full minutes of active human interaction for a single test cycle.")

    # =========================================================================
    # SLIDE 5: Project II Findings – Manual Results & Defect Reporting
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide5, "Project II Findings: Manual Execution Results & Defects")
    add_footer(slide5, 5)

    # 2 Cards for Defect D-01 and D-02
    d1 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3))
    d1.fill.solid()
    d1.fill.fore_color.rgb = COLOR_WHITE
    d1.line.color.rgb = COLOR_RED

    tb_d1 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.9))
    tf_d1 = tb_d1.text_frame
    tf_d1.word_wrap = True

    p = tf_d1.paragraphs[0]
    p.text = "DEFECT D-01 (SEVERITY: HIGH)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_RED

    d1_points = [
        "Defect Title: Empty Cart Checkout Allowed",
        "Requirement Impacted: FR-08 / TC-08 / TC-09",
        "Behavior Observed: SauceDemo permits users to navigate to /cart.html with 0 items and click Checkout, proceeding through customer info & overview.",
        "Risk: Causes unnecessary payment processing overhead & bad user experience.",
        "Manual Status: FAILED (Logged in Defect Report)"
    ]
    for pt in d1_points:
        p_pt = tf_d1.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(10)
        p_pt.font.color.rgb = COLOR_DARK

    d2 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.6), Inches(5.3))
    d2.fill.solid()
    d2.fill.fore_color.rgb = COLOR_WHITE
    d2.line.color.rgb = RGBColor(200, 100, 0)

    tb_d2 = slide5.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.2), Inches(4.9))
    tf_d2 = tb_d2.text_frame
    tf_d2.word_wrap = True

    p_d2 = tf_d2.paragraphs[0]
    p_d2.text = "DEFECT D-02 (SEVERITY: MEDIUM)"
    p_d2.font.size = Pt(13)
    p_d2.font.bold = True
    p_d2.font.color.rgb = RGBColor(200, 100, 0)

    d2_points = [
        "Defect Title: Inadequate Input Field Validation",
        "Requirement Impacted: FR-10 / TC-10",
        "Behavior Observed: Checkout customer fields accept single-character inputs ('a', '1', '!') without length or postal code regex validation.",
        "Risk: Potential data integrity issues in fulfillment systems.",
        "Manual Status: FAILED (Logged in Defect Report)"
    ]
    for pt in d2_points:
        p_pt = tf_d2.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(10)
        p_pt.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide5, "Manual testing uncovered 2 key application defects: D-01, where an empty cart can proceed to checkout, and D-02, where checkout forms accept single-character inputs. These formed our baseline for Phase 3 automation.")

    # =========================================================================
    # SLIDE 6: Project III Summary – Automation Strategy & Stack
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide6, "Project III Summary: Test Automation Strategy & Tech Stack")
    add_footer(slide6, 6)

    card6 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
    card6.fill.solid()
    card6.fill.fore_color.rgb = COLOR_GRAY_BG
    card6.line.color.rgb = COLOR_NAVY

    tb6 = slide6.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
    tf6 = tb6.text_frame
    tf6.word_wrap = True

    p = tf6.paragraphs[0]
    p.text = "Technology Stack & Automation Architecture"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    stack = [
        "Python 3.11: Primary programming language selected for high readability, rich testing ecosystem, and seamless CI/CD integration.",
        "Selenium WebDriver 4.47: Core browser automation library utilizing native Selenium Manager for automatic ChromeDriver management.",
        "Pytest 9.1 Test Framework: Executes test suites, handles test parameterization, fixtures, marker filtering, and CLI flags.",
        "Robot Framework 7.4: Keyword-driven test suite with SeleniumLibrary providing readable business-level test scripts.",
        "Pytest-HTML & JUnit XML: Generates self-contained interactive visual HTML reports and structured JUnit XML for CI pipelines.",
        "Dual Execution Modes: Supports Headed mode (--headed) for visual demonstration and Headless Chrome (--headless=new) for fast CI/CD execution."
    ]

    for item in stack:
        p_item = tf6.add_paragraph()
        p_item.text = f"• {item}\n"
        p_item.font.size = Pt(10.5)
        p_item.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide6, "For Project III, we selected Python, Selenium WebDriver, Pytest, and Robot Framework. This dual-framework approach gave us both code-based Page Object Model testing and business-readable keyword testing.")

    # =========================================================================
    # SLIDE 7: Page Object Model (POM) Architecture
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide7, "Page Object Model (POM) Architecture Breakdown")
    add_footer(slide7, 7)

    card7 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
    card7.fill.solid()
    card7.fill.fore_color.rgb = COLOR_WHITE
    card7.line.color.rgb = COLOR_TEAL

    tb7 = slide7.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
    tf7 = tb7.text_frame
    tf7.word_wrap = True

    p = tf7.paragraphs[0]
    p.text = "Modular Component Breakdown"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL

    pom_components = [
        "1. BasePage (base_page.py): Foundation parent class containing explicit waits (WebDriverWait), safe JavaScript clicks, React event dispatching, and screenshot capture.",
        "2. Encapsulated Page Classes (pages/*.py): 7 dedicated page objects (LoginPage, InventoryPage, ProductDetailsPage, CartPage, CheckoutStepOnePage, CheckoutStepTwoPage, CheckoutCompletePage) holding locators & action methods.",
        "3. Test Suites (tests/*.py): Pure assertion test files (test_authentication.py, test_inventory.py, test_cart.py, test_checkout.py, test_e2e_workflow.py) containing zero hardcoded locators.",
        "4. Architectural Benefits: High reusability, single-point locator maintenance, dynamic synchronization, and zero code duplication across test suites."
    ]

    for comp in pom_components:
        p_comp = tf7.add_paragraph()
        p_comp.text = f"• {comp}\n"
        p_comp.font.size = Pt(11)
        p_comp.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide7, "Our Selenium architecture follows the Page Object Model strictly. Locators are isolated inside Page classes. If an HTML ID changes tomorrow, we update one line in the Page class and zero test files break.")

    # =========================================================================
    # SLIDE 8: Project III Execution Results – 100% Pass Rate
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide8, "Project III Execution Results: 100% Pass Rate")
    add_footer(slide8, 8)

    # Table of Results
    rows = 4
    cols = 5
    table_shape = slide8.shapes.add_table(rows, cols, Inches(0.8), Inches(1.5), Inches(11.733), Inches(2.2))
    table = table_shape.table

    headers = ["Framework / Suite", "Total Scenarios", "Passed", "Failed", "Pass Rate"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.font.size = Pt(11)
        p.alignment = PP_ALIGN.CENTER

    data = [
        ["Selenium WebDriver (Pytest)", "22", "22", "0", "100%"],
        ["Robot Framework Suite", "14", "14", "0", "100%"],
        ["CONSOLIDATED TOTAL", "36", "36", "0", "100%"]
    ]

    for row_idx, r in enumerate(data, start=1):
        for col_idx, val in enumerate(r):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_GRAY_BG if row_idx < 3 else COLOR_TEAL
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(11)
            p.alignment = PP_ALIGN.CENTER
            if row_idx == 3:
                p.font.bold = True
                p.font.color.rgb = COLOR_WHITE
            elif col_idx == 4:
                p.font.bold = True
                p.font.color.rgb = COLOR_GREEN

    # Text box below table
    tb8 = slide8.shapes.add_textbox(Inches(0.8), Inches(4.0), Inches(11.733), Inches(2.8))
    tf8 = tb8.text_frame
    tf8.word_wrap = True

    p = tf8.paragraphs[0]
    p.text = "Key Automation Highlights:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    highlights = [
        "Full Feature Coverage: TC-01 to TC-14 automated seamlessly across login, catalog grid, 4-way sorting, cart management, checkout forms, and math calculations.",
        "Mathematical Verification (TC-11): Programmatically verified floating-point math: Subtotal ($45.98) + 8% Tax ($3.68) == Total ($49.66).",
        "E2E Purchase Workflow: Automated complete 13-step user purchasing journey from authentication to order finish and secure logout in 3.45 seconds."
    ]
    for h in highlights:
        p_h = tf8.add_paragraph()
        p_h.text = f"• {h}"
        p_h.font.size = Pt(10.5)
        p_h.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide8, "We automated all 14 functional test cases plus negative parameterizations and a full E2E workflow. Both our Selenium and Robot Framework test suites achieved a 100% pass rate across 36 test runs.")

    # =========================================================================
    # SLIDE 9: Discrepancies Analysis – Manual vs. Automated
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide9, "Discrepancies Analysis: Manual vs. Automated Execution")
    add_footer(slide9, 9)

    card9 = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
    card9.fill.solid()
    card9.fill.fore_color.rgb = COLOR_GRAY_BG
    card9.line.color.rgb = COLOR_NAVY

    tb9 = slide9.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
    tf9 = tb9.text_frame
    tf9.word_wrap = True

    p = tf9.paragraphs[0]
    p.text = "Execution Speed & Performance Discrepancy"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    disc_points = [
        "Total Execution Duration: Manual testing required 18 minutes (1,080 seconds) vs. Automation running in 1 minute 50 seconds (110.58 seconds) — an 89.8% reduction in regression time (9.8x faster).",
        "Average Time per Test Case: Reduced from ~77.1 seconds manually down to ~5.0 seconds per automated test case.",
        "Human Labor Savings: 100% human labor savings during regression cycles. Bot handles execution headlessly without manual interaction.",
        "Repeatability & Precision: Manual testing is subject to fatigue and human error; Automation provides 100% deterministic precision and instant screenshot evidence on failure."
    ]

    for pt in disc_points:
        p_pt = tf9.add_paragraph()
        p_pt.text = f"• {pt}\n"
        p_pt.font.size = Pt(11)
        p_pt.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide9, "Comparing manual vs automated testing shows an 89.8% time reduction. What took 18 minutes manually now runs automatically in under 2 minutes with zero human effort.")

    # =========================================================================
    # SLIDE 10: Technical Discrepancies & Resolutions
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide10, "Technical Discrepancies & Engineering Resolutions")
    add_footer(slide10, 10)

    card10 = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
    card10.fill.solid()
    card10.fill.fore_color.rgb = COLOR_WHITE
    card10.line.color.rgb = COLOR_TEAL

    tb10 = slide10.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
    tf10 = tb10.text_frame
    tf10.word_wrap = True

    p = tf10.paragraphs[0]
    p.text = "Key Technical Challenges & Solutions"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL

    tech_resolutions = [
        "1. React Virtual DOM Mutation (TC-04 Sorting): React unmounts old DOM nodes during re-sorting, causing StaleElementReferenceException. Resolved by evaluating live DOM arrays atomically via JavaScript in BasePage.",
        "2. Controlled Input Component Sync (TC-09, TC-10): Headless Chrome send_keys() bypassed React internal _valueTracker state. Resolved by dispatching synthetic 'input' and 'change' events in BasePage.enter_text().",
        "3. Headless Text Extraction Discrepancy: Selenium .text returned empty string on select span elements in headless mode. Resolved by standardizing on direct textContent JavaScript extraction.",
        "4. Transition Animation Sync (TC-14): Sidebar menu slide-out caused click interception. Resolved by adding explicit WebDriverWait conditions instead of hardcoded sleeps."
    ]

    for tr in tech_resolutions:
        p_tr = tf10.add_paragraph()
        p_tr.text = f"• {tr}\n"
        p_tr.font.size = Pt(10.5)
        p_tr.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide10, "Transitioning to automation revealed technical DOM quirks. We resolved React virtual DOM stale element issues and controlled input state desynchronization using custom JavaScript helpers.")

    # =========================================================================
    # SLIDE 11: Continuous Integration (CI/CD) Pipelines
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide11, "Continuous Integration (CI/CD) Pipeline Implementation")
    add_footer(slide11, 11)

    # 2 Columns for Jenkins and GitHub Actions
    j1 = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3))
    j1.fill.solid()
    j1.fill.fore_color.rgb = COLOR_GRAY_BG
    j1.line.color.rgb = COLOR_NAVY

    tb_j1 = slide11.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.9))
    tf_j1 = tb_j1.text_frame
    tf_j1.word_wrap = True

    p = tf_j1.paragraphs[0]
    p.text = "JENKINS PIPELINE (ci_cd/Jenkinsfile)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    j_points = [
        "Declarative Multi-Stage Pipeline:",
        "1. Checkout: Pulls latest code from git repository.",
        "2. Environment Setup: Installs requirements.txt.",
        "3. Selenium Pytest Stage: Runs headless test suite & outputs JUnit XML.",
        "4. Robot Framework Stage: Runs headless Robot suite.",
        "5. Archive Artifacts: Publishes HTML reports & test results."
    ]
    for pt in j_points:
        p_pt = tf_j1.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(10)
        p_pt.font.color.rgb = COLOR_DARK

    g2 = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.6), Inches(5.3))
    g2.fill.solid()
    g2.fill.fore_color.rgb = COLOR_GRAY_BG
    g2.line.color.rgb = COLOR_TEAL

    tb_g2 = slide11.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.2), Inches(4.9))
    tf_g2 = tb_g2.text_frame
    tf_g2.word_wrap = True

    p_g2 = tf_g2.paragraphs[0]
    p_g2.text = "GITHUB ACTIONS (.github/workflows/)"
    p_g2.font.size = Pt(13)
    p_g2.font.bold = True
    p_g2.font.color.rgb = COLOR_TEAL

    g_points = [
        "Automated Push & PR Workflow:",
        "• Triggers automatically on code push to main/master.",
        "• Runs on Windows runner with Python 3.11.",
        "• Executes both Selenium and Robot test suites.",
        "• Uploads HTML test reports and failure screenshots as GitHub workflow run artifacts.",
        "• Verified building green on GitHub repository."
    ]
    for pt in g_points:
        p_pt = tf_g2.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(10)
        p_pt.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide11, "We integrated our automation suite into both Jenkins and GitHub Actions. Every time code is pushed to GitHub, our full regression suite executes automatically and publishes test artifacts.")

    # =========================================================================
    # SLIDE 12: Live Demonstration Guide (Mandatory Demo)
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide12, "Mandatory Live Demonstration Guide")
    add_footer(slide12, 12)

    card12 = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
    card12.fill.solid()
    card12.fill.fore_color.rgb = COLOR_WHITE
    card12.line.color.rgb = COLOR_NAVY

    tb12 = slide12.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
    tf12 = tb12.text_frame
    tf12.word_wrap = True

    p = tf12.paragraphs[0]
    p.text = "Live Execution Steps & Terminal Commands"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    demo_steps = [
        "Step 1: Visual Headed Execution (Watch Chrome Run Live)",
        "   Command: python -m pytest automation_selenium/tests/ --headed -v",
        "   Demonstrates: Real-time browser automation of login, sorting, cart add/remove, form input, math tax validation, and logout.",
        "Step 2: Unified Test Runner Execution",
        "   Command: python run_tests.py --suite all",
        "   Demonstrates: Sequential execution of Pytest POM suite and Robot Framework suite with summary console metrics.",
        "Step 3: Interactive Visual HTML Report Inspection",
        "   Open in Browser: reports/selenium_test_report.html & reports/robot_logs/report.html",
        "   Demonstrates: 100% Pass Rate charts, individual test timings, system environment metadata, and failure screenshot hooks."
    ]

    for ds in demo_steps:
        p_ds = tf12.add_paragraph()
        p_ds.text = ds
        if ds.startswith("Step"):
            p_ds.font.bold = True
            p_ds.font.size = Pt(11.5)
            p_ds.font.color.rgb = COLOR_TEAL
        else:
            p_ds.font.size = Pt(10)
            p_ds.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide12, "Now we will perform our mandatory live demo. First, we will run our tests in headed mode so you can watch Chrome perform actions live. Then we will show our unified runner and interactive HTML test reports.")

    # =========================================================================
    # SLIDE 13: Project ROI, Value Delivered & Recommendations
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide13, "Project ROI, Value Delivered & Recommendations")
    add_footer(slide13, 13)

    card13 = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
    card13.fill.solid()
    card13.fill.fore_color.rgb = COLOR_GRAY_BG
    card13.line.color.rgb = COLOR_NAVY

    tb13 = slide13.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
    tf13 = tb13.text_frame
    tf13.word_wrap = True

    p = tf13.paragraphs[0]
    p.text = "Value Delivered & Future Automation Roadmap"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    val_points = [
        "1. Quantifiable ROI: 89.8% time savings on regression testing (reduced from 18 minutes to 1 min 50 seconds), saving significant manual QA hours per release cycle.",
        "2. Quality Assurance Guardrails: Continuous automated regression guardrails for Phase 2 defects D-01 (Empty Cart Checkout) and D-02 (Weak Input Rules).",
        "3. Future Cross-Browser Grid: Expand test execution matrix across Firefox, Edge, and Safari using Selenium Grid / Docker containers.",
        "4. Application Development Recommendations: Recommend SauceDemo development team implement client-side empty cart validation (#checkout button disable) and postal code regex format constraints."
    ]

    for vp in val_points:
        p_vp = tf13.add_paragraph()
        p_vp.text = f"• {vp}\n"
        p_vp.font.size = Pt(11)
        p_vp.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide13, "The ROI of our automation is clear: 9.8x faster regression testing, 100% repeatability, and immediate CI/CD feedback. We recommend SauceDemo developers fix defects D-01 and D-02 in upcoming releases.")

    # =========================================================================
    # SLIDE 14: Conclusion & Q&A
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_slide_layout)
    add_header(slide14, "Conclusion & Questions")
    add_footer(slide14, 14)

    card14 = slide14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
    card14.fill.solid()
    card14.fill.fore_color.rgb = COLOR_WHITE
    card14.line.color.rgb = COLOR_TEAL

    tb14 = slide14.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
    tf14 = tb14.text_frame
    tf14.word_wrap = True

    p = tf14.paragraphs[0]
    p.text = "Project Conclusion Summary"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL

    p_body = tf14.add_paragraph()
    p_body.text = "• Successfully synthesized Phase 1 (Proposal & Scope), Phase 2 (Manual Testing & Defects), and Phase 3 (Automated Testing & CI/CD).\n• Achieved 100% Pass Rate across 36 test runs using Selenium Page Object Model & Robot Framework.\n• Full CI/CD integration established with Jenkins and GitHub Actions.\n\nGitHub Repository: https://github.com/MeetAhalpara/QA-Test-Automation\n\nThank you Professor Datta and class! We are happy to answer any questions."
    p_body.font.size = Pt(12)
    p_body.font.color.rgb = COLOR_DARK

    set_speaker_notes(slide14, "Thank you Professor Datta and class for your attention. All project code, documents, and reports are published on our GitHub repository. We are now happy to answer any questions!")

    output_path = "Docs/Project 3 - Final Presentation - Devangbhai & Meet.pptx"
    prs.save(output_path)
    print(f"Successfully generated presentation: {output_path}")


if __name__ == "__main__":
    create_presentation()
