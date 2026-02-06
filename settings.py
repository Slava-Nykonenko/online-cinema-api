from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Online Cinema API"
    DATABASE_URL: str = Field(description="Database URL")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


settings = Settings()
