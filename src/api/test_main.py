import os
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)

def test_read_main():
    response = client.get("/api/v1/public/")
    assert response.status_code == 200
    assert response.text == "OK"

def test_read_secure_main():
    response = client.get("/api/v1/secure/", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert data["user_id"] == 0

def test_read_main_invalid_parameter():
    response = client.get("/api/v1/secure/")
    assert response.status_code == 403
    invalid_token = os.environ.get('API_KEY') + "0"
    response = client.get("/api/v1/secure/", headers={"X-API-Key": invalid_token})
    assert response.status_code == 403

def test_read_main_not_found():
    response = client.get("/")
    assert response.status_code != 200
    assert response.json() == {"detail": "Not Found"}

def test_read_user_role():
    response = client.get("/api/v1/secure/users/role", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_role": "root"}

def test_read_user_renew():
    # TODO
    response = client.get("/api/v1/secure/users/renew", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}
    
def test_read_user_profile():
    response = client.get("/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_user_invalid_parameter():
    response = client.get("/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_create_user_profile():
    response = client.get("/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_create_user_invalid_parameter():
    response = client.get("/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_update_user_profile():
    response = client.get("/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_update_user_invalid_parameter():
    response = client.get("/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_delete_user_profile():
    response = client.get("/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_delete_user_invalid_parameter():
    response = client.get("/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_read_all_conversation():
    response = client.get("/conversations/all", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_conversation():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_conversation_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_create_conversation():
    response = client.post("/conversation", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_create_conversation_invalid_parameter():
    response = client.post("/conversation", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_update_conversation():
    response = client.get("/conversation", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_update_conversation_invalid_parameter():
    response = client.get("/conversation", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_delete_conversation():
    cid = "test"
    response = client.get(f"/conversation/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_delete_conversation_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversation/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})




def test_read_random_comments():
    response = client.get("/comments/random", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}
    
def test_read_random_comments_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_read_comments_moderate():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_comments_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_create_comment():
    response = client.post("/comments", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_create_comments_invalid_parameter():
    response = client.post("/comments", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_update_comments():
    response = client.get("/comments", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_update_comments_invalid_parameter():
    response = client.put("/comments", headers={"X-API-Key": os.environ.get('API_KEY')})

def test_delete_comments():
    cid = "test"
    response = client.get(f"/conversation/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_delete_comments_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversation/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})
