from fastapi.testclient import TestClient

from .core import app

client = TestClient(app)

def test_read_main():
    response = client.get("/api/v1/public/")
    assert response.status_code == 200
    assert response.json() == {"detail": "OK"}


def test_read_main_not_found():
    response = client.get("/")
    assert response.status_code != 200
    assert response.json() == {"detail": "Not Found"}
