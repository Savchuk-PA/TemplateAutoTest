import allure

from test_data import User
from ..base_page.base_page import BasePage
from .locators import LoginPageLocators


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = LoginPageLocators
        self._endpoint = ""
        self.open_self()

    @allure.step("Input username")
    def input_username(self, username: str):
        self.logger.info(f"Input username {username}")
        self.element_is_visible(locator=self.__locators.input_username).send_keys(
            username
        )

    @allure.step("Input password")
    def input_password(self, password: str):
        self.element_is_visible(locator=self.__locators.input_password).send_keys(
            password
        )

    @allure.step("Click login button")
    def click_login_button(self):
        self.logger.info(f"Click login button")
        self.element_is_visible(locator=self.__locators.loing_button).click()

    @allure.step("Login to main page")
    def login(
        self,
        username: str | None = None,
        password: str | None = None,
        user: User | None = None,
    ) -> None:
        """
        Log in to the main page.

        Args:
            username (str): Username to log in.
            password (str): Password to log in.
            user (User): A User object with generated test data.
        Returns:
            None
        """
        if user:
            username = user.username
            password = user.password
        self.input_username(username=username)
        self.input_password(password=password)
        self.click_login_button()
