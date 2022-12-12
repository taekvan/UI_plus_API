import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.common.utils.actions import Actions
from tests.common.utils.reporter import Reporter
from tests.common.utils.waits import Waits


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    url = config['url']

    if browser == 'chrome':
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(service=service, options=options)

    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.close()


# @pytest.fixture
# def base_page(driver):
#     return BasePage(driver=driver)
#
#
# @pytest.fixture
# def login_page(driver):
#     return LoginPage(driver=driver)


@pytest.fixture
def waits(driver, config):
    return Waits(driver, config)


@pytest.fixture
def actions(driver, waits):
    return Actions(driver, waits)


@pytest.fixture
def reporter(driver, config):
    return Reporter(driver, config)
