from selenium.webdriver import Chrome


class Singleton:
    def __new__(cls, *args):
        if not hasattr(cls, "instance"):
            setattr(cls, "instance", super().__new__(cls))

        return getattr(cls, "instance")

    def __init__(self, driver: Chrome = None) -> None:
        self._driver = driver
