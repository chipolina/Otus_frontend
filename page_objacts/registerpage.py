from selenium.webdriver.common.by import By

from page_objacts.basepage import BasePage


class RegistertPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@id='input-firstname']")
    POLICY = (By.XPATH, "//input[@name='agree']")
    PAGE_MAIN_TITLE = (By.XPATH, "//*[@id='content']/h1")
    REQUIRED_FIELDS = (By.XPATH, "//div[contains(@class,'required')]")
    MENU_SECTIONS = (By.XPATH, "//a[@class='list-group-item']")

    def find_title(self):
        return self.element(self.PAGE_MAIN_TITLE)

    def find_first_name(self):
        return self.element(self.FIRST_NAME)

    def find_req_fields(self):
        return self.elements(self.REQUIRED_FIELDS)

    def find_policy(self):
        return self.element(self.POLICY)

    def find_menu_sections(self):
        return self.elements(self.MENU_SECTIONS)
