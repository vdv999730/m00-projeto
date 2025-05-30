from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Backend Online 🚀"}

def test_ping():
    response = client.get("/auth/ping")
    assert response.status_code == 200
    assert response.json() == {"pong": True}

def test_health():
    response = client.get("/auth/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_version():
    response = client.get("/auth/version")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "1.0.0"
    assert data["system"] == "m00-backend"
