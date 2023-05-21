import time

from selenium.webdriver.common.by import By

from page_objacts.basepage import BasePage
from src.helper import generate_text, generate_email


class RegistertPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@id='input-firstname']")
    LAST_NAME = (By.XPATH, "//input[@id='input-lastname']")
    EMAIL = (By.XPATH, "//input[@id='input-email']")
    PASSWORD = (By.XPATH, "//input[@id='input-password']")
    CONTINUE_BTN = (By.XPATH, "//button[@type= 'submit']")

    POLICY = (By.XPATH, "//input[@name='agree']")
    PAGE_MAIN_TITLE = (By.XPATH, "//*[@id='content']/h1")
    REQUIRED_FIELDS = (By.XPATH, "//div[contains(@class,'required')]")
    MENU_SECTIONS = (By.XPATH, "//a[@class='list-group-item']")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//*[@id='content']/h1")

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

    def create_random_user(self):
        self.element(self.FIRST_NAME).send_keys(generate_text(7))
        self.element(self.LAST_NAME).send_keys(generate_text(7))
        self.element(self.EMAIL).send_keys(generate_email())
        self.element(self.PASSWORD).send_keys(generate_text(7))
        time.sleep(1)
        self.element(self.POLICY).click()
        self.element(self.CONTINUE_BTN).click()
        time.sleep(1)
        self.check_element_text(self.ACCOUNT_CREATED_TEXT, "Your Account Has Been Created!")


