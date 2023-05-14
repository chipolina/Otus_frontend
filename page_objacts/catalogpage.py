from selenium.webdriver.common.by import By

from page_objacts.basepage import BasePage
from src.helper import CategoryData


class CatalogPage(BasePage):
    CATEGORIES = (By.XPATH, "//a[contains(@class, 'list-group-item')]")
    SORT = (By.XPATH, "//label[@for='input-sort']")
    SORT_SELECT = (By.XPATH, "//*[@id='input-sort']")
    LIMIT = (By.XPATH, "//label[@for='input-limit']")
    LIMIT_SELECT = (By.XPATH, "//*[@id='input-limit']/option")

    def find_categories(self):
        return self.elements(self.CATEGORIES)

    def find_sort(self):
        return self.element(self.CATEGORIES)

    def find_limit(self):
        return self.element(self.CATEGORIES)

    def find_limit_select(self):
        return self.elements(self.CATEGORIES)

    def check_categories_names(self, categories):
        for category in categories:
            assert category.text.split(" (")[0] in [c.value for c in CategoryData]

    def check_limits_select(self, limits_select):
        for limit in limits_select:
            assert int(limit.text) in [10, 25, 50, 75, 100]
