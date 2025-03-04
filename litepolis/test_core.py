from fastapi.testclient import TestClient

from .core import get_test_app

app = get_test_app()
client = TestClient(app)

def test_read_main():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"detail": "OK"}


def test_read_main_not_found():
    response = client.get("/")
    assert response.status_code != 200
    assert response.json() == {"detail": "Not Found"}
