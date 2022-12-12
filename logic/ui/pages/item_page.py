from selenium.webdriver.common.by import By

from logic.ui.elements.base.button_element import ButtonElement
from logic.ui.elements.base.input_element import InputElement
from logic.ui.locators.login_page_locators import LoginPageLocators
from webium.find import Find
from webium import BasePage
from selenium.webdriver.remote.webelement import WebElement



class ItemPage(BasePage):
    url = 'https://www.saucedemo.com/'

    username_input = Find(InputElement, By.XPATH, LoginPageLocators.USERNAME_INPUT[1])
    password_input = Find(InputElement, by=By.XPATH, value=LoginPageLocators.PASSWORD_INPUT[1])
    login_btn = Find(ButtonElement, by=By.XPATH, value=LoginPageLocators.LOGIN_BTN[1])
