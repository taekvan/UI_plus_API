from selenium.webdriver.common.by import By


class MainPageLocators:

    # HEADER

    HEADER_CONTAINER = (By.XPATH, '//div[@id="header_container"]')
    PRIMARY_HEADER = (By.XPATH, HEADER_CONTAINER[1] + '/div[@class="primary_header"]')
    BASKET_BTN = (By.XPATH, PRIMARY_HEADER[1] + '//div[@class="shopping_cart_container"]/a')

    SECONDARY_HEADER = (By.XPATH, HEADER_CONTAINER[1] + '/div[@class="header_secondary_container"]')
    SECONDARY_HEADER_TITLE = (By.XPATH, SECONDARY_HEADER[1] + '/span[@class="title"]')

    # ITEMS
    INVENTORY_LIST = (By.XPATH, '//div[@class="inventory_list"]')
    ITEM_CONTAINER = (By.XPATH, INVENTORY_LIST[1] + '//div[@class="inventory_item"]')
    ITEM_DESCRIPTION = (By.XPATH,  './/div[@class="inventory_item_description"]')
    ITEM_TITLE = (By.XPATH, ITEM_DESCRIPTION[1] + '//div[@class="inventory_item_name"]')

    ITEM_PRICEBAR = (By.XPATH, ITEM_DESCRIPTION[1] + '//div[@class="pricebar"]')
    ITEM_PRICE = (By.XPATH, ITEM_PRICEBAR[1] + '/div[@class="inventory_item_price"]')
    ITEM_ADD_TO_CART_BTN = (By.XPATH, ITEM_PRICEBAR[1] + '/button[contains(text(), "Add to cart")]')
    ITEM_REMOVE_BTN = (By.XPATH, ITEM_PRICEBAR[1] + '/button[contains(text(), "Remove")]')
