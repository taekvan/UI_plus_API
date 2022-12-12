import pytest

from logic.base_case import LoginCase


@pytest.mark.smoke
class TestCase(LoginCase):

    @pytest.mark.testit_case_id(3000)
    @pytest.mark.testit_case_title("E2E successful buy one item")
    def test_buy_one_item(self):
        page = self.page_factory.get_page('main')
        item = page.get_random_item()
        page.add_item_to_cart(item)
        page.go_to_cart()
        page = self.page_factory.get_page('cart')
        page.checkout()
        page = self.page_factory.get_page('checkout')
        page.fill_random_information()
        page.click_continue_btn()
        page = self.page_factory.get_page('checkout_overview')
        page.finish_payment()

        page = self.page_factory.get_page('checkout_complete')
        assert page.is_purchase_successful()
