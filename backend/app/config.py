from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "FinTrack API"
    ALLOWED_ORIGINS: str = "http://localhost:5137"
    
    # Database Configuration
    # Defaulting to a local SQLite file for Phase 2
    DATABASE_URL: str = "sqlite:///./fintrack.db"

    @property
    def origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"

settings = Settings()