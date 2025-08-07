from selenium.webdriver.common.by import By


class BasePageLocators:

    # элемент в хедере
    logo = (
        By.XPATH,
        "//div[@data-test='header-container']//div[@class='app_logo' and text()='Swag Labs']",
    )
    error_message = (By.XPATH, "//h3[@data-test='error']")
    select_list = (By.XPATH, "//span[@class='select_container']")
    select_list_option_value = lambda value: (
        By.XPATH,
        f"//select//option[@value='{value}']",
    )
