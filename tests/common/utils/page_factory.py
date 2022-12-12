from logic.ui.pages.cart_page import CartPage
from logic.ui.pages.checkout_complete_page import CheckoutCompletePage
from logic.ui.pages.checkout_overview_page import CheckoutOverviewPage
from logic.ui.pages.checkout_page import CheckoutPage
from logic.ui.pages.login_page import LoginPage
from logic.ui.pages.main_page import MainPage
from logic.ui.pages.basket_page import BasketPage


class CartOverviewPage:
    pass


PAGES = {
    'main_page': MainPage,
    'login_page': LoginPage,
    'basket_page': BasketPage,
    'cart_page': CartPage,
    'checkout_page': CheckoutPage,
    'checkout_overview_page': CheckoutOverviewPage,
    'checkout_complete_page': CheckoutCompletePage,

}


class PageFactory:

    def __init__(self, driver, waits, actions, reporter, config):
        self.driver = driver
        self.actions = actions
        self.reporter = reporter
        self.config = config
        self.waits = waits

    def get_page(self, page_name):
        page_name = f'{page_name}_page'
        page_name = page_name.lower()
        if page_name not in PAGES:
            raise ValueError(f'The page {page_name} in not defined')
        page = PAGES[page_name](driver=self.driver,
                                waits=self.waits,
                                actions=self.actions,
                                reporter=self.reporter,
                                config=self.config
                                )
        return page
