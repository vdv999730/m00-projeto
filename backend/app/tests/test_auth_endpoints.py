import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from app.core.security import get_password_hash
from app.models.user import User as UserModel
from sqlalchemy.ext.asyncio import AsyncSession


# 1. Fixture do AsyncClient
@pytest.fixture
async def async_client(app: FastAPI):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client


# 2. Testar POST /auth/token com usuário inválido
@pytest.mark.asyncio
async def test_login_invalid_user(async_client):
    invalid_payload = {"username": "naoexiste", "password": "1234"}
    response = await async_client.post("/auth/token", data=invalid_payload)
    assert response.status_code == 401


# 3. Fixture para criar usuário de teste
@pytest.fixture(scope="function", autouse=True)
async def create_test_user(app):
    # Acessa o banco assíncrono
    async with app.state._db() as session:
        db: AsyncSession = session
        user = UserModel(
            username="usuarioteste", hashed_password=get_password_hash("teste123")
        )
        db.add(user)
        await db.commit()

        yield

        await db.delete(user)
        await db.commit()


# 4. Testar POST /auth/token com credenciais corretas
@pytest.mark.asyncio
async def test_login_valid_user(async_client):
    payload = {"username": "usuarioteste", "password": "teste123"}
    response = await async_client.post("/auth/token", data=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


# 5. Testar rota protegida GET /auth/users/me com token válido
@pytest.mark.asyncio
async def test_protected_route(async_client):
    # Primeiro, obter token
    payload = {"username": "usuarioteste", "password": "teste123"}
    login_resp = await async_client.post("/auth/token", data=payload)
    token = login_resp.json()["access_token"]

    # Acessar rota protegida
    headers = {"Authorization": f"Bearer {token}"}
    response = await async_client.get("/auth/users/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "usuarioteste"
