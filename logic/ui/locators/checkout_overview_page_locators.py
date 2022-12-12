from selenium.webdriver.common.by import By


class CheckoutOverviewPageLocators:

    CART_FOOTER = (By.XPATH, '//div[@class="cart_footer"]')
    FINISH_BTN = (By.XPATH, CART_FOOTER[1] + '//button[@id="finish"]')


