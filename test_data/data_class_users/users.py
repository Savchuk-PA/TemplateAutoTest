from dataclasses import dataclass

from utils.data_generate_helper import DataGenerateHelper


@dataclass
class User(DataGenerateHelper):
    username: str
    password: str

    def build_random_user(self):
        self.username = self.faker.user_name()
        self.password = self.faker.password()


standard_user = User(username="standard_user", password="secret_sauce")
error_user = User(username="error_user", password="secret_sauce")
