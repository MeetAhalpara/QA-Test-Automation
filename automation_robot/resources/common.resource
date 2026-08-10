*** Settings ***
Documentation    Common keywords and utilities for SauceDemo automation suite.
...              Course: CST8513 - Quality Assurance and Testing (Assignment III)
...              Students: Devangbhai Pandit & Meet Ahalpara
Library          SeleniumLibrary
Resource         variables.resource

*** Keywords ***
Open SauceDemo In Browser
    [Documentation]    Opens the SauceDemo application in Chrome headless mode.
    Open Browser    ${BASE_URL}    headlesschrome    options=add_argument("--no-sandbox");add_argument("--disable-dev-shm-usage");add_argument("--window-size=1920,1080")
    Set Selenium Timeout    ${TIMEOUT}
    Set Selenium Speed      ${DELAY}

Close Test Browser
    [Documentation]    Closes the active browser session.
    Close Browser

Login To Application
    [Arguments]    ${username}    ${password}
    [Documentation]    Enters credentials and submits the login form.
    Execute Javascript
    ...    function setVal(id, v) {
    ...        let el = document.getElementById(id);
    ...        let last = el.value;
    ...        el.value = v;
    ...        if (el._valueTracker) el._valueTracker.setValue(last);
    ...        el.dispatchEvent(new Event('input', { bubbles: true }));
    ...    }
    ...    setVal('user-name', '${username}');
    ...    setVal('password', '${password}');
    Execute Javascript    document.getElementById('login-button').click();

Login As Standard User
    [Documentation]    Performs successful login using standard credentials.
    Login To Application    ${VALID_USER}    ${VALID_PASSWORD}
    Wait Until Location Contains    inventory.html
    Wait Until Page Contains Element    ${PAGE_TITLE}
    Element Text Should Be              ${PAGE_TITLE}    Products

Logout From Application
    [Documentation]    Opens sidebar and performs logout.
    Execute Javascript    document.getElementById('react-burger-menu-btn').click();
    Sleep    0.5s
    Execute Javascript    document.getElementById('logout_sidebar_link').click();
    Wait Until Page Contains Element    ${LOGIN_BUTTON}

Add Item To Cart By Name
    [Arguments]    ${item_name}
    [Documentation]    Locates item by name and clicks its Add to cart button.
    ${locator}=    Set Variable    xpath=//div[text()='${item_name}']/ancestor::div[@class='inventory_item']//button
    Execute Javascript    document.evaluate("//div[text()='${item_name}']/ancestor::div[@class='inventory_item']//button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();
    Sleep    0.3s

Remove Item From Cart By Name
    [Arguments]    ${item_name}
    [Documentation]    Locates item by name and clicks its Remove button.
    Execute Javascript    document.evaluate("//div[text()='${item_name}']/ancestor::div[contains(@class, 'item')]//button[text()='Remove']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();
    Sleep    0.3s

Navigate To Cart
    [Documentation]    Clicks the shopping cart icon and waits for cart page to load.
    Execute Javascript    document.querySelector('.shopping_cart_link').click();
    Wait Until Location Contains    cart.html

Proceed To Checkout
    [Documentation]    Navigates from cart to checkout step 1.
    Navigate To Cart
    Wait Until Page Contains Element    id=checkout
    Execute Javascript    document.getElementById('checkout').click();
    Wait Until Location Contains    checkout-step-one.html

Fill Checkout Form
    [Arguments]    ${first_name}    ${last_name}    ${postal_code}
    [Documentation]    Fills customer information fields in Checkout Step 1.
    Execute Javascript
    ...    function setInput(id, val) {
    ...        let input = document.getElementById(id);
    ...        if (!input) return;
    ...        let lastValue = input.value;
    ...        input.value = val;
    ...        let tracker = input._valueTracker;
    ...        if (tracker) tracker.setValue(lastValue);
    ...        input.dispatchEvent(new Event('input', { bubbles: true }));
    ...        input.dispatchEvent(new Event('change', { bubbles: true }));
    ...    }
    ...    setInput('first-name', '${first_name}');
    ...    setInput('last-name', '${last_name}');
    ...    setInput('postal-code', '${postal_code}');

Submit Checkout Step One
    [Documentation]    Clicks Continue on checkout step 1.
    Execute Javascript    document.getElementById('continue').click();

Complete Order
    [Documentation]    Clicks Finish on checkout step 2.
    Execute Javascript    document.getElementById('finish').click();
    Wait Until Location Contains    checkout-complete.html
