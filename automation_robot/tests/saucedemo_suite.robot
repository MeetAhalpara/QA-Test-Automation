*** Settings ***
Documentation    Robot Framework Test Suite covering Functional Test Cases TC-01 through TC-14.
...              Course: CST8513 - Quality Assurance and Testing (Assignment III)
...              Students: Devangbhai Pandit & Meet Ahalpara
Resource         ../resources/common.resource
Test Setup       Open SauceDemo In Browser
Test Teardown    Close Test Browser

*** Test Cases ***
TC-01: Verify Successful Login With Valid Credentials
    [Documentation]    FR-01: System authenticates standard_user and redirects to /inventory.html.
    [Tags]             auth    smoke
    Login To Application    ${VALID_USER}    ${VALID_PASSWORD}
    Location Should Contain    inventory.html
    Element Text Should Be     ${PAGE_TITLE}    Products
    Page Should Contain Element    ${INVENTORY_ITEM}

TC-02: Verify Login Error For Invalid Credentials
    [Documentation]    FR-02: Clear error message displayed when submitting invalid credentials.
    [Tags]             auth    negative
    Login To Application    ${INVALID_USER}    ${INVALID_PASSWORD}
    Element Should Be Visible    ${LOGIN_ERROR_BANNER}
    Element Should Contain       ${LOGIN_ERROR_BANNER}    Username and password do not match

TC-03: Verify Product Inventory Display
    [Documentation]    FR-03: Inventory grid displays all 6 catalog items with details.
    [Tags]             inventory
    Login As Standard User
    ${count}=    Get Element Count    ${INVENTORY_ITEM}
    Should Be Equal As Integers       ${count}    6
    Page Should Contain               Sauce Labs Backpack
    Page Should Contain               Sauce Labs Bike Light

TC-04: Verify Product Sorting Functionality
    [Documentation]    FR-04: Products reorder dynamically when sorting option is selected.
    [Tags]             inventory
    Login As Standard User
    Select From List By Value    ${SORT_DROPDOWN}    lohi
    Element Text Should Be       ${ACTIVE_SORT_LABEL}    Price (low to high)
    Select From List By Value    ${SORT_DROPDOWN}    za
    Element Text Should Be       ${ACTIVE_SORT_LABEL}    Name (Z to A)

TC-05: Verify Product Details View
    [Documentation]    FR-05: Clicking product opens details page with price and description.
    [Tags]             inventory
    Login As Standard User
    Click Element                xpath=//div[text()='Sauce Labs Backpack']
    Location Should Contain      inventory-item.html
    Element Text Should Be       ${DETAILS_NAME}     Sauce Labs Backpack
    Element Text Should Be       ${DETAILS_PRICE}    $29.99
    Execute Javascript           document.getElementById('back-to-products').click();
    Wait Until Location Contains    inventory.html

TC-06: Verify Add Product To Cart
    [Documentation]    FR-06: Cart count updates immediately when adding products.
    [Tags]             cart    smoke
    Login As Standard User
    Add Item To Cart By Name     Sauce Labs Backpack
    Element Text Should Be       ${CART_BADGE}    1
    Add Item To Cart By Name     Sauce Labs Bike Light
    Element Text Should Be       ${CART_BADGE}    2

TC-07: Verify Remove Product From Cart
    [Documentation]    FR-07: Cart count decrements when removing products.
    [Tags]             cart
    Login As Standard User
    Add Item To Cart By Name     Sauce Labs Backpack
    Add Item To Cart By Name     Sauce Labs Bike Light
    Element Text Should Be       ${CART_BADGE}    2
    Remove Item From Cart By Name    Sauce Labs Backpack
    Element Text Should Be       ${CART_BADGE}    1

TC-08: Verify Shopping Cart Review
    [Documentation]    FR-08: Reviewing cart page displays selected items accurately.
    [Tags]             cart
    Login As Standard User
    Add Item To Cart By Name     Sauce Labs Backpack
    Navigate To Cart
    Page Should Contain          Sauce Labs Backpack
    Page Should Contain          $29.99
    Execute Javascript           document.getElementById('continue-shopping').click();
    Wait Until Location Contains    inventory.html

TC-09: Verify Checkout Required Fields Validation
    [Documentation]    FR-09: Submitting blank checkout form triggers First Name error.
    [Tags]             checkout    negative
    Login As Standard User
    Add Item To Cart By Name     Sauce Labs Backpack
    Proceed To Checkout
    Submit Checkout Step One
    Wait Until Element Is Visible    ${CHECKOUT_ERROR_BANNER}
    Element Should Contain           ${CHECKOUT_ERROR_BANNER}    Error: First Name is required

TC-10: Verify Checkout Incomplete Data Validation
    [Documentation]    FR-10: Submitting missing postal code triggers Postal Code error.
    [Tags]             checkout    negative
    Login As Standard User
    Add Item To Cart By Name     Sauce Labs Backpack
    Proceed To Checkout
    Fill Checkout Form           ${FIRST_NAME}    ${LAST_NAME}    ${EMPTY}
    Submit Checkout Step One
    Wait Until Element Is Visible    ${CHECKOUT_ERROR_BANNER}
    Element Should Contain           ${CHECKOUT_ERROR_BANNER}    Error: Postal Code is required

TC-11: Verify Checkout Overview Tax and Total Calculations
    [Documentation]    FR-11: Overview displays correct item subtotal, 8% tax, and total.
    [Tags]             checkout
    Login As Standard User
    Add Item To Cart By Name     Sauce Labs Backpack
    Proceed To Checkout
    Fill Checkout Form           ${FIRST_NAME}    ${LAST_NAME}    ${POSTAL_CODE}
    Submit Checkout Step One
    Wait Until Location Contains    checkout-step-two.html
    Element Should Contain       ${SUBTOTAL_LABEL}    Item total: $29.99
    Element Should Contain       ${TAX_LABEL}         Tax: $2.40
    Element Should Contain       ${TOTAL_LABEL}       Total: $32.39

TC-12: Verify Order Completion Confirmation
    [Documentation]    FR-12: Clicking Finish shows order confirmation and back home navigation.
    [Tags]             checkout    smoke
    Login As Standard User
    Add Item To Cart By Name     Sauce Labs Backpack
    Proceed To Checkout
    Fill Checkout Form           ${FIRST_NAME}    ${LAST_NAME}    ${POSTAL_CODE}
    Submit Checkout Step One
    Wait Until Location Contains    checkout-step-two.html
    Complete Order
    Element Text Should Be       ${COMPLETE_HEADER}    Thank you for your order!

TC-13: Verify Checkout Cancellation Redirection
    [Documentation]    FR-13: Cancelling checkout returns user cleanly to cart.
    [Tags]             checkout
    Login As Standard User
    Add Item To Cart By Name     Sauce Labs Backpack
    Proceed To Checkout
    Execute Javascript           document.getElementById('cancel').click();
    Wait Until Location Contains    cart.html

TC-14: Verify Secure User Logout
    [Documentation]    FR-14: User logout securely ends session and returns to login page.
    [Tags]             auth    smoke
    Login As Standard User
    Logout From Application
    Location Should Be           ${BASE_URL}
    Page Should Contain Element  ${LOGIN_BUTTON}
