import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: list[int]
    DATABASE_URL: str
    RATE_LIMIT: int = 2

    class Config:
        env_file = ".env"

config = Settings()