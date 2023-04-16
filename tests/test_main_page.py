from locators.locators_main_page import MainPageLocators, CatalogPageLocators
from src.helper import BASE_URL, CATALOG_URL, CategoryData, SINGLE_CARD_URL


def t1est_check_main_page_elements(set_browser):
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


def test_check_single_card(set_browser):
    browser = set_browser
    browser.get(SINGLE_CARD_URL)
