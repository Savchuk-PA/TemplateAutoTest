import os

from dotenv import load_dotenv

load_dotenv()


class WebSettings:

    host = os.getenv("WEB_HOST")


class Settings:

    web: WebSettings = WebSettings()


settings = Settings()
