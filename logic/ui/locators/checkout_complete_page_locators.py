from selenium.webdriver.common.by import By


class CheckoutCompletePageLocators:

    COMPLETE_CONTAINER = (By.XPATH, '//div[@class="checkout_complete_container"]')
    COMPLETE_HEADER = (By.XPATH, COMPLETE_CONTAINER[1] + '//h2[@class="complete-header"]')




