from selenium.webdriver.common.by import By


class CartPageLocators:


    CART_LIST = (By.XPATH, '//div[@class="cart_list"]')
    CART_ITEM = (By.XPATH, CART_LIST[1] + '/div[@class="cart_item"]')
    CART_ITEM_TITLE = (By.XPATH, './/div[@class="inventory_item_name"]')
    CART_ITEM_PRICE = (By.XPATH, './/div[@class="inventory_item_price"]')

    CHECKOUT_BTN = (By.XPATH, '//button[@id="checkout"]')
