from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str

    def build_random_user(self):
        self.username = self.username.upper()
        self.password = self.password.upper()
