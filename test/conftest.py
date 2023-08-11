import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption("--browser_type",
                     help="Type of the browser. Can be Firefox or Chrome",
                     action='store',
                     default="Chrome")


@pytest.fixture(scope="session")
def browser(request):
    mode = request.config.getoption("--browser_type")

    if mode == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
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
