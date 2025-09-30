from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "todo_API"
    api_version: str = "1.0.0"
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/todo_db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
