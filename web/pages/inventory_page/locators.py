from selenium.webdriver.common.by import By


class InventoryPageLocators:
    select = (By.XPATH, "//select[@data-test='product-sort-container']")
    select_option_by_text = lambda text_option: (
        By.XPATH,
        f"//select//option[text()='{text_option}']",
    )
