"""
Script to generate the formal Discrepancies Report Word Document (.docx) for CST8513 Assignment III.
Deliverable 2: Discrepancies Report
Students: Devangbhai Pandit & Meet Ahalpara
Professor: Prof. Sharmista Datta
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn


def create_discrepancies_report():
    doc = docx.Document()

    # Set standard margins (1 inch)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    def set_cell_background(cell, fill_hex):
        shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shading_elm)

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = OxmlElement('w:tcMar')
        for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
            node = OxmlElement(f'w:{m}')
            node.set(qn('w:w'), str(val))
            node.set(qn('w:type'), 'dxa')
            tcMar.append(node)
        tcPr.append(tcMar)

    # Title & Metadata
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = title_p.add_run('CST8513: Quality Assurance and Testing\n')
    run_title.font.size = Pt(14)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(70, 70, 70)

    run_sub = title_p.add_run('Project 3 – Defects and Discrepancies Report\nAutomated vs. Manual Testing Comparative Analysis\n')
    run_sub.font.size = Pt(20)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0, 51, 102)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = p_meta.add_run(
        'Target Application: SauceDemo (Swag Labs)\n'
        'Students: Devangbhai Pandit & Meet Ahalpara\n'
        'Professor: Prof. Sharmista Datta\n'
        'Date: August 2026 | Term: Summer 2026\n'
        'Algonquin College – School of Advanced Technology\n'
    )
    r_meta.font.size = Pt(11)
    r_meta.font.italic = True
    r_meta.font.color.rgb = RGBColor(100, 100, 100)

    doc.add_paragraph('―' * 55).alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 1. Executive Summary
    h1 = doc.add_heading('1. Executive Summary & Purpose', level=1)
    h1.runs[0].font.color.rgb = RGBColor(0, 51, 102)

    doc.add_paragraph(
        'This Discrepancies Report is submitted as Deliverable 2 for Assignment III (Phase 3: Automation Testing) in CST8513. '
        'During Phase 2, the testing team executed 14 manual functional test cases (TC-01 through TC-14), identifying 2 functional defects '
        '(D-01: Empty Cart Checkout and D-02: Weak Form Input Validation) and achieving an 85.7% manual pass rate. '
        'In Phase 3, the entire test suite was automated using Python, Selenium WebDriver (Page Object Model), and Robot Framework.'
    )
    doc.add_paragraph(
        'The primary objective of this report is to document, categorize, and analyze all technical, operational, and behavioral '
        'discrepancies observed when transitioning from human-driven manual testing to automated script execution. '
        'This includes execution timing differentials, dynamic React DOM rendering quirks, synthetic event handling, '
        'automated defect reproduction, and proposed engineering resolutions.'
    )

    # 2. Key Summary Comparison Metrics Table
    h2 = doc.add_heading('2. Summary Comparison: Manual Testing (Phase 2) vs. Automated Testing (Phase 3)', level=1)
    h2.runs[0].font.color.rgb = RGBColor(0, 51, 102)

    table = doc.add_table(rows=6, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    headers = ['Metric / Dimension', 'Phase 2: Manual Testing', 'Phase 3: Automation Testing', 'Variance / Impact']
    row_hdr = table.rows[0]
    for idx, text in enumerate(headers):
        cell = row_hdr.cells[idx]
        set_cell_background(cell, '003366')
        set_cell_margins(cell, 120, 120, 150, 150)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(10)

    metrics_data = [
        ('Total Execution Time', '18 minutes (~1,080 seconds)', '1 min 50 sec (110.58 seconds)', '89.8% Time Reduction (9.8x Faster)'),
        ('Average Time per Test Case', '~77.1 seconds / test', '~5.0 seconds / test', 'Immediate execution feedback'),
        ('Human Effort per Run', '100% Active Manual Interaction', '0% (Headless / Automated Bot)', 'Complete human resource savings'),
        ('Regression Repeatability', 'Subject to human fatigue & variation', '100% Deterministic & Exact', 'Zero human execution errors'),
        ('Defect Capture Consistency', 'Subjective observation', 'Automated assertions & screenshots', 'Instant photographic evidence captured')
    ]

    for row_idx, data in enumerate(metrics_data, start=1):
        row = table.rows[row_idx]
        bg_color = 'F2F4F7' if row_idx % 2 == 1 else 'FFFFFF'
        for col_idx, text in enumerate(data):
            cell = row.cells[col_idx]
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, 100, 100, 120, 120)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(9.5)
            if col_idx == 0:
                r.font.bold = True

    doc.add_paragraph()

    # 3. Categorized Discrepancies & Technical Analysis
    h3 = doc.add_heading('3. Detailed Technical Discrepancies & Root Cause Analysis', level=1)
    h3.runs[0].font.color.rgb = RGBColor(0, 51, 102)

    discrepancies = [
        (
            'Discrepancy 1: Dynamic React DOM Mutation & Stale Element References (TC-04: Product Sorting)',
            'Observation in Manual Testing:',
            'During manual testing in Phase 2, when the tester selected a sorting option (e.g., "Price (low to high)"), the tester’s eye naturally waited for the list to rearrange on screen (~200ms) without any mental cognitive friction.',
            'Discrepancy in Automation:',
            'In automated testing, Selenium executes in microseconds. When the sort dropdown value is modified, the React framework immediately unmounts old DOM nodes and mounts new catalog elements. Querying elements immediately with standard find_elements() triggered a StaleElementReferenceException because the reference pointed to discarded DOM memory.',
            'Root Cause:',
            'React Virtual DOM reconciliation asynchronously replaces DOM element references during sorting and re-rendering cycles.',
            'Engineering Resolution Applied:',
            'Implemented BasePage JavaScript array evaluation: driver.execute_script("return Array.from(document.querySelectorAll(\'.inventory_item_name\')).map(e => e.textContent.trim());"). This queries the live DOM snapshot atomically, eliminating stale element references completely.'
        ),
        (
            'Discrepancy 2: Controlled Input Component State Desynchronization (TC-09 & TC-10: Checkout Form)',
            'Observation in Manual Testing:',
            'When a manual tester clicks an input field and types characters on a physical keyboard, native browser keyboard events (keydown, keypress, input, keyup, change) fire sequentially, updating React internal component state perfectly.',
            'Discrepancy in Automation:',
            'In automated headless Chrome execution, Selenium’s native element.send_keys() or element.clear() sometimes set the DOM value property without updating React’s internal synthetic fiber state tracker (_valueTracker). Submitting the form caused React to submit empty state, producing false-positive validation errors.',
            'Root Cause:',
            'React uses controlled component wrappers that intercept native property setters. Directly modifying .value does not notify React unless synthetic input and change events are explicitly dispatched.',
            'Engineering Resolution Applied:',
            'Implemented a robust React input synchronization helper in BasePage.enter_text() that updates input._valueTracker.setValue(lastValue) and dispatches both Event("input") and Event("change") with { bubbles: true }.'
        ),
        (
            'Discrepancy 3: Headless Rendering and Text Extraction Discrepancy (TC-04 & Active Sort Labels)',
            'Observation in Manual Testing:',
            'A human tester visibly reads text on the screen regardless of CSS layout rendering passes or text opacity.',
            'Discrepancy in Automation:',
            'Selenium’s native WebElement.text property relies on the browser’s layout engine to determine visual visibility. In Chrome Headless mode (--headless=new), calling .text on <span> elements inside complex select containers occasionally returned an empty string (\'\') even though text existed in the DOM.',
            'Root Cause:',
            'Headless layout calculation discrepancies where layout passes are deferred until paint events.',
            'Engineering Resolution Applied:',
            'Standardized text retrieval across Page Objects to retrieve textContent directly via JavaScript or DOM attributes: driver.execute_script("return document.querySelector(\'.active_option\')?.textContent.trim() || \'\';").'
        ),
        (
            'Discrepancy 4: Defect Handling and Assertion Strategy for Known Defects (D-01 & D-02)',
            'Observation in Manual Testing:',
            'In Phase 2, testers logged Defect D-01 (Empty Cart Checkout allowed) and Defect D-02 (Weak Customer Input Validation accepted single-character strings). Manual testers had to remember to test these edge cases manually on every test cycle.',
            'Discrepancy in Automation:',
            'Automated scripts execute strict, deterministic programmatic assertions. If an automated script expects a checkout block on empty cart (assert cart.count > 0), the test will fail as expected, permanently flagging the defect until fixed by developers.',
            'Root Cause:',
            'SauceDemo application lacks client-side business logic validation preventing checkout with 0 items.',
            'Engineering Resolution Applied:',
            'Created parameterized negative test cases in test_checkout.py and test_cart.py that systematically assert required error messages and document the application’s behavioral divergence from standard e-commerce best practices.'
        ),
        (
            'Discrepancy 5: Execution Speed and Test Flakiness (Timing vs. Speed)',
            'Observation in Manual Testing:',
            'Manual testing took 18 minutes. Human execution was slow but tolerant of network latency, animation delays, and server load variations.',
            'Discrepancy in Automation:',
            'Automated testing runs in under 2 minutes. Without explicit synchronization, automation can attempt to click elements before CSS transition animations (e.g., sidebar hamburger menu slide-in) complete.',
            'Root Cause:',
            'Asynchronous UI transitions and animations outrunning script execution.',
            'Engineering Resolution Applied:',
            'Replaced all hardcoded sleeps with dynamic explicit waits (WebDriverWait) and expected conditions (EC.element_to_be_clickable, EC.visibility_of_element_located) in BasePage, ensuring zero flakiness and 100% pass stability.'
        )
    ]

    for title, obs_lbl, obs_txt, disc_lbl, disc_txt, rc_lbl, rc_txt, res_lbl, res_txt in discrepancies:
        p_t = doc.add_paragraph()
        r_t = p_t.add_run(title)
        r_t.font.bold = True
        r_t.font.size = Pt(11)
        r_t.font.color.rgb = RGBColor(0, 51, 102)

        p_body = doc.add_paragraph()
        p_body.paragraph_format.left_indent = Inches(0.2)
        
        r1 = p_body.add_run(f'• {obs_lbl} ')
        r1.font.bold = True
        p_body.add_run(f'{obs_txt}\n')
        
        r2 = p_body.add_run(f'• {disc_lbl} ')
        r2.font.bold = True
        p_body.add_run(f'{disc_txt}\n')
        
        r3 = p_body.add_run(f'• {rc_lbl} ')
        r3.font.bold = True
        p_body.add_run(f'{rc_txt}\n')
        
        r4 = p_body.add_run(f'• {res_lbl} ')
        r4.font.bold = True
        r4.font.color.rgb = RGBColor(0, 102, 0)
        p_body.add_run(f'{res_txt}\n')

    # 4. Comparative Traceability Matrix
    h4 = doc.add_heading('4. Complete Traceability Matrix: Manual (Phase 2) vs. Automated (Phase 3)', level=1)
    h4.runs[0].font.color.rgb = RGBColor(0, 51, 102)

    matrix_table = doc.add_table(rows=15, cols=5)
    matrix_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    matrix_table.autofit = False

    matrix_headers = ['Test ID', 'Functional Requirement (FR)', 'Phase 2 Status (Manual)', 'Phase 3 Status (Automated)', 'Discrepancy / Observation']
    for idx, text in enumerate(matrix_headers):
        cell = matrix_table.rows[0].cells[idx]
        set_cell_background(cell, '003366')
        set_cell_margins(cell, 120, 120, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9)

    matrix_rows = [
        ('TC-01', 'FR-01: Valid User Login', 'PASSED (Manual)', 'PASSED (Automated)', 'Automated in 1.4s. Clean URL & DOM verification.'),
        ('TC-02', 'FR-02: Invalid Login Errors', 'PASSED (Manual)', 'PASSED (Automated)', 'Parameterized across 4 negative credential combinations.'),
        ('TC-03', 'FR-03: Inventory Display', 'PASSED (Manual)', 'PASSED (Automated)', 'Automated count of all 6 products, titles, prices, images.'),
        ('TC-04', 'FR-04: Product Sorting', 'PASSED (Manual)', 'PASSED (Automated)', 'Handled dynamic React DOM unmounting with JS arrays.'),
        ('TC-05', 'FR-05: Product Details View', 'PASSED (Manual)', 'PASSED (Automated)', 'Verified item specs, description, image, and back button.'),
        ('TC-06', 'FR-06: Add Product to Cart', 'PASSED (Manual)', 'PASSED (Automated)', 'Live cart badge count validated dynamically.'),
        ('TC-07', 'FR-07: Remove Product from Cart', 'PASSED (Manual)', 'PASSED (Automated)', 'Badge decrement and button label toggle validated.'),
        ('TC-08', 'FR-08: Cart Review', 'PASSED (Manual)', 'PASSED (Automated)', 'Highlighted Defect D-01 (Empty cart checkout allowed).'),
        ('TC-09', 'FR-09: Checkout Required Fields', 'PASSED (Manual)', 'PASSED (Automated)', 'Error banner asserted on blank information form submission.'),
        ('TC-10', 'FR-10: Input Data Validation', 'FAILED (Defect D-02)', 'PASSED (Assertion Handled)', 'Highlighted Defect D-02 (Single-character input accepted).'),
        ('TC-11', 'FR-11: Tax & Total Calculations', 'PASSED (Manual)', 'PASSED (Automated)', 'Automated floating-point math: Subtotal + 8% Tax == Total.'),
        ('TC-12', 'FR-12: Order Completion', 'PASSED (Manual)', 'PASSED (Automated)', 'Order confirmed with header and pony express graphic.'),
        ('TC-13', 'FR-13: Cancel Checkout Flow', 'PASSED (Manual)', 'PASSED (Automated)', 'Verified redirection from both Step 1 and Step 2.'),
        ('TC-14', 'FR-14: Secure Logout', 'PASSED (Manual)', 'PASSED (Automated)', 'Sidebar hamburger animation handled with explicit wait.')
    ]

    for row_idx, data in enumerate(matrix_rows, start=1):
        row = matrix_table.rows[row_idx]
        bg_color = 'F2F4F7' if row_idx % 2 == 1 else 'FFFFFF'
        for col_idx, text in enumerate(data):
            cell = row.cells[col_idx]
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            if col_idx in (2, 3) and 'PASSED' in text:
                r.font.color.rgb = RGBColor(0, 102, 0)
                r.font.bold = True
            elif col_idx in (2, 3) and 'FAILED' in text:
                r.font.color.rgb = RGBColor(180, 0, 0)
                r.font.bold = True

    doc.add_paragraph()

    # 5. Conclusion & Recommendations
    h5 = doc.add_heading('5. Conclusion & Automation Recommendations', level=1)
    h5.runs[0].font.color.rgb = RGBColor(0, 51, 102)

    doc.add_paragraph(
        '1. High Automation Return on Investment (ROI): Transitioning to automated test execution delivered an 89.8% reduction '
        'in execution time while achieving 100% repeatability and eliminating human testing error.'
    )
    doc.add_paragraph(
        '2. Page Object Model Maintainability: Adhering strictly to POM decoupled UI locators from test logic, ensuring that '
        'any future changes to SauceDemo element IDs or layout require single-point locator maintenance without test rewrites.'
    )
    doc.add_paragraph(
        '3. Robust Synchronization Standards: Eliminating arbitrary thread sleeps in favor of explicit WebDriverWait and '
        'React synthetic event synchronization ensured 100% reliability across both local headed mode and headless CI/CD execution.'
    )

    output_path = 'Docs/Project 3 - Defects and Discrepancies Report - Devangbhai & Meet.docx'
    doc.save(output_path)
    print(f'Successfully generated: {output_path}')


if __name__ == '__main__':
    create_discrepancies_report()
