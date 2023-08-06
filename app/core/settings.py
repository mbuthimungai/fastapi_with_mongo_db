from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    MONGO_URL: str = os.getenv("ME_MONGODB_URL")
    API_TITLE: str = os.getenv("TITLE")
    
settings = Settings()