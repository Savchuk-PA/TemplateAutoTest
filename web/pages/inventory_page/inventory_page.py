import allure

from .locators import InventoryPageLocators
from ..base_page.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._endpoint = "inventory.html"
        self.__locators = InventoryPageLocators
        self.open_self()

    @allure.step("Set sort products A to Z")
    def sort_products_a_to_z(self):
        """
        Selects the sorting option to sort products alphabetically from A to Z.

        Returns:
            None
        """
        self.logger.info("Sort products A to Z")
        self.base_select_list(select_list_value="az")

    @allure.step("Set sort products Z to A")
    def sort_products_z_to_a(self):
        """
        Selects the sorting option to sort products alphabetically from Z to A.

        Returns:
            None
        """
        self.logger.info("Sort products Z to A")
        self.base_select_list(select_list_value="za")

    @allure.step("Sort products price by desc")
    def sort_products_price_by_desc(self):
        """
        Selects the sorting option to sort products by price in descending order
        (from low to high).

        Returns:
            None
        """
        self.logger.info("Sort products price by desc")
        self.base_select_list(select_list_value="lohi")

    @allure.step("Sort products price by asc")
    def sort_products_price_by_asc(self):
        """
        Selects the sorting option to sort products by price in ascending order
        (from high to low).

        Returns:
            None
        """
        self.logger.info("Sort products price by asc")
        self.base_select_list(select_list_value="hilo")

    # или
    @allure.step("Sort products: {param}")
    def sort_products(self, param: str):
        """
        Sorts the products based on the provided sorting parameter.

        Args:
            param (str): The sorting method. Possible values:
                - "az": Sort products alphabetically from A to Z.
                - "za": Sort products alphabetically from Z to A.
                - "lohi": Sort products by price in descending order.
                - "hilo": Sort products by price in ascending order.

        Returns:
            None
        """
        self.logger.info(f"Sort products param: {param}")

        match param:
            case "az":
                self.logger.info("Sorting A to Z")
                self.base_select_list(select_list_value="az")
            case "za":
                self.logger.info("Sorting Z to A")
                self.base_select_list(select_list_value="za")
            case "lohi":
                self.logger.info("Sorting by price desc")
                self.base_select_list(select_list_value="lohi")
            case "hilo":
                self.logger.info("Sorting by price asc")
                self.base_select_list(select_list_value="hilo")
            case _:
                self.logger.error(f"Invalid sort parameter: {param}")
                raise ValueError(f"Unknown sort parameter: {param}")
