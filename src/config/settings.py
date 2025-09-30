from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "todo_API"
    api_version: str = "1.0.0"


settings = Settings()
