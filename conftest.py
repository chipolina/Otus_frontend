import os.path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", choices=("chrome", "firefox", "safari"))
    parser.addoption("--headless", action='store_true')
    parser.addoption("--base_url", default="http://192.168.15.102:8081/en-gb/")
    parser.addoption("--drivers_folder", default="drivers")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    drivers_folder = request.config.getoption("--drivers_folder")
    driver = None
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.add_argument('--headless=new')
        service = ChromeService(executable_path=os.path.join(f"{drivers_folder}", "chromedriver"))
        driver = webdriver.Chrome(service=service, options=options)
    if browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless_mode:
            options.add_argument('--headless')
        service = FirefoxService(executable_path=os.path.join(f"{drivers_folder}", "geckodriver"))
        driver = webdriver.Firefox(service=service, options=options)
    if browser_name == 'safari':
        driver = webdriver.Safari()

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
