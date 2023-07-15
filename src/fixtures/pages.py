import pytest
from selenium import webdriver
from src.pages.main_page import MainPage


@pytest.fixture(scope="session")
def browser(request):
    mode = request.config.getoption("--browser_type")

    if mode == "Chrome":
        driver = webdriver.Chrome()
        yield driver
        driver.quit()
    elif mode == "Firefox":
        driver = webdriver.Firefox()
        yield driver
        driver.quit()
    else:
        raise AssertionError("Incorrect browser name. Can be Chrome of Firefox")


@pytest.fixture(scope="session")
def main_page(browser):
    main_page = MainPage(browser)
    browser.get("https://taxer.ua/")
    yield main_page
