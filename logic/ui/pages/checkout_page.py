from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from logic.common.common import generate_random_person
from logic.ui.elements.base.button_element import ButtonElement
from logic.ui.elements.base.error_container_element import ErrorContainerElement
from logic.ui.elements.base.input_element import InputElement
from logic.ui.locators.checkout_page_locators import CheckoutPageLocators
from logic.ui.locators.login_page_locators import LoginPageLocators
from webium.find import Find

from selenium.webdriver.remote.webelement import WebElement

from logic.ui.pages.base_page import BasePage


class CheckoutPage(BasePage):

    # username_input = Find(InputElement, By.XPATH, LoginPageLocators.USERNAME_INPUT[1])
    # password_input = Find(InputElement, by=By.XPATH, value=LoginPageLocators.PASSWORD_INPUT[1])
    # login_btn = Find(ButtonElement, by=By.XPATH, value=LoginPageLocators.LOGIN_BTN[1])
    #
    # error_notification = Find(ErrorContainerElement, by=By.XPATH, value=LoginPageLocators.ERROR_MSG_CONTAINER_TEXT[1])

    # def login(self, username, password):
    #     self.username_input.set_value(username)
    #     self.password_input.set_value(password)
    #     self.login_btn.button_click()
    #
    # def get_login_error_text(self):
    #     self.error_notification.get_text()

    def fill_random_information(self):
        random_person = generate_random_person()
        self.fill_first_name(random_person['name'])
        self.fill_last_name(random_person['surname'])
        self.fill_post_code(random_person['zip'])


    def fill_first_name(self, first_name):
        self.actions.set_value(CheckoutPageLocators.FIRST_NAME_INPUT, first_name)

    def fill_last_name(self, last_name):
        self.actions.set_value(CheckoutPageLocators.LAST_NAME_INPUT, last_name)

    def fill_post_code(self, post_code):
        self.actions.set_value(CheckoutPageLocators.ZIP_INPUT, post_code)

    def click_continue_btn(self):
        self.actions.click_with_wait(CheckoutPageLocators.CONTINUE_BTN)

