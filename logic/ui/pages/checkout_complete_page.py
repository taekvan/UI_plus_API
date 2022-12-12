from logic.ui.locators.checkout_complete_page_locators import CheckoutCompletePageLocators
from logic.ui.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):

    def is_purchase_successful(self):
        header = self.actions.get_text(CheckoutCompletePageLocators.COMPLETE_HEADER)
        return header == 'THANK YOU FOR YOUR ORDER'


