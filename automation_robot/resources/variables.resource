*** Settings ***
Documentation    Variables and locators for SauceDemo Robot Framework Test Automation.
...              Course: CST8513 - Quality Assurance and Testing (Assignment III)
...              Students: Devangbhai Pandit & Meet Ahalpara

*** Variables ***
${BASE_URL}                  https://www.saucedemo.com/
${BROWSER}                   chrome
${DELAY}                     0s
${TIMEOUT}                   10s

# Credentials
${VALID_USER}                standard_user
${VALID_PASSWORD}            secret_sauce
${INVALID_USER}              wrong_user
${INVALID_PASSWORD}          wrong_password
${LOCKED_USER}               locked_out_user

# Checkout Test Data
${FIRST_NAME}                Meet
${LAST_NAME}                 Ahalpara
${POSTAL_CODE}               K2G 1V8

# Locators - Login
${LOGIN_USERNAME_INPUT}      id=user-name
${LOGIN_PASSWORD_INPUT}      id=password
${LOGIN_BUTTON}              id=login-button
${LOGIN_ERROR_BANNER}        css=h3[data-test='error']

# Locators - Inventory
${PAGE_TITLE}                class=title
${INVENTORY_ITEM}            class=inventory_item
${SORT_DROPDOWN}             class=product_sort_container
${ACTIVE_SORT_LABEL}         class=active_option
${CART_ICON}                 class=shopping_cart_link
${CART_BADGE}                class=shopping_cart_badge
${BURGER_MENU_BUTTON}        id=react-burger-menu-btn
${LOGOUT_LINK}               id=logout_sidebar_link

# Locators - Product Details
${DETAILS_NAME}              class=inventory_details_name
${DETAILS_PRICE}             class=inventory_details_price
${BACK_TO_PRODUCTS_BTN}      id=back-to-products

# Locators - Cart
${CART_ITEM}                 class=cart_item
${CONTINUE_SHOPPING_BTN}     id=continue-shopping
${CHECKOUT_BUTTON}           id=checkout

# Locators - Checkout
${CHECKOUT_FIRST_NAME}       id=first-name
${CHECKOUT_LAST_NAME}        id=last-name
${CHECKOUT_POSTAL_CODE}      id=postal-code
${CHECKOUT_CONTINUE_BTN}     id=continue
${CHECKOUT_CANCEL_BTN}       id=cancel
${CHECKOUT_FINISH_BTN}       id=finish
${CHECKOUT_ERROR_BANNER}     css=h3[data-test='error']
${SUBTOTAL_LABEL}            class=summary_subtotal_label
${TAX_LABEL}                 class=summary_tax_label
${TOTAL_LABEL}               class=summary_total_label
${COMPLETE_HEADER}           class=complete-header
