from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=("chrome", "firefox"))
    parser.addoption("--headless", action='store_true')


@pytest.fixture
def set_browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    browser = None
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.add_argument('--headless=new')
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    if browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = headless_mode
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    browser.maximize_window()
    yield browser
    browser.quit()
