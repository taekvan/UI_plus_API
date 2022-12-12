import pytest

from logic.base_case import LoginCase


@pytest.mark.integration
class TestCase(LoginCase):
    @pytest.mark.testit_case_id(2000)
    @pytest.mark.testit_case_title("Integration add one item to the cart")
    def test_add_1_random_item_to_cart(self):
        page = self.page_factory.get_page('main')
        item = page.get_random_item()
        item_name = [page.get_item_title(item)]
        item_price = page.get_item_price(item)
        page.add_item_to_cart(item)
        page.go_to_cart()

        page = self.page_factory.get_page('cart')
        assert page.get_items_amount() == 1
        assert page.get_total_cost() == item_price
        assert page.get_items_name_list() == item_name
        print(item_name)
