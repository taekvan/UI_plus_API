from logic.ui.locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver, waits, actions, reporter, config):
        self.driver = driver
        self.waits = waits
        self.actions = actions
        self.reporter = reporter
        self.config = config


