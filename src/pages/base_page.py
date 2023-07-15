from src.core.singleton import Singleton
from src.core.cookies import Cookies
from src.core.localStorage import LocalStorage
from src.pages.locators import common_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage(Singleton):
    def __init__(self, driver):
        super().__init__(driver)

        self._cookie = Cookies(driver)
        self._localStorage = LocalStorage(driver)

        self._wait = WebDriverWait(driver, 5)

# TODO: Improve calling?
        self._common_locators = common_locators.GeneralLocators()

    def find_visible(self, locator):
        return self._wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def scroll_to_footer(self):
        body = self._driver.find_element(By.XPATH, self._common_locators.body)
        body.send_keys(Keys.END)

    def scroll_to_header(self):
        body = self._driver.find_element(By.XPATH, self._common_locators.body)
        body.send_keys(Keys.HOME)

    def scroll_to_element(self, locator):
        element = self._driver.find_element(By.XPATH, locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_title(self):
        return self._driver.title

    def get_current_url(self):
        return self._driver.current_url

    def open_main_page(self):
        self._wait.until(ec.visibility_of_element_located((By.XPATH, self._common_locators.logo_button))).click()
