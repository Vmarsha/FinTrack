from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "FinTrack API"
    
    # We store origins as a comma-separated string in .env 
    # but convert it to a list for FastAPI to use.
    ALLOWED_ORIGINS: str = "http://localhost:5173"

    @property
    def origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"

# Create a singleton instance to be used across the app
settings = Settings()