import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
from datetime import datetime


@pytest.fixture(scope="session")
def chrome_options():
    options = Options()

    # Базовые настройки
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Расширенные настройки для отключения уведомлений о паролях
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "password_leak_detection": False,
            "profile.password_manager_leak_detection": False,
        },
    )

    # Дополнительные аргументы
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--ignore-certificate-errors")

    return options


@pytest.fixture(scope="function")
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(
        attach,
        name=f"Screenshot {datetime.today()}",
        attachment_type=allure.attachment_type.PNG,
    )
    driver.quit()
