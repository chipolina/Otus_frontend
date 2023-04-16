from selenium.webdriver.common.by import By


class MainPageLocators:
    CURRENCY = (By.XPATH, "//*[@id='form-currency']/div/a/span")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search']/button")
    CART_BUTTON = (By.XPATH, "//*[@id='header-cart']/div/button")
    PRODUCT_CARD = (By.XPATH, "//*[@class='product-thumb']")
    TOP_NAVIGATION_ITEMS = (By.XPATH, "//li[contains(@class, 'nav-item')]")

class CatalogPageLocators:
    CATEGORIES = (By.XPATH, "//a[@class='list-group-item']")