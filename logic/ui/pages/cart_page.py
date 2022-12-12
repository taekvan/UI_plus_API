from logic.ui.locators.cart_page_locators import CartPageLocators
from logic.ui.locators.main_page_locators import MainPageLocators
from logic.ui.pages.base_page import BasePage


class CartPage(BasePage):

    def get_items_amount(self):
        items_list = self.actions.find_elements_with_wait(CartPageLocators.CART_LIST)
        return len(items_list)

    def get_total_cost(self):
        items_list = self.actions.find_elements_with_wait(CartPageLocators.CART_LIST)
        total_cost = 0
        for element in items_list:
            element_price = self.actions.get_element_text(
                self.actions.find_inner_element(element, CartPageLocators.CART_ITEM_PRICE))
            total_cost += float(element_price.replace('$', ''))

        return total_cost

    def get_items_name_list(self):
        items_list = self.actions.find_elements_with_wait(CartPageLocators.CART_LIST)
        items_name_list = []
        for element in items_list:
            element_name = self.actions.get_element_text(
                self.actions.find_inner_element(element, CartPageLocators.CART_ITEM_TITLE))
            items_name_list.append(element_name)
        return items_name_list

    def checkout(self):
        self.actions.click_with_wait(CartPageLocators.CHECKOUT_BTN)

