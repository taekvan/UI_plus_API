from selenium.webdriver.remote.webelement import WebElement


class ButtonElement(WebElement):

    def get_name(self):
        return self.get_attribute('value')

    def button_click(self):
        self.click()

