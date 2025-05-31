import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.core.database import Base, get_db
from app.main import app

# 1. URL para banco de teste (SQLite local)
TEST_DATABASE_URL = "sqlite:///./test_db.sqlite3"

# 2. Criar engine e SessionLocal para o teste
engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# 3. Override da dependência get_db para utilizar o banco de teste
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# 4. Aplica o override no app
app.dependency_overrides[get_db] = override_get_db

# 5. Fixture para criar e destruir o banco de teste antes/depois de cada sessão
@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    # Remove arquivo antigo, se existir
    if os.path.exists("./test_db.sqlite3"):
        os.remove("./test_db.sqlite3")

    # Criar todas as tabelas no engine de teste
    Base.metadata.create_all(bind=engine)
    yield
    # Ao final, destrói as tabelas e remove o arquivo
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("./test_db.sqlite3"):
        os.remove("./test_db.sqlite3")

# 6. Fixture para instanciar o TestClient do FastAPI
@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c
