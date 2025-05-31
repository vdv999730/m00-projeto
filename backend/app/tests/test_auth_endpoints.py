import pytest
from app.core.security import get_password_hash
from app.models.user import User as UserModel
from app.core.database import get_db
from sqlalchemy.orm import Session

# 1. Testar POST /auth/token com usuário inválido
def test_login_invalid_user(client):
    invalid_payload = {"username": "naoexiste", "password": "1234"}
    response = client.post("/auth/token", data=invalid_payload)
    assert response.status_code == 401

# 2. Fixture para criar usuário de teste
@pytest.fixture(scope="function", autouse=True)
def create_test_user(client):
    # Usa a fixture 'client' para acessar dependency_overrides
    db: Session = next(client.app.dependency_overrides[get_db]())
    user = UserModel(username="usuarioteste", hashed_password=get_password_hash("teste123"))
    db.add(user)
    db.commit()
    yield
    db.query(UserModel).filter(UserModel.username == "usuarioteste").delete()
    db.commit()

# 3. Testar POST /auth/token com credenciais corretas
def test_login_valid_user(client):
    payload = {"username": "usuarioteste", "password": "teste123"}
    response = client.post("/auth/token", data=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

# 4. Testar rota protegida GET /auth/users/me com token válido
def test_protected_route(client):
    # Primeiro, obter token
    payload = {"username": "usuarioteste", "password": "teste123"}
    login_resp = client.post("/auth/token", data=payload)
    token = login_resp.json()["access_token"]

    # Acessar rota protegida
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/auth/users/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "usuarioteste"
