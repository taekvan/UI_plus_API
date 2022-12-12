from selenium.webdriver import Keys


class Actions:
    def __init__(self, driver, waits):
        self.driver = driver
        self._waits = waits

    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @staticmethod
    def clear_field(element):
        element.click()
        element.clear()

    def set_value(self, locator: tuple, value: str) -> None:
        element = self._waits.wait_for_element(locator=locator)
        self.clear_field(element)
        element.send_keys(value)
        element.send_keys(Keys.TAB)

    def click(self, locator: tuple) -> None:
        element = self.find_element(locator=locator)
        element.click()

    def click_with_wait(self, locator: tuple) -> None:
        element = self._waits.wait_for_element(locator=locator)
        element.click()

    def is_element_present(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) == 1

    def is_element_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    def get_placeholder(self, locator):
        element = self._waits.wait_for_element_visibility(locator)
        return element.get_attribute(name='placeholder')

    def get_value(self, locator):
        element = self._waits.wait_for_element_visibility(locator)
        return element.get_attribute(name='value')

    def get_text(self, locator):
        element = self._waits.wait_for_element_visibility(locator)
        return element.text

    @staticmethod
    def get_element_text(element):
        return element.text

    @staticmethod
    def find_inner_element(element, locator):
        inner_element = element.find_element(*locator)
        return inner_element

    def find_elements_with_wait(self, locator):
        self._waits.wait_for_element_visibility(locator)
        return self.driver.find_elements(*locator)