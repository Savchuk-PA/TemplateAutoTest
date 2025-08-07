import time

import allure

import web as web_pages
import test_data


class TestUsers:

    @allure.title("Test Users")
    def test_login(self, driver):
        auth = web_pages.AuthPage(driver=driver)
        auth.login(user=test_data.standard_user)
        # после логина логично проверить данные в профиле пользователя
        # на сайте такой возможности нет
        # проверим просто текст лого (текст лого в xpath)
        res_auth = auth.check_visibility_logo()
        assert res_auth is True, "Login failed. Logo is not visible."
