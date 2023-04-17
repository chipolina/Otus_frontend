import time

from locators.locators_main_page import MainPageLocators, CatalogPageLocators, ProductPageLocators, RegisterPageLocators
from src.helper import CategoryData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def te1st_check_main_page_elements(browser, base_url):
    browser.get(base_url)

    currency = browser.find_element(*MainPageLocators.CURRENCY)
    search_btn = browser.find_element(*MainPageLocators.SEARCH_BUTTON)
    cart_btn = browser.find_element(*MainPageLocators.CART_BUTTON)
    product_cards = browser.find_elements(*MainPageLocators.PRODUCT_CARD)
    top_navigation_items = browser.find_elements(*MainPageLocators.TOP_NAVIGATION_ITEMS)

    assert currency.text == 'Currency'
    assert search_btn.is_enabled()
    assert cart_btn.is_enabled()
    assert len(product_cards) == 4
    assert len(top_navigation_items) == 8


def te1st_check_catalog_elements(browser, base_url):
    browser.get(base_url + "catalog/tablet")
    categories = browser.find_elements(*CatalogPageLocators.CATEGORIES)

    sort = browser.find_element(*CatalogPageLocators.SORT)
    limit = browser.find_element(*CatalogPageLocators.LIMIT)
    limits_select = browser.find_elements(*CatalogPageLocators.LIMIT_SELECT)

    assert len(categories) == 8
    for category in categories:
        assert category.text.split(" (")[0] in [c.value for c in CategoryData]
    assert sort.is_enabled()
    assert limit.is_enabled()
    for limit in limits_select:
        assert int(limit.text) in [10, 25, 50, 75, 100]


def te1st_check_product_card(browser, base_url):
    browser.get(base_url + "product/laptop-notebook/hp-lp3065")

    product_price = browser.find_element(*ProductPageLocators.PRICE)
    add_wl = browser.find_element(*ProductPageLocators.ADD_WISH_LIST)
    add_to_cart = browser.find_element(*ProductPageLocators.ADD_TO_CART)
    quantity = browser.find_element(*ProductPageLocators.QUANTITY)
    delivery_date = browser.find_element(*ProductPageLocators.DELIVERY_DATE)
    delivery_date.click()
    calendar = browser.find_element(*ProductPageLocators.CALENDAR)

    assert product_price.is_displayed()
    assert add_wl.is_enabled()
    assert add_to_cart.is_enabled()
    assert quantity.get_property('value') == '1'
    assert delivery_date.get_property('value') == "2011-04-22"
    assert calendar.is_displayed()


def test_registration_page(browser, base_url):
    browser.get(base_url + "?route=account/register")
    page_main_title = browser.find_element(*RegisterPageLocators.PAGE_MAIN_TITLE)
    first_name = browser.find_element(*RegisterPageLocators.FIRST_NAME)
    required_fields = browser.find_elements(*RegisterPageLocators.REQUIRED_FIELDS)
    policy = browser.find_element(*RegisterPageLocators.POLICY)
    menu_sections = browser.find_element(*RegisterPageLocators.MENU_SECTIONS)

    assert page_main_title.text == "Register Account"
    assert first_name.get_property("placeholder") == "First Name"
    assert not policy.is_selected()
    assert len(required_fields) == 4
    assert len(menu_sections) == 13
