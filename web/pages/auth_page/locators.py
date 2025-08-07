from selenium.webdriver.common.by import By


class LoginPageLocators:
    input_username = (By.XPATH, "//input[@data-test='username']")
    input_password = (By.XPATH, "//input[@data-test='password']")
    loing_button = (By.XPATH, "//input[@data-test='login-button']")
