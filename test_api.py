import pytest
from app_core import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Midterm API is running!" in response.data

def test_health_check(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_tasks_returns_list(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert len(response.json) == 2