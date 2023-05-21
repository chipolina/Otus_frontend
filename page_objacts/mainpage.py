from selenium.webdriver.common.by import By

from page_objacts.basepage import BasePage
from src.helper import CurrencyIcons


class MainPage(BasePage):
    CURRENCY = (By.XPATH, "//*[@id='form-currency']/div/a/span")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search']/button")
    CART_BUTTON = (By.XPATH, "//*[@id='header-cart']/div/button")
    PRODUCT_CARD = (By.XPATH, "//*[@class='product-thumb']")
    TOP_NAVIGATION_ITEMS = (By.XPATH, "//li[contains(@class, 'nav-item')]")
    CURRENCY_LIST = (By.XPATH, "//ul[@class= 'dropdown-menu show']/li")
    CURRENCY_ELEMENT = (By.XPATH, "//a[@class='dropdown-item']")
    CURRENCY_SYMBOL = (By.XPATH, "//a[@class= 'dropdown-toggle']/strong")

    def find_currency(self):
        return self.element(self.CURRENCY)

    def find_search_btn(self):
        return self.element(self.SEARCH_BUTTON)

    def find_cart_btn(self):
        return self.element(self.CART_BUTTON)

    def find_product_cards(self):
        return self.elements(self.PRODUCT_CARD)

    def find_top_navigation_items(self):
        return self.elements(self.TOP_NAVIGATION_ITEMS)

    def select_currency(self, currency):
        return self.driver.find_element(By.XPATH, f"//a[@href= '{currency}']")

    def change_currency(self, currency):
        self.element(self.CURRENCY).click()
        self.elements(self.CURRENCY_LIST)
        self.select_currency(currency).click()
        currency_icon = CurrencyIcons[currency].value
        self.check_element_text(self.CURRENCY_SYMBOL, currency_icon)
