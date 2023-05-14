from selenium.webdriver.common.by import By

from page_objacts.basepage import BasePage


class CatalogPage(BasePage):
    CATEGORIES = (By.XPATH, "//a[contains(@class, 'list-group-item')]")
    SORT = (By.XPATH, "//label[@for='input-sort']")
    SORT_SELECT = (By.XPATH, "//*[@id='input-sort']")
    LIMIT = (By.XPATH, "//label[@for='input-limit']")
    LIMIT_SELECT = (By.XPATH, "//*[@id='input-limit']/option")

    def find_categories(self):
        return self.elements(*self.CATEGORIES)

    def find_sort(self):
        return self.element(*self.CATEGORIES)

    def find_limit(self):
        return self.element(*self.CATEGORIES)

    def find_limit_select(self):
        return self.elements(*self.CATEGORIES)
