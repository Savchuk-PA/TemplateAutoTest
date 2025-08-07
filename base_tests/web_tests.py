import time


import web as web_pages
import test_data


class TestUsers:

    def test_login(self, driver):
        auth = web_pages.AuthPage(driver=driver)

        auth.login(user=test_data.standard_user)
        time.sleep(2)
