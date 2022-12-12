from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class InputElement(WebElement):

    def get_value(self):
        return self.get_attribute('value')

    def get_placeholder(self):
        return self.get_attribute('placeholder')

    def clear_field(self):
        self.click()
        self.clear()

    def set_value(self, value):
        self.clear_field()

        self.send_keys(value)

        self.send_keys(Keys.TAB)
