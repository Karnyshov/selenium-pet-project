from src.pages.base_page import BasePage
from src.pages.prices_pages import PricesPage
from src.pages.locators import main_page_locators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

# TODO: Improve calling?
        self._locators = main_page_locators.MainPageLocators()

        self._page_url = "https://taxer.ua/uk/"
        self._page_title = "Taxer.ua — Електронний кабінет підприємця"

    def open_prices_page(self):
        self.find_visible(self._common_locators.header_price_button).click()
        return PricesPage(self._driver)
