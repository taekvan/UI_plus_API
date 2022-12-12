from logic.ui.locators.main_page_locators import MainPageLocators
from logic.ui.pages.base_page import BasePage
import random


class MainPage(BasePage):

    def go_to_cart(self):
        self.actions.click_with_wait(MainPageLocators.BASKET_BTN)

    def add_item_to_cart(self, item):
        add_to_cart_btn = self.actions.find_inner_element(item, MainPageLocators.ITEM_ADD_TO_CART_BTN)
        add_to_cart_btn.click()

    def get_random_item(self):
        items = self.actions.find_elements_with_wait(MainPageLocators.ITEM_CONTAINER)
        return items[random.randint(0, len(items)-1)]

    def get_item_title(self, item):
        item_title = self.actions.find_inner_element(item, MainPageLocators.ITEM_TITLE)
        return self.actions.get_element_text(item_title)

    # def add_random_item_to_cart_and(self):
    #     items = self.waits.wait_for_element_visibility(MainPageLocators.ITEM_CONTAINER)
    #     random_element = items[1]
    #     random_element_price = self.get_item_price(random_element)
    #     self.add_item_to_cart(random_element_price)
    #     self.actions.click_with_wait(MainPageLocators.BASKET_BTN)

    def get_page_title(self):
        return self.actions.get_text(MainPageLocators.SECONDARY_HEADER_TITLE)

    def get_item_price(self, item):
        item_price = self.actions.find_inner_element(item, MainPageLocators.ITEM_PRICE)
        return float(self.actions.get_element_text(item_price).replace('$', ''))
