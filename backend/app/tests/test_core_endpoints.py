import pytest


# Testes para endpoints básicos (raiz e /auth/*)
@pytest.mark.asyncio
async def test_read_root(async_client):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Backend Online 🚀"}


@pytest.mark.asyncio
async def test_auth_ping(async_client):
    response = await async_client.get("/auth/ping")
    assert response.status_code == 200
    assert response.json() == {"pong": True}


@pytest.mark.asyncio
async def test_auth_health(async_client):
    response = await async_client.get("/auth/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_auth_version(async_client):
    response = await async_client.get("/auth/version")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "1.0.0"
    assert data["system"] == "m00-backend"
