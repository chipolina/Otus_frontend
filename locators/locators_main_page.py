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



