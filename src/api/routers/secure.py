import os
import uuid

from fastapi import APIRouter, Depends, Request

from auth import get_user
from db import API_Keys
from db import Users
from db import Conversations
from db import Comments

router = APIRouter()

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return {'detail': {
        'id': user[0],
        'email': user[1],
        'role': user[2]
    }}

# user CRUD
@router.get("/users/role")
async def get_userrole(user: tuple = Depends(get_user)):
    return {'detail': {
        'role': user[2]
    }}

@router.put("/users/renew")
async def update_usertoken(user: dict = Depends(get_user)):
    api_key_not_updated = True
    while api_key_not_updated:
        new_api_key = str(uuid.uuid4())
        api_keys = API_Keys(new_api_key, user[0])
        if api_keys.get_user_id_from_apikey() is None:
            api_keys.update()
            api_key_not_updated = False
    return {'detail': {
        'key': new_api_key
    }}

if os.environ['ui'] == 'streamlit':
    @router.get("/users/auth")
    async def get_userauth(user: dict = Depends(get_user)):
        # collect all user password pair for streamlit auth
        return {'detail': 'useryaml'}

@router.get("/users/profile")
async def get_userprofile(user: dict = Depends(get_user)):
    return user[1]

@router.post("/users/profile")
async def create_userprofile(request: Request,
                             user: dict = Depends(get_user)):
    request_body = await request.json()
    new_record = Users(**request_body)
    new_record.create()

@router.put("/users/profile")
async def update_userprofile(request: Request,
                             user: dict = Depends(get_user)):
    request_body = await request.json()
    new_record = Users(**request_body)
    new_record.update()

@router.delete("/users/profile")
async def delete_userprofile(user: dict = Depends(get_user)):
    raise NotImplementedError

# CURD of conversation
@router.get("/conversations/all")
async def get_all_conversations(user: dict = Depends(get_user)):
    return Conversations.get_all_conversation(user[0])

@router.get("/conversations/{cid}")
async def get_conversation(cid: int,
                           user: dict = Depends(get_user)):
    record = Conversations(cid=cid)
    return record.get_conversation_from_id()

@router.post("/conversations")
async def create_conversation(request: Request,
                              user: dict = Depends(get_user)):
    request_body = await request.json()
    new_record = Conversations(**request_body)
    new_record.create()

@router.put("/conversations")
async def update_conversation(request: Request,
                              user: dict = Depends(get_user)):
    request_body = await request.json()
    new_record = Conversations(**request_body)
    new_record.update()

@router.delete("/conversations/{cid}")
async def delete_conversation(cid: int,
                              user: dict = Depends(get_user)):
    record = Conversations(cid=cid)
    record.delete()

# CURD of comments
@router.get("/comments/random")
async def get_comment(user: dict = Depends(get_user)):
    return user

@router.get("/comments/moderate")
async def get_comments(user: dict = Depends(get_user)):
    return user

@router.post("/comments/")
async def create_comment(request: Request,
                         user: dict = Depends(get_user)):
    request_body = await request.json()
    new_record = Comments(**request_body)
    new_record.create()

@router.put("/comments/")
async def update_comment(request: Request,
                         user: dict = Depends(get_user)):
    request_body = await request.json()
    new_record = Comments(**request_body)
    new_record.update()

@router.delete("/comments/{cid}")
async def delete_comment(cid: int,
                         user: dict = Depends(get_user)):
    record = Comments(cid)
    record.delete()
