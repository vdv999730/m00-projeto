# Testes para endpoints básicos (raiz e /auth/*)
def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Backend Online 🚀"}


def test_auth_ping(client):
    response = client.get("/auth/ping")
    assert response.status_code == 200
    assert response.json() == {"pong": True}


def test_auth_health(client):
    response = client.get("/auth/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_auth_version(client):
    response = client.get("/auth/version")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "1.0.0"
    assert data["system"] == "m00-backend"
