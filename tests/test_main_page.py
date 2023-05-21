import pytest

from page_objacts.catalogpage import CatalogPage
from page_objacts.productpage import ProductPage
from page_objacts.registerpage import RegistertPage
from page_objacts.mainpage import MainPage


def test_check_main_page_elements(browser, base_url):
    browser.get(base_url)

    MainPage(browser).check_element_text(MainPage.CURRENCY, 'Currency')
    MainPage(browser).check_enable_element(MainPage.SEARCH_BUTTON)
    MainPage(browser).check_enable_element(MainPage.CART_BUTTON)
    MainPage(browser).check_len_elements(MainPage.PRODUCT_CARD, 4)
    MainPage(browser).check_len_elements(MainPage.TOP_NAVIGATION_ITEMS, 8)


def test_check_catalog_elements(browser, base_url):
    browser.get(base_url + "catalog/tablet")

    categories = CatalogPage(browser).find_categories()
    limits_select = CatalogPage(browser).find_limit_select()

    CatalogPage(browser).check_len_elements(CatalogPage.CATEGORIES, 8)
    CatalogPage(browser).check_enable_element(CatalogPage.SORT)
    CatalogPage(browser).check_enable_element(CatalogPage.LIMIT)
    CatalogPage(browser).check_categories_names(categories)
    CatalogPage(browser).check_limits_select(limits_select)


def test_check_product_card(browser, base_url):
    browser.get(base_url + "product/laptop-notebook/hp-lp3065")

    ProductPage(browser).check_display_element(ProductPage.PRICE)
    ProductPage(browser).check_enable_element(ProductPage.ADD_WISH_LIST)
    ProductPage(browser).check_enable_element(ProductPage.ADD_TO_CART)
    ProductPage(browser).check_element_property(ProductPage.QUANTITY, 'value', '1')
    ProductPage(browser).check_element_property(ProductPage.DELIVERY_DATE, 'value', '2011-04-22')
    ProductPage(browser).set_delivery_date()
    ProductPage(browser).check_display_element(ProductPage.CALENDAR)


def test_registration_page(browser, base_url):
    browser.get(base_url + "?route=account/register")

    RegistertPage(browser).check_element_text(RegistertPage.PAGE_MAIN_TITLE, "Register Account")
    RegistertPage(browser).check_element_property(RegistertPage.FIRST_NAME, "placeholder", "First Name")
    RegistertPage(browser).check_is_not_selected(RegistertPage.POLICY)
    RegistertPage(browser).check_len_elements(RegistertPage.REQUIRED_FIELDS, 4)
    RegistertPage(browser).check_len_elements(RegistertPage.MENU_SECTIONS, 13)


def test_add_new_product(browser): ...


def test_remove_product(browser): ...


def test_register_new_user(browser, base_url):
    browser.get(base_url + "?route=account/register")
    RegistertPage(browser).create_random_user()


def test_switch_currency(browser, base_url):
    browser.get(base_url)
    MainPage(browser).change_currency("GBP")
