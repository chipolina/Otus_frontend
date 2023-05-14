from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элемент {locator} не видно на странице")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элементы {locator} не видны на странице")

    def check_len_elements(self, locator, number):
        assert len(self.elements(locator)) == number

    def check_enable_element(self, locator):
        self.element(locator).is_enabled()

    def check_element_text(self, locator, text):
        self.element(locator).text(text)
