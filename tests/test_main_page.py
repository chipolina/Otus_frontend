from locators.locators_main_page import MainPageLocators, CatalogPageLocators
from src.helper import BASE_URL, CATALOG_URL


def test_check_main_page_elements(set_browser):
    browser = set_browser
    browser.get(BASE_URL)

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


def test_check_catalog_elements(set_browser):
    browser = set_browser
    browser.get(CATALOG_URL)

    cat = browser.find_elements(*CatalogPageLocators.CATEGORIES)

    assert len(cat) == 8
