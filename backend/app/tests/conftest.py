import os
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient
from fastapi import FastAPI
from app.core.database import Base, get_db
from app.main import app as main_app

DATABASE_URL_TEST = "sqlite+aiosqlite:///./test_db.sqlite3"

# 1. Async Engine para testes
engine_test = create_async_engine(
    DATABASE_URL_TEST, connect_args={"check_same_thread": False}
)
AsyncSessionLocal = sessionmaker(
    bind=engine_test, class_=AsyncSession, expire_on_commit=False
)


# 2. Override get_db para usar AsyncSession
async def override_get_db():
    async with AsyncSessionLocal() as session:
        yield session


# 3. Fixture para o app com dependências sobreescritas
@pytest.fixture(scope="session")
def app() -> FastAPI:
    main_app.dependency_overrides[get_db] = override_get_db
    return main_app


# 4. Fixture para criar e destruir o banco de teste
@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    # Remove arquivo antigo se existir
    if os.path.exists("./test_db.sqlite3"):
        os.remove("./test_db.sqlite3")

    # Cria tabelas
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Apaga tabelas
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    if os.path.exists("./test_db.sqlite3"):
        os.remove("./test_db.sqlite3")


# 5. AsyncClient Fixture para testes
@pytest.fixture
async def async_client(app: FastAPI):
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
