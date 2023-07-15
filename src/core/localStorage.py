from src.core.singleton import Singleton


class LocalStorage(Singleton):
    def __init__(self, driver):
        super().__init__(driver)

    def get_record(self, key):
        return self._driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def set_record(self, key, value):
        self._driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def delete_record(self, key):
        self._driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

    def clear_storage(self):
        self._driver.execute_script("window.localStorage.clear();")
