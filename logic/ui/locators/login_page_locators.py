from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOGO_PIC = (By.XPATH, '//div[@class="login_logo"]')
    LOGIN_WRAPPER = (By.XPATH, '//div[@class="login_wrapper-inner"]')
    USERNAME_INPUT = (By.XPATH, LOGIN_WRAPPER[1] + '//input[@id="user-name"]')
    PASSWORD_INPUT = (By.XPATH, LOGIN_WRAPPER[1] + '//input[@id="password"]')

    ERROR_MSG_CONTAINER = (By.XPATH, LOGIN_WRAPPER[1] + '//div[contains(@class, "error-message-container")]')
    ERROR_MSG_CONTAINER_TEXT = (By.XPATH, ERROR_MSG_CONTAINER[1] + '//h3[@data-test="error"]')
    ERROR_BTN = (By.XPATH, ERROR_MSG_CONTAINER[1] + '//button[@class="error-button"]')

    LOGIN_BTN = (By.XPATH, LOGIN_WRAPPER[1] + '//input[@id="login-button"]')
