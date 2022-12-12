from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class TextElement(WebElement):

    def get_value(self):
        return self.text

