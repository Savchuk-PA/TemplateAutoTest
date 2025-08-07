import os

from dotenv import load_dotenv
from loguru import logger

logger.add(
    "logs/info.log",
    rotation="5 MB",
    retention="3 days",
    compression="zip",
    level="INFO",
    format="{time} - {name} - {message}",
    enqueue=True,
)

load_dotenv()


class WebSettings:

    host = os.getenv("WEB_HOST")


class Settings:
    logger = logger
    web: WebSettings = WebSettings()


settings = Settings()
