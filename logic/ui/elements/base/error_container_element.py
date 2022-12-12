from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from webium import Find

from logic.ui.elements.base.button_element import ButtonElement
from logic.ui.locators.login_page_locators import LoginPageLocators


class ErrorContainerElement(WebElement):

    # error_btn = Find(ButtonElement, By.XPATH, '.')

    def get_login_error_text(self):
        return self.text


