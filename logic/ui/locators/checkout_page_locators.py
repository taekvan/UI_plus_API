from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    INPUT_FIELDS_WRAPPER = (By.XPATH, '//div[@class="checkout_info"]')
    FIRST_NAME_INPUT = (By.XPATH, INPUT_FIELDS_WRAPPER[1] + '//input[@id="first-name"]')
    LAST_NAME_INPUT = (By.XPATH, INPUT_FIELDS_WRAPPER[1] + '//input[@id="last-name"]')
    ZIP_INPUT = (By.XPATH, INPUT_FIELDS_WRAPPER[1] + '//input[@id="postal-code"]')
    CONTINUE_BTN = (By.XPATH, '//input[@id="continue"]')


