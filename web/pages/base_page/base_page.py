import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from settings import settings
from web.pages.base_page.base_locators import BasePageLocators
from ..info_messages import info_erorros_messages
from ..info_messages.info_erorros_messages import messages


class BasePage:
    def __init__(self, driver):
        self.__base_locators = BasePageLocators
        self.host = settings.web.host
        self.info_messages = messages
        self.driver = driver
        self.logger = settings.logger
        self.logger.info(f"Base page host: {self.host}")

    @allure.step("Open url a browser")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Open url in to object page")
    def open_self(self):
        self.driver.get(f"{self.host}{self._endpoint}")

    @allure.step("Find a visible element")
    def element_is_visible(self, locator, timeout=20):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Find visible elements")
    def elements_are_visible(self, locator, timeout=20):
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Find a present element")
    def element_is_present(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Find present elements")
    def elements_are_present(self, locator, timeout=20):
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Find a not visible element")
    def element_is_not_visible(self, locator, timeout=20):
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Find clickable elements")
    def element_is_clickable(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Go to specified element")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Check visibility logo")
    def check_visibility_logo(self):
        self.logger.info(f"Check visibility logo...")
        res = self.element_is_visible(locator=self.__base_locators.logo).is_displayed()
        self.logger.info(f"Visibility logo: {res}")
        return res
