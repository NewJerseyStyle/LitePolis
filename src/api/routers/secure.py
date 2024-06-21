import os
import re
import uuid
import hashlib

from pydantic import BaseModel
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

# @app.post("/items/", response_model=ResponseMessage)
# https://fastapi.tiangolo.com/advanced/generate-clients/
class UserProfile(BaseModel):
    email: str = None
    password: str = None

class ConversationModel(BaseModel):
    title: str = None
    description: str = None

class CommentModel(BaseModel):
    comment_id: int = None
    comment: str = None
    user_id: int = None
    conversation_id: int = None
    task: str = None
    vote: int = None

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
async def create_userprofile(user_profile: UserProfile,
                             user: dict = Depends(get_user)):
    """Create a new user profile.

    Parameters
    ----------
    user_profile : UserProfile
        User profile information.
    user : dict
        Authenticated user information.
    """
    # Validation
    if None  in [user_profile.email, user_profile.password]:
        raise HTTPException(status_code=400, detail="Invalid password")
    if not re.match(r"'[^@]+@[^@]+\.[^@]+'", user_profile.email):
        raise HTTPException(status_code=400, detail="Invalid email")
    # Sanitization
    data = {
        'email': user_profile.email,
        'password': hashlib.sha1(user_profile.password.encode()).hexdigest()
    }
    # Commit to DB
    new_record = Users(**data)
    new_record.create()

@router.put("/users/profile", tags=["User"])
async def update_userprofile(update_user: UserProfile,
                             user: dict = Depends(get_user)):
    """Update the authenticated user's profile.

    Parameters
    ----------
    update_user : UpdateUserProfile
        User profile information to update.
    user : dict
        Authenticated user information.
    """
    if user['role'] not in ['user', 'root']:
        raise HTTPException(status_code=401, detail="Unauthorized")
    data = {'id': user['id']}
    if update_user.email:
        data['email'] = update_user.email
    if update_user.password:
        data['password'] = hashlib.sha1(update_user.password.encode()).hexdigest()
    new_record = Users(**data)
    new_record.update()

@router.delete("/users/profile", tags=["User"])
async def delete_userprofile(user: dict = Depends(get_user)):
    raise HTTPException(status_code=403, detail="Method Not Allowed")
    # raise HTTPException(status_code=501, detail="Not Implemented")

# CURD of conversation
@router.get("/conversations/all", tags=["Conversations"])
async def get_all_conversations(user: dict = Depends(get_user)):
    """Get all conversations for the authenticated user.

    Returns
    -------
    dict
        A dictionary containing all conversations for the user.
    """
    return {
        'detail': Conversations.get_all_conversation(user['id'])
    }

@router.get("/conversations/{cid}", tags=["Conversations"])
async def get_conversation(cid: int,
                           user: dict = Depends(get_user)):
    """Get a conversation by ID.

    Returns
    -------
    dict
        A dictionary containing the conversation details.
    """
    record = Conversations(cid=cid)
    return record.get_conversation_from_id()

@router.post("/conversations", tags=["Conversations"])
async def create_conversation(create_conversation: ConversationModel,
                              user: dict = Depends(get_user)):
    """Create a new conversation.

    Parameters
    ----------
    create_conversation : ConversationModel
        Conversation information to create.
    user : dict
        Authenticated user information.
    """
    if user['role'] != 'user' or None in [create_conversation.title,
                                          create_conversation.description]:
        raise HTTPException(status_code=401, detail="Unauthorized")
    data = {'creator_id': user['id'],
            'title': create_conversation.title,
            'desc': create_conversation.description}
    new_record = Conversations(**data)
    new_record.create()

@router.put("/conversations", tags=["Conversations"])
async def update_conversation(update_conversation: ConversationModel,
                              user: dict = Depends(get_user)):
    """Update a conversation.

    Parameters
    ----------
    update_conversation : ConversationModel
        Conversation update information.
    user : dict
        Authenticated user information.
    """
    data = {'creator_id': user['id']}
    if update_conversation.title:
        data['title'] = update_conversation.title
    if update_conversation.description:
        data['desc'] = update_conversation.description
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
    """Get comments waiting for moderation from a conversation.

    Returns
    -------
    dict
        A dictionary containing comments waiting for moderation.
    """
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
async def create_comment(comment: CommentModel,
                         user: dict = Depends(get_user)):
    """Create a new comment.
    """
    if user['role'] != 'user':
        raise HTTPException(status_code=401, detail="Unauthorized")
    if None in [comment.comment_id,
                comment.comment,
                comment.user_id,
                comment.conversation_id,
                comment.task,
                comment.vote]:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    new_record = Comments(**comment.dict(exclude_none=True))
    new_record.create()

@router.put("/comments/", tags=["Comments"])
async def update_comment(comment: CommentModel,
                         user: dict = Depends(get_user)):
    """Update a comment.
    """
    if user['role'] != 'user':
        raise HTTPException(status_code=401, detail="Unauthorized")
    if comment.comment_id is None:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    record = Comments(**comment.dict(exclude_unset=True))
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
