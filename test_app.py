from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home_returns_success():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["project"] == "Project 07"
    assert response.json()["status"] == "running"


def test_health_returns_healthy():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "timestamp" in response.json()


def test_unknown_route_returns_404():
    response = client.get("/does-not-exist")

    assert response.status_code == 404
