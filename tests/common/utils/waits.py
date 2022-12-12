from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.timeout = config['timeout']
        self._wait = WebDriverWait(self.driver, self.timeout)

    def wait_for_element(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator=locator))

    def wait_for_element_visibility(self, locator: tuple):
        return self._wait.until(EC.visibility_of_element_located(locator=locator))


