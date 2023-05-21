from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element(self, locator: tuple) -> WebElement:
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элемент {locator} не видно на странице")

    def elements(self, locator: tuple)-> WebElement:
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элементы {locator} не видны на странице")

    def check_len_elements(self, locator, number):
        assert len(self.elements(locator)) == number

    def check_enable_element(self, locator):
        self.element(locator).is_enabled()

    def check_element_text(self, locator, text):
        assert self.element(locator).text == text

    def check_element_property(self, locator, prop, value):
        assert self.element(locator).get_property(prop) == value

    def check_display_element(self, locator):
        self.element(locator).is_displayed()

    def check_is_not_selected(self, locator):
        assert not self.element(locator).is_selected()
