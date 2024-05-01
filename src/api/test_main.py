from fastapi.testclient import TestClient

import main

client = TestClient(main.app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_main_invalid_parameter():
    response = client.get("/")

def test_read_main_not_found():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
