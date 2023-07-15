import pytest
from selenium import webdriver
from src.pages.main_page import MainPage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://taxer.ua/")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def main_page(driver):
    main_page = MainPage(driver)
    yield main_page
