import pytest

from logic.ui.pages.base_page import BasePage


from tests.common.utils.page_factory import PageFactory


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, waits, actions, reporter, config):
        self.driver = driver
        self.config = config
        self.waits = waits
        self.actions = actions
        self.reporter = reporter

        self.base_page = BasePage(self.driver, waits, actions, reporter, config)
        self.page_factory = PageFactory(driver=self.driver,
                                        waits=self.waits,
                                        actions=self.actions,
                                        reporter=self.reporter,
                                        config=self.config,
                                        )


class LoginCase(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def login(self, setup):
        page = self.page_factory.get_page('login')
        page.login(self.config['standart_user'], self.config['standart_password'])
        page = self.page_factory.get_page('main')
        assert page.get_page_title() == 'PRODUCTS', \
            f'Page Products should be opened'
