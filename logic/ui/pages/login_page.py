from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from logic.ui.elements.base.button_element import ButtonElement
from logic.ui.elements.base.error_container_element import ErrorContainerElement
from logic.ui.elements.base.input_element import InputElement
from logic.ui.locators.login_page_locators import LoginPageLocators
from webium.find import Find

from selenium.webdriver.remote.webelement import WebElement

from logic.ui.pages.base_page import BasePage
from logic.ui.pages.main_page import MainPage


class LoginPage(MainPage):

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

    def login_page_is_displayed(self):
        try:
            self.waits.wait_for_element_visibility(LoginPageLocators.LOGO_PIC)
            return True
        except TimeoutException:
            return False

    def fill_username(self, username):
        self.actions.set_value(LoginPageLocators.USERNAME_INPUT, username)

    def fill_password(self, password):
        self.actions.set_value(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_btn(self):
        self.actions.click_with_wait(LoginPageLocators.LOGIN_BTN)

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_btn()

    def get_login_error_text(self):
        return self.actions.get_text(LoginPageLocators.ERROR_MSG_CONTAINER_TEXT)

    def is_username_field_visible(self):
        self.waits.wait_for_element_visibility(LoginPageLocators.USERNAME_INPUT)
        return self.actions.is_element_displayed(LoginPageLocators.USERNAME_INPUT)

    def get_username_field_placeholder(self):
        return self.actions.get_placeholder(LoginPageLocators.USERNAME_INPUT)

    def is_password_field_visible(self):
        self.waits.wait_for_element_visibility(LoginPageLocators.PASSWORD_INPUT)
        return self.actions.is_element_displayed(LoginPageLocators.PASSWORD_INPUT)

    def get_password_field_placeholder(self):
        return self.actions.get_placeholder(LoginPageLocators.PASSWORD_INPUT)

    def is_login_btn_visible(self):
        self.waits.wait_for_element_visibility(LoginPageLocators.LOGIN_BTN)
        return self.actions.is_element_displayed(LoginPageLocators.LOGIN_BTN)

    def get_login_btn_name(self):
        return self.actions.get_value(LoginPageLocators.LOGIN_BTN)
