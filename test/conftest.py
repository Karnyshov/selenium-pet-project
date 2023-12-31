import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
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
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(executable_path="./chromedriver")
        driver = webdriver.Chrome(options=options, service=service)
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
