from selenium.webdriver.common.by import By

from page_objacts.basepage import BasePage


class ProductPage(BasePage):
    PRICE = (By.XPATH, "//span[@class='price-new']")
    ADD_WISH_LIST = (By.XPATH, "//button[@title='Add to Wish List']")
    ADD_TO_CART = (By.XPATH, "//button[@id='button-cart']")
    QUANTITY = (By.XPATH, "//input[@id='input-quantity']")
    DELIVERY_DATE = (By.XPATH, "//input[@id='input-option-225']")
    CALENDAR = (By.XPATH, "//*[contains(@class, 'daterangepicker')]")

    def find_product_price(self):
        return self.element(self.PRICE)

    def find_add_wl(self):
        return self.element(self.ADD_WISH_LIST)

    def find_add_to_cart(self):
        return self.element(self.ADD_TO_CART)

    def find_quantity(self):
        return self.element(self.QUANTITY)

    def find_delivery_date(self):
        return self.element(self.DELIVERY_DATE)

    def set_delivery_date(self):
        self.find_delivery_date().click()

    def find_calendar(self):
        return self.element(self.CALENDAR)
