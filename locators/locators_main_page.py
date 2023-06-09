from selenium.webdriver.common.by import By


class MainPageLocators:
    CURRENCY = (By.XPATH, "//*[@id='form-currency']/div/a/span")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='search']/button")
    CART_BUTTON = (By.XPATH, "//*[@id='header-cart']/div/button")
    PRODUCT_CARD = (By.XPATH, "//*[@class='product-thumb']")
    TOP_NAVIGATION_ITEMS = (By.XPATH, "//li[contains(@class, 'nav-item')]")


class CatalogPageLocators:
    CATEGORIES = (By.XPATH, "//a[contains(@class, 'list-group-item')]")
    SORT = (By.XPATH, "//label[@for='input-sort']")
    SORT_SELECT = (By.XPATH, "//*[@id='input-sort']")
    LIMIT = (By.XPATH, "//label[@for='input-limit']")
    LIMIT_SELECT = (By.XPATH, "//*[@id='input-limit']/option")


class ProductPageLocators:
    PRICE = (By.XPATH, "//span[@class='price-new']")
    ADD_WISH_LIST = (By.XPATH, "//button[@title='Add to Wish List']")
    ADD_TO_CART = (By.XPATH, "//button[@id='button-cart']")
    QUANTITY = (By.XPATH, "//input[@id='input-quantity']")
    DELIVERY_DATE = (By.XPATH, "//input[@id='input-option-225']")
    CALENDAR = (By.XPATH, "//*[contains(@class, 'daterangepicker')]")


class RegisterPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@id='input-firstname']")
    POLICY = (By.XPATH, "//input[@name='agree']")
    PAGE_MAIN_TITLE = (By.XPATH, "//*[@id='content']/h1")
    REQUIRED_FIELDS = (By.XPATH, "//div[contains(@class,'required')]")
    MENU_SECTIONS = (By.XPATH, "//a[@class='list-group-item']")
