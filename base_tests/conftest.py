import pytest
import web as web_pages
import test_data


@pytest.fixture(scope="function")
def login(driver):
    auth_p = web_pages.AuthPage(driver=driver)
    auth_p.login(user=test_data.standard_user)

    yield auth_p
