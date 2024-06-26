import os
import json
from fastapi.testclient import TestClient

import main
from auth import is_valid_uuid

client = TestClient(main.app)

def test_read_main():
    response = client.get("/api/v1/public/")
    assert response.status_code == 200
    assert response.json() == {"detail": "OK"}

def test_read_secure_main():
    response = client.get("/api/v1/secure/", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    data = response.json()['detail']
    assert "id" in data
    assert data["id"] == 0

def test_read_main_invalid_parameter():
    response = client.get("/api/v1/secure/")
    assert response.status_code == 403
    invalid_token = os.environ.get('API_KEY') + "0"
    response = client.get("/api/v1/secure/", headers={"X-API-Key": invalid_token})
    assert response.status_code == 401

def test_read_main_not_found():
    response = client.get("/")
    assert response.status_code != 200
    assert response.json() == {"detail": "Not Found"}

def test_read_user_role():
    response = client.get("/api/v1/secure/users/role", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json()['detail'] == "root"

def test_read_user_renew():
    response = client.put("/api/v1/secure/users/renew", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert is_valid_uuid(response.json()['detail'])
    
def test_read_user_profile():
    test_read_secure_main()

def test_read_user_invalid_parameter():
    test_read_main_invalid_parameter()

def test_create_user_profile():
    import hashlib
    response = client.post("/api/v1/secure/users/profile",
                           headers={"X-API-Key": os.environ.get('API_KEY')},
                           json={
                               "email": "test@user.com",
                               "password": hashlib.md5(b"mysecretpassword").hexdigest()
                           })
    assert response.status_code == 200
    assert is_valid_uuid(response.json()["detail"])
    os.environ['API_KEY'] = response.json()["detail"]

def test_create_user_invalid_parameter():
    response = client.post("/api/v1/secure/users/profile",
                           headers={"X-API-Key": os.environ.get('API_KEY')},
                           json={
                               "email": "test@user.com"
                           })
    assert response.status_code != 200
    assert isinstance(response.json()['detail'], str)

def test_update_user_profile():
    import hashlib
    response = client.put("/api/v1/secure/users/profile",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              "email": "newmail@user.com",
                              "password": hashlib.md5(b"newpassword").hexdigest()
                          })
    assert response.status_code == 200

def test_update_user_invalid_parameter():
    import hashlib
    response = client.put("/api/v1/secure/users/profile",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              "email": "newmail.user.com",
                              "password": hashlib.md5(b"newpassword").hexdigest()
                          })
    assert response.status_code != 200
    response = client.put("/api/v1/secure/users/profile",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              "email": "newmail@user.com",
                              "password": ""
                          })
    assert response.status_code == 400
    response = client.put("/api/v1/secure/users/profile",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              "email": "newmail@user.com",
                              "password": hashlib.md5(b"newpassword").hexdigest(),
                              "id": 1
                          })
    assert response.status_code != 200
    response = client.put("/api/v1/secure/users/profile",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              "email": "newmail@user.com",
                              "password": hashlib.md5(b"newpassword").hexdigest(),
                              "role": "root"
                          })
    assert response.status_code != 200

def test_delete_user_profile():
    response = client.delete("/api/v1/secure/users/profile", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 403

def test_delete_user_invalid_parameter():
    pass # as delete is not implemented right now

def test_read_conversation():
    # create conversation
    response = client.post("/api/v1/secure/conversations",
                           headers={"X-API-Key": os.environ.get('API_KEY')},
                           json={
                               "title": "A topic",
                               "description": "Users will come in this conversation and leave comments"
                           })
    assert response.status_code == 200
    response = client.get("/api/v1/secure/conversations/all", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    for conversation in response.json()['detail']:
        assert conversation['creator_id'] == 0
    cid = conversation['id']
    response = client.get(f"/api/v1/secure/conversations/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    assert response.json() == json.dumps(conversation)

def test_read_conversation_invalid_parameter():
    cid = "test"
    response = client.get(f"/api/v1/secure/conversations/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code != 200

def test_create_conversation_invalid_parameter():
    response = client.post("/api/v1/secure/conversations", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code != 200

def test_update_conversation():
    response = client.put("/api/v1/secure/conversations",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              "id": 1,
                              "title": "A new topic",
                              "description": "Users will come in this conversation and leave comments",
                              "moderate": True
                          })
    assert response.status_code == 200

def test_update_conversation_invalid_parameter():
    response = client.put("/api/v1/secure/conversations", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code != 200
    response = client.put("/api/v1/secure/conversations",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              "title_desc": "A new topic"
                          })
    assert response.status_code != 200

def test_delete_conversation():
    cid = 1
    response = client.delete(f"/api/v1/secure/conversations/{cid}", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 403

def test_delete_conversation_invalid_parameter():
    pass # as delete is not implemented right now

def test_read_comments_moderate():
    # create comment
    response = client.post("/api/v1/secure/comments",
                           headers={"X-API-Key": os.environ.get('API_KEY')},
                           json={
                               "comment": "test comment",
                               "conversation_id": 1
                           })
    assert response.status_code == 200
    cid = 1
    response = client.get(f"/api/v1/secure/comments/{cid}/moderate",
                          headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    for comment in response.json()['detail']:
        assert 'comment' in  comment
        assert 'user_id' in  comment
        assert 'comment_id' in  comment
        assert 'conversation_id' in  comment
    response = client.put(f"/api/v1/secure/comments",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              'update': 'APPROVE',
                              'comment_id': comment['comment_id']
                          })
    assert response.status_code == 200
    response = client.get(f"/api/v1/secure/comments/{cid}/random", headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 200
    for comment in response.json()['detail']:
        assert 'comment' in  comment
        assert 'user_id' in  comment
        assert 'comment_id' in  comment
        assert 'conversation_id' in  comment

def test_read_comments_invalid_parameter():
    cid = "test"
    response = client.get(f"/api/v1/secure/comments/{cid}",
                            headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code != 200

def test_create_comments_invalid_parameter():
    response = client.post("/api/v1/secure/comments",
                           headers={"X-API-Key": os.environ.get('API_KEY')},
                           json={
                               "comment": "test comment"
                           })
    assert response.status_code != 200
    response = client.post("/api/v1/secure/comments",
                           headers={"X-API-Key": os.environ.get('API_KEY')},
                           json={
                               "conversation_id": 1
                           })
    assert response.status_code != 200

def test_update_comments():
    response = client.put(f"/api/v1/secure/comments",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              'comment_id': 1,
                              'comment': "comment text"
                          })
    assert response.status_code == 200

def test_update_comments_invalid_parameter():
    response = client.put(f"/api/v1/secure/comments",
                          headers={"X-API-Key": os.environ.get('API_KEY')},
                          json={
                              'comment': "comment"
                          })
    assert response.status_code != 200

def test_delete_comments():
    cid = 1
    response = client.delete(f"/api/v1/secure/comments/{cid}",
                                headers={"X-API-Key": os.environ.get('API_KEY')})
    assert response.status_code == 403

def test_delete_comments_invalid_parameter():
    pass # as delete is not implemented right now
