# file /rudesktop_web/conftest.py

import pytest
from selene import browser
from selenium import webdriver
from pages.base_page import BasePage
from selene.api import be, have, s

def setup_browser(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-US")
    browser.config.timeout = 10
    browser.config.driver_options = options
    browser.open(base_url)

def browser_teardown():
    BasePage().get_screenshot()
    browser.close()
    browser.quit()

@pytest.fixture()
def close_cookie():
    try:
        s("//div[contains(@class,'l-accept-cookies')]//button[@data-ok]").should(be.visible).click()
    except:
        pass

@pytest.fixture(scope="function")
def setup(request):
    base_url = 'https://192.168.10.74'
    setup_browser(base_url)
    BasePage().open_unsafe()
    yield
    browser_teardown()