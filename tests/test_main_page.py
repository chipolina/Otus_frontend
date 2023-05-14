import pytest

from page_objacts.catalogpage import CatalogPage
from page_objacts.productpage import ProductPage
from page_objacts.registerpage import RegistertPage
from src.helper import CategoryData
from page_objacts.mainpage import MainPage

@pytest.mark.test
def test_check_main_page_elements(browser, base_url):
    browser.get(base_url)

    currency = MainPage(browser).find_currency()
    search_btn = MainPage(browser).find_search_btn()
    cart_btn = MainPage(browser).find_cart_btn()
    product_cards = MainPage(browser).find_product_cards()
    top_navigation_items = MainPage(browser).find_top_navigation_items()

    MainPage(browser).check_element_text(MainPage.CURRENCY, 'Currency')
    MainPage(browser).check_enable_element(MainPage.SEARCH_BUTTON)
    MainPage(browser).check_enable_element(MainPage.CART_BUTTON)
    MainPage(browser).check_len_elements(MainPage.PRODUCT_CARD, 4)
    MainPage(browser).check_len_elements(MainPage.TOP_NAVIGATION_ITEMS, 8)


def test_check_catalog_elements(browser, base_url):
    browser.get(base_url + "catalog/tablet")
    categories = CatalogPage(browser).find_categories()

    sort = CatalogPage(browser).find_sort()
    limit = CatalogPage(browser).find_limit()
    limits_select = CatalogPage(browser).find_limit_select()

    CatalogPage(browser).check_len_elements(categories, 8)
    CatalogPage(browser).check_enable_element(sort)
    CatalogPage(browser).check_enable_element(limit)
    CatalogPage(browser).check_categories_names(categories)
    CatalogPage(browser).check_limits_select(limits_select)
    # for category in categories:
    #     assert category.text.split(" (")[0] in [c.value for c in CategoryData]
    # for limit in limits_select:
    #     assert int(limit.text) in [10, 25, 50, 75, 100]


def test_check_product_card(browser, base_url):
    browser.get(base_url + "product/laptop-notebook/hp-lp3065")

    product_price = ProductPage(browser).find_product_price()
    add_wl = ProductPage(browser).find_add_wl()
    add_to_cart = ProductPage(browser).find_add_to_cart()
    quantity = ProductPage(browser).find_quantity()
    delivery_date = ProductPage(browser).set_delivery_date()
    calendar = ProductPage(browser).find_calendar()

    ProductPage(browser).check_display_element(product_price)
    ProductPage(browser).check_enable_element(add_wl)
    ProductPage(browser).check_enable_element(add_to_cart)
    ProductPage(browser).check_element_property(quantity, 'value', '1')
    ProductPage(browser).check_element_property(delivery_date, 'value', '2011-04-22')
    ProductPage(browser).check_display_element(calendar)


def test_registration_page(browser, base_url):
    browser.get(base_url + "?route=account/register")
    page_main_title = RegistertPage(browser).find_title()
    first_name = RegistertPage(browser).find_first_name()
    required_fields = RegistertPage(browser).find_req_fields()
    policy = RegistertPage(browser).find_policy()
    menu_sections = RegistertPage(browser).find_menu_sections()

    RegistertPage(browser).check_element_text(page_main_title, "Register Account")
    RegistertPage(browser).check_element_property(first_name, "placeholder", "First Name")
    RegistertPage(browser).check_is_not_selected(policy)
    RegistertPage(browser).check_len_elements(required_fields, 4)
    RegistertPage(browser).check_len_elements(menu_sections, 13)


def test_add_new_product(browser): ...


def test_remove_product(browser): ...


def test_register_new_user(browser): ...


def test_switch_currency(browser): ...
