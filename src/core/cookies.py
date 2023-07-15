from src.core.singleton import Singleton


class Cookies(Singleton):
    def __init__(self, driver):
        super().__init__(driver)

    def get_all_cookies(self):
        return self._driver.get_cookies()

    def get_cookie(self, name):
        return self._driver.get_cookie(name)

# TODO: improve setter
    def add_cookie(self, name, value):
        self._driver.add_cookie({"name": f"{name}", "value": f"{value}"})

    def delete_cookie(self, name):
        self._driver.delete_cookie(name)

    def delete_all_cookies(self):
        self._driver.delete_all_cookies()
