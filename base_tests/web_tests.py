import time

import allure
import pytest
import web as web_pages
import test_data


class TestAuthorization:

    @allure.title("Test Authorization: correct data")
    @pytest.mark.smoke
    def test_login(self, driver):
        auth = web_pages.AuthPage(driver=driver)
        auth.login(user=test_data.standard_user)
        res_auth = auth.check_visibility_logo()
        assert res_auth is True, "Login failed. Logo is not visible."

    @allure.title("Test Authorization: blocked user")
    def test_wrong_login(self, driver):
        auth = web_pages.AuthPage(driver=driver)
        auth.login(user=test_data.locked_out_user)
        text_error_message = auth.get_error_message()
        assert text_error_message == auth.info_messages.auth_page.error_user_blocked
