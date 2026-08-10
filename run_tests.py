"""
Unified Test Runner Script for CST8513 Assignment III Automation Testing.
Course: CST8513 - Quality Assurance and Testing
Students: Devangbhai Pandit & Meet Ahalpara
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.resolve()
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

PYTHON_EXE = sys.executable


def run_selenium_tests(headed: bool = False, marker: str = None) -> int:
    """Runs Selenium Pytest test suite."""
    print("\n" + "=" * 80)
    print(" EXECUTING SELENIUM WEBDRIVER TEST SUITE (PAGE OBJECT MODEL)")
    print("=" * 80)

    html_report = REPORTS_DIR / "selenium_test_report.html"
    junit_xml = REPORTS_DIR / "junit_selenium.xml"

    cmd = [
        PYTHON_EXE,
        "-m",
        "pytest",
        str(PROJECT_ROOT / "automation_selenium" / "tests"),
        "-v",
        f"--html={html_report}",
        "--self-contained-html",
        f"--junitxml={junit_xml}",
    ]

    if headed:
        cmd.append("--headed")
    if marker:
        cmd.extend(["-m", marker])

    print(f"Executing command: {' '.join(cmd)}\n")
    return subprocess.call(cmd)


def run_robot_tests() -> int:
    """Runs Robot Framework test suite."""
    print("\n" + "=" * 80)
    print(" EXECUTING ROBOT FRAMEWORK TEST SUITE")
    print("=" * 80)

    output_dir = REPORTS_DIR / "robot_logs"
    suite_path = PROJECT_ROOT / "automation_robot" / "tests" / "saucedemo_suite.robot"

    cmd = [
        PYTHON_EXE,
        "-m",
        "robot",
        "--outputdir",
        str(output_dir),
        str(suite_path),
    ]

    print(f"Executing command: {' '.join(cmd)}\n")
    return subprocess.call(cmd)


def main():
    parser = argparse.ArgumentParser(description="SauceDemo QA Test Automation Runner")
    parser.add_argument(
        "--suite",
        choices=["selenium", "robot", "all"],
        default="all",
        help="Test suite to run (default: all)",
    )
    parser.add_argument(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed browser mode (Selenium only)",
    )
    parser.add_argument(
        "--marker",
        type=str,
        default=None,
        help="Pytest marker filter (e.g. auth, inventory, cart, checkout, smoke, e2e)",
    )

    args = parser.parse_args()

    exit_code = 0
    if args.suite in ["selenium", "all"]:
        selenium_code = run_selenium_tests(headed=args.headed, marker=args.marker)
        if selenium_code != 0:
            exit_code = selenium_code

    if args.suite in ["robot", "all"]:
        robot_code = run_robot_tests()
        if robot_code != 0:
            exit_code = robot_code

    print("\n" + "=" * 80)
    print(" TEST EXECUTION COMPLETE")
    print("=" * 80)
    print(f"• Selenium HTML Report: {REPORTS_DIR / 'selenium_test_report.html'}")
    print(f"• Robot Framework Logs: {REPORTS_DIR / 'robot_logs' / 'report.html'}")
    print("=" * 80 + "\n")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
