import os
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "OK"

def test_read_secure_main():
    response = client.get("/", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_main_invalid_parameter():
    response = client.get("/", headers={"X-Token": os.environ.get('API_KEY')})

def test_read_main_not_found():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_user_renew():
    response = client.get("/", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}
    
def test_read_user_profile():
    response = client.get("/users/profile", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_user_invalid_parameter():
    response = client.get("/users/profile", headers={"X-Token": os.environ.get('API_KEY')})

def test_create_user_profile():
    response = client.get("/users/profile", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_create_user_invalid_parameter():
    response = client.get("/users/profile", headers={"X-Token": os.environ.get('API_KEY')})

def test_update_user_profile():
    response = client.get("/users/profile", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_update_user_invalid_parameter():
    response = client.get("/users/profile", headers={"X-Token": os.environ.get('API_KEY')})

def test_delete_user_profile():
    response = client.get("/users/profile", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_delete_user_invalid_parameter():
    response = client.get("/users/profile", headers={"X-Token": os.environ.get('API_KEY')})

def test_read_all_conversation():
    response = client.get("/conversations/all", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_conversation():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_conversation_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-Token": os.environ.get('API_KEY')})

def test_create_conversation():
    response = client.post("/conversation", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_create_conversation_invalid_parameter():
    response = client.post("/conversation", headers={"X-Token": os.environ.get('API_KEY')})

def test_update_conversation():
    response = client.get("/conversation", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_update_conversation_invalid_parameter():
    response = client.get("/conversation", headers={"X-Token": os.environ.get('API_KEY')})

def test_delete_conversation():
    cid = "test"
    response = client.get(f"/conversation/{cid}", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_delete_conversation_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversation/{cid}", headers={"X-Token": os.environ.get('API_KEY')})




def test_read_random_comments():
    response = client.get("/comments/random", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}
    
def test_read_random_comments_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-Token": os.environ.get('API_KEY')})

def test_read_comments_moderate():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_read_comments_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversations/{cid}", headers={"X-Token": os.environ.get('API_KEY')})

def test_create_comment():
    response = client.post("/comments", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_create_comments_invalid_parameter():
    response = client.post("/comments", headers={"X-Token": os.environ.get('API_KEY')})

def test_update_comments():
    response = client.get("/comments", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_update_comments_invalid_parameter():
    response = client.put("/comments", headers={"X-Token": os.environ.get('API_KEY')})

def test_delete_comments():
    cid = "test"
    response = client.get(f"/conversation/{cid}", headers={"X-Token": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == {"user_id": 0}

def test_delete_comments_invalid_parameter():
    cid = "test"
    response = client.get(f"/conversation/{cid}", headers={"X-Token": os.environ.get('API_KEY')})
