import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")  # dev, test, prod
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    @property
    def async_database_url(self):
        """
        Ajusta a DATABASE_URL para usar driver assíncrono quando necessário.
        """
        if self.DATABASE_URL.startswith("postgresql://"):
            return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
        return self.DATABASE_URL  # Ex.: sqlite+aiosqlite:///:memory:


settings = Settings()
