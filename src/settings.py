"""Application configurations settings"""

from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# _ = load_dotenv(".env.local")  # Load environment variables from .env file


class AppSettings(BaseSettings):
    """
    Represents the application settings.

    Attributes:
        APP_ENV (str): The application environment.       
        RABBIT_URI (str): The RabbitMQ URI.
        RABBIT_QUEUE_NAME (str): The RabbitMQ queue name.

    """

    APP_ENV: str = "None"
    RABBITMQ_URI: str = "None"
    RABBITMQ_QUEUE_NAME: str = "None"

    model_config = ConfigDict(
        env_file=".env.dev",
        env_file_encoding="utf-8"
    )


app_settings: AppSettings = AppSettings()
