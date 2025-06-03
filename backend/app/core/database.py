import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

# 🛠️ Corrigir para driver asyncpg
DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Criar engine assíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Criar sessionmaker para AsyncSession
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
)

# Base
Base = declarative_base()


# Dependência para injetar a sessão no FastAPI
async def get_db():
    async with SessionLocal() as session:
        yield session
