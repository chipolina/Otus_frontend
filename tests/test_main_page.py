from page_objacts.catalogpage import CatalogPage
from page_objacts.productpage import ProductPage
from page_objacts.registerpage import RegistertPage
from src.helper import CategoryData
from page_objacts.mainpage import MainPage


def test_check_main_page_elements(browser, base_url):
    browser.get(base_url)

    currency = MainPage(browser).find_currency()
    search_btn = MainPage(browser).find_search_btn()
    cart_btn = MainPage(browser).find_cart_btn()
    product_cards = MainPage(browser).find_product_cards()
    top_navigation_items = MainPage(browser).find_top_navigation_items()

    assert currency.text == 'Currency'
    assert search_btn.is_enabled()
    assert cart_btn.is_enabled()
    assert len(product_cards) == 4
    assert len(top_navigation_items) == 8


def test_check_catalog_elements(browser, base_url):
    browser.get(base_url + "catalog/tablet")
    categories = CatalogPage(browser).find_categories()

    sort = CatalogPage(browser).find_sort()
    limit = CatalogPage(browser).find_limit()
    limits_select = CatalogPage(browser).find_limit_select()

    assert len(categories) == 8
    for category in categories:
        assert category.text.split(" (")[0] in [c.value for c in CategoryData]
    assert sort.is_enabled()
    assert limit.is_enabled()
    for limit in limits_select:
        assert int(limit.text) in [10, 25, 50, 75, 100]


def test_check_product_card(browser, base_url):
    browser.get(base_url + "product/laptop-notebook/hp-lp3065")

    product_price = ProductPage(browser).find_product_price()
    add_wl = ProductPage(browser).find_add_wl()
    add_to_cart = ProductPage(browser).find_add_to_cart()
    quantity = ProductPage(browser).find_quantity()
    delivery_date = ProductPage(browser).set_delivery_date()
    calendar = ProductPage(browser).find_calendar()

    assert product_price.is_displayed()
    assert add_wl.is_enabled()
    assert add_to_cart.is_enabled()
    assert quantity.get_property('value') == '1'
    assert delivery_date.get_property('value') == "2011-04-22"
    assert calendar.is_displayed()


def test_registration_page(browser, base_url):
    browser.get(base_url + "?route=account/register")
    page_main_title = RegistertPage(browser).find_title()
    first_name = RegistertPage(browser).find_first_name()
    required_fields = RegistertPage(browser).find_req_fields()
    policy = RegistertPage(browser).find_policy()
    menu_sections = RegistertPage(browser).find_menu_sections()

    assert page_main_title.text == "Register Account"
    assert first_name.get_property("placeholder") == "First Name"
    assert not policy.is_selected()
    assert len(required_fields) == 4
    assert len(menu_sections) == 13
