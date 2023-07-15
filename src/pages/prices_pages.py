from src.pages.base_page import BasePage


class PricesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self._page_url = "https://taxer.ua/uk/prices"
        self._page_title = "Taxer.ua — Електронний кабінет підприємця"
