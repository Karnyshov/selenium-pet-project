from src.core.singleton import Singleton
from src.core.cookies import Cookies
from src.core.localStorage import LocalStorage
from src.pages.locators import common_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO, filemode='w')


class BasePage(Singleton):

    def __init__(self, driver):
        super().__init__(driver)

        self._cookie = Cookies(driver)
        self._localStorage = LocalStorage(driver)

        self._wait = WebDriverWait(driver, 5)

# TODO: Improve calling?
        self._common_locators = common_locators.GeneralLocators()

    def find_visible(self, locator):
        logger.info(f"Trying to find visible element by XPath locator: {locator}")
        try:
            element = self._wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        except NoSuchElementException as err1:
            raise err1
        except TimeoutException as err2:
            raise err2
        else:
            return element

    def find_xpath(self, locator):
        logger.info(f"Trying to find element by XPath locator: {locator}")
        try:
            element = self._driver.find_element(By.XPATH, locator)
        except NoSuchElementException as err1:
            raise err1
        except TimeoutException as err2:
            raise err2
        else:
            return element

    def scroll_to_footer(self):
        logger.info("Scrolling to footer")
        body = self.find_xpath(self._common_locators.body)
        body.send_keys(Keys.END)

    def scroll_to_header(self):
        logger.info("Scrolling to header")
        body = self.find_xpath(self._common_locators.body)
        body.send_keys(Keys.HOME)

    def scroll_to_element(self, locator):
        logger.info(f"Scrolling to footer by using locator: {locator}")
        element = self.find_xpath(locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_title(self):
        return self._driver.title

    def get_current_url(self):
        return self._driver.current_url

    def open_main_page(self):
        logger.info("Opening main page")
        element = self.find_visible(self._common_locators.logo_button)
        element.click()
