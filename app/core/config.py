from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import AnyUrl

class Settings(BaseSettings):
    DATABASE_URL: AnyUrl

    SYNC_DATABASE_URL: AnyUrl | None = None

    REDIS_URL: AnyUrl

    RABBITMQ_URL: AnyUrl

    APP_NAME: str = "Air_API"

    DEBUG: bool = False

    model_config = SettingsConfigDict(

        env_file = ".env",
        env_file_encoding = "utf-8",
        extra="ignore"
    )
settings = Settings()