from logic.ui.locators.checkout_overview_page_locators import CheckoutOverviewPageLocators
from logic.ui.pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):

    def finish_payment(self):
        self.actions.click_with_wait(CheckoutOverviewPageLocators.FINISH_BTN)
