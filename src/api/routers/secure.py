import os
import re
import uuid
import hashlib

from fastapi import APIRouter, Depends, Request
from fastapi import HTTPException

from auth import get_user
from db import API_Keys
from db import Users
from db import Conversations
from db import Comments

tags_metadata = [
    {
        "name": "User",
        "description": "Operations related to the currently authenticated user",
    },
    {
        "name": "API Keys",
        "description": "Operations related to API keys",
    },
    {
        "name": "Conversations",
        "description": "Operations related to conversations",
    },
    {
        "name": "Comments",
        "description": "Operations related to comments",
    }
]

# from pydantic import BaseModel
# @app.post("/items/", response_model=ResponseMessage)
# https://fastapi.tiangolo.com/advanced/generate-clients/

router = APIRouter()

@router.get("/", tags=["User"])
async def get_testroute(user: dict = Depends(get_user)):
    """This endpoint returns information about the currently authenticated user.

    Parameters
    ----------
    user : dict
        A dictionary containing user information retrieved
        from the `get_user` dependency from `auth` module.
        The dictionary is expected to have the following structure:
        ```
        {
            'id': <user_id>,
            'email': <user_email>,
            'role': <user_role>
        }
        ```

    Returns
    -------
    dict
        A dictionary containing the user's id, email, and role.
    """
    return {
        'detail': {
            'id': user['id'],
            'email': user['email'],
            'role': user['role']
        }
    }

# user CRUD
@router.get("/users/role", tags=["User"])
async def get_userrole(user: tuple = Depends(get_user)):
    """
    This endpoint returns the role of the currently authenticated user.

    Parameters
    ----------
    user : dict
        A dictionary containing user information retrieved
        from the `get_user` dependency from `auth` module.
        The dictionary is expected to have the following structure:
        ```
        {
            'id': <user_id>,
            'email': <user_email>,
            'role': <user_role>
        }

    Returns
    -------
    dict
        A dictionary containing the user's role.
    """
    return {
        'detail': {
            'role': user['role']
        }
    }

@router.put("/users/renew", tags=["User", "API Keys"])
async def update_usertoken(user: dict = Depends(get_user)):
    """Updates the API key for the currently authenticated user.

    Parameters
    ----------
    user : dict
        A dictionary containing user information retrieved
        from the `get_user` dependency from `auth` module.
        The dictionary is expected
        to have the following structure:
        ```
        {
            'id': <user_id>,
            'email': <user_email>,
            'role': <user_role>
        }
        ```

    Returns
    -------
    dict
        A dictionary containing the new API key.
    """
    api_key_not_updated = True
    while api_key_not_updated:
        new_api_key = str(uuid.uuid4())
        api_keys = API_Keys(new_api_key, user[0])
        if api_keys.get_user_id_from_apikey() is None:
            api_keys.update()
            api_key_not_updated = False
    return {
        'detail': {
            'key': new_api_key
        }
    }

if os.environ['ui'] == 'streamlit':
    @router.get("/users/auth") # hidden for streamlit before beta version
    async def get_userauth(user: dict = Depends(get_user)):
        # collect all user password pair for streamlit auth
        return {'detail': 'useryaml'}

@router.get("/users/profile", tags=["User"])
async def get_userprofile(user: dict = Depends(get_user)):
    """This endpoint returns information about the currently authenticated user.

    Parameters
    ----------
    user : dict
        A dictionary containing user information retrieved
        from the `get_user` dependency from `auth` module.
        The dictionary is expected
        to have the following structure:
        ```
        {
            'id': <user_id>,
            'email': <user_email>,
            'role': <user_role>
        }
        ```

    Returns
    -------
    dict
        A dictionary containing the user's id, email, and role.
    """
    return {
        'detail': {
            'id': user['id'],
            'email': user['email'],
            'role': user['role']
        }
    }

@router.post("/users/profile", tags=["User"])
async def create_userprofile(request: Request,
                             user: dict = Depends(get_user)):
    request_body = await request.json()
    # sanitization
    data = dict()
    if 'email' in request_body:
        # validate email format in UI
        if re.match(r"'[^@]+@[^@]+\.[^@]+'",
                    request_body['email']):
            data['email'] = request_body['email']
        else:
            raise HTTPException(status_code=400,
                                detail="Invalid parameter")
        # allow config for sending validation email
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    if 'password' in request_body:
        data['password'] = hashlib.sha1(
            request_body['password'].encode()).hexdigest()
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    new_record = Users(**data)
    new_record.create()

@router.put("/users/profile", tags=["User"])
async def update_userprofile(request: Request,
                             user: dict = Depends(get_user)):
    if user['role'] != 'user' or user['role'] != 'root':
        raise HTTPException(status_code=401, detail="Unauthorized")
    request_body = await request.json()
    data = dict()
    data['id'] = user['id']
    if 'email' in request_body:
        data['email'] = request_body['email']
    if 'password' in request_body:
        data['password'] = hashlib.sha1(
            request_body['password'].encode()).hexdigest()
    new_record = Users(**data)
    new_record.update()

@router.delete("/users/profile", tags=["User"])
async def delete_userprofile(user: dict = Depends(get_user)):
    raise HTTPException(status_code=403, detail="Method Not Allowed")
    # raise HTTPException(status_code=501, detail="Not Implemented")

# CURD of conversation
@router.get("/conversations/all", tags=["Conversations"])
async def get_all_conversations(user: dict = Depends(get_user)):
    return {
        'detail': Conversations.get_all_conversation(user['id'])
    }

@router.get("/conversations/{cid}", tags=["Conversations"])
async def get_conversation(cid: int,
                           user: dict = Depends(get_user)):
    record = Conversations(cid=cid)
    return record.get_conversation_from_id()

@router.post("/conversations", tags=["Conversations"])
async def create_conversation(request: Request,
                              user: dict = Depends(get_user)):
    if user['role'] != 'user':
        raise HTTPException(status_code=401, detail="Unauthorized")
    request_body = await request.json()
    data = {'creator_id': user[0]}
    if 'title' in request_body:
        data['title'] = request_body['title']
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    if 'description' in request_body:
        data['desc'] = request_body['description']
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    new_record = Conversations(**data)
    new_record.create()

@router.put("/conversations", tags=["Conversations"])
async def update_conversation(request: Request,
                              user: dict = Depends(get_user)):
    request_body = await request.json()
    data = {'creator_id': user[0]}
    if 'title' in request_body:
        data['title'] = request_body['title']
    if 'description' in request_body:
        data['desc'] = request_body['description']
    new_record = Conversations(**data)
    new_record.update()

@router.delete("/conversations/{cid}", tags=["Conversations"])
async def delete_conversation(cid: int,
                              user: dict = Depends(get_user)):
    raise HTTPException(status_code=403, detail="Method Not Allowed")
    # raise HTTPException(status_code=501, detail="Not Implemented")
    # record = Conversations(cid=cid)
    # record.delete()

# CURD of comments
@router.get("/comments/{cid}/", tags=["Comments"])
async def get_comment(cid: int,
                      random: bool = False,
                      moderated: bool = False,
                      user: dict = Depends(get_user)):
    comment = Comments(conversation_id=cid,
                       random=random,
                       moderated=moderated)
    return {'detail': comment.get_comments_from_conversation()}

@router.get("/comments/{cid}/moderate", tags=["Comments"])
async def get_comments(cid: int, user: dict = Depends(get_user)):
    # waiting to be moderated comments if conversation moderation enabled
    record = Conversations(cid=cid)
    data = record.get_conversation_from_id()
    if data['moderation'] is True:
        comment = Comments(conversation_id=cid)
        return {'detail': comment.get_comments_waiting_for_moderate()}

@router.post("/comments/", tags=["Comments"])
async def create_comment(request: Request,
                         user: dict = Depends(get_user)):
    if user['role'] != 'user':
        raise HTTPException(status_code=401, detail="Unauthorized")
    request_body = await request.json()
    data = dict()
    if 'comment' in request_body:
        data['comment'] = request_body['comment']
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    if 'user_id' in request_body:
        data['user_id'] = request_body['user_id']
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    if 'conversation_id' in request_body:
        data['conversation_id'] = request_body['conversation_id']
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    new_record = Comments(**data)
    new_record.create()

@router.put("/comments/", tags=["Comments"])
async def update_comment(request: Request,
                         user: dict = Depends(get_user)):
    if user['role'] != 'user':
        raise HTTPException(status_code=401, detail="Unauthorized")
    request_body = await request.json()
    data = dict()
    if 'comment_id' in request_body:
        data['comment_id'] = request_body['comment_id']
    else:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    if 'comment' in request_body:
        data['comment'] = request_body['comment']
    if 'vote' in request_body:
        data['vote'] = request_body['vote']
    record = Comments(**data)
    if request_body['task'] == 'approve':
        record.approve()
    elif request_body['task'] == 'reject':
        record.reject()
    else:
        record.update()

@router.delete("/comments/{cid}", tags=["Comments"])
async def delete_comment(cid: int,
                         user: dict = Depends(get_user)):
    raise HTTPException(status_code=403, detail="Method Not Allowed")
    # raise HTTPException(status_code=501, detail="Not Implemented")
    # record = Comments(cid)
    # record.delete()
