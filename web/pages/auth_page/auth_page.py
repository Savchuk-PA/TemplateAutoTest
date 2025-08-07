import allure

from ..base_page.base_page import BasePage
from .locators import LoginPageLocators


class AuthPage(BasePage):

    locators = LoginPageLocators

    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = ""
        self.open_self()

    @allure.step("Input username")
    def input_username(self, username):
        self.element_is_visible(locator=self.locators.input_username).send_keys(
            username
        )

    @allure.step("Input password")
    def input_password(self, password):
        self.element_is_visible(locator=self.locators.input_password).send_keys(
            password
        )

    @allure.step("Click login button")
    def click_login_button(self):
        self.element_is_visible(locator=self.locators.loing_button).click()

    @allure.step("Login to main page")
    def login(self, username, password) -> None:
        """
        Login to main page
        :param username: username
        :param password: password
        :return:
        """
        self.input_username(username=username)
        self.input_password(password=password)
        self.click_login_button()
