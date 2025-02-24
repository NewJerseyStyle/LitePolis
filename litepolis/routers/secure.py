import os
import re
import uuid
import hashlib
from typing import List, Union

from pydantic import BaseModel, EmailStr
from fastapi import APIRouter, Depends
from fastapi import HTTPException

from middleware.BasicHeaderAuth import get_user
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

class UserProfile(BaseModel):
    email: EmailStr | None = None
    password: str | None = None

class ConversationModel(BaseModel):
    id: int | None = None
    title: str | None = None
    description: str | None = None

class CommentModel(BaseModel):
    comment_id: int | None = None
    comment: str | None = None
    user_id: int | None = None
    conversation_id: int | None = None
    task: str | None = None
    vote: int | None = None

class UserResponseMessage(BaseModel):
    id: int
    email: str
    role: str
    
class ConversationResponseMessage(BaseModel):
    id: int
    title: str
    description: str
    creator_id: int
    moderation: bool | None = None

class CommentResponseMessage(BaseModel):
    id: int
    create_date: str
    comment: str
    user_id: int
    conversation_id: int
    moderated: bool = False
    approved: bool = False

class ResponseMessage(BaseModel):
    detail: Union[str,
                  UserResponseMessage,
                  ConversationResponseMessage,
                  CommentResponseMessage]
    error: str | None = None
    message: str | None = None
    status_code: int = 200

class ConversationResponse(ResponseMessage):
    detail: str | List[ConversationResponseMessage]
    
class CommentResponse(ResponseMessage):
    detail: str | List[CommentResponseMessage]

router = APIRouter()

@router.get("/", tags=["User"], response_model=ResponseMessage)
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
    ResponseMessage
        `detail` is `UserResponseMessage` containing the user's id, email, and role.
    """
    return ResponseMessage(
        message="User information",
        detail=UserResponseMessage(
            id=user['id'],
            email=user['email'],
            role=user['role']
        )
    )

# user CRUD
@router.get("/users/role", tags=["User"], response_model=ResponseMessage)
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
    ResponseMessage
        `detail` string of the user's role.
    """
    return ResponseMessage(
        message="User information",
        detail=user['role']
    )

@router.put("/users/renew",
            tags=["User", "API Keys"],
            response_model=ResponseMessage)
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
    ResponseMessage
        `detail` is the string of the new API key.
    """
    api_key_not_updated = True
    while api_key_not_updated:
        new_api_key = str(uuid.uuid4())
        api_key = API_Keys(new_api_key, user['id'])
        if api_key.get_user_id_from_apikey() is None:
            api_key.update()
            api_key_not_updated = False
    return ResponseMessage(message='New API Key',
                           detail=new_api_key)

@router.post("/users/auth", tags=["User"],
            response_model=ResponseMessage)
async def get_userauth(user_profile: UserProfile,
                       user: dict = Depends(get_user)):
    # user is the default user with ClientSideAPIKey
    assert user['role'] == 'GUI'
    User(email=user_profile.email,
         password=user_profile.password)
    uid = User.get_user_id_from_email(user_profile.email)
    if uid is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
        # return ResponseMessage(message="User information",
        #                        detail="None")
    if User.verify_user(id=uid, passwd=user_profile.password) is None:
        raise HTTPException(status_code=403, detail="Unauthorized")
    api_key_not_updated = True
    while api_key_not_updated:
        new_api_key = str(uuid.uuid4())
        api_key = API_Keys(new_api_key, user['id'])
        if api_key.get_user_id_from_apikey() is None:
            api_key.create()
            api_key_not_updated = False
    return ResponseMessage(message='New API Key',
                           detail=new_api_key)

@router.get("/users/profile", tags=["User"], response_model=ResponseMessage)
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
    ResponseMessage
        `detail` is `UserResponseMessage` containing the user's id, email, and role.
    """
    return ResponseMessage(
        message="User information",
        detail=UserResponseMessage(
            id=user['id'],
            email=user['email'],
            role=user['role']
        )
    )

@router.post("/users/profile", tags=["User"],
            response_model=ResponseMessage)
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
    if None in [user_profile.email, user_profile.password]:
        raise HTTPException(status_code=400, detail="Invalid password")
    # Sanitization
    if (user['role'] == 'guest' and
        Users.get_user_id_from_email(user.email) is not None):
        user['role'] = 'user'
        update_userprofile(user_profile, user)
    data = {
        'email': user_profile.email,
        'password': hashlib.sha1(user_profile.password.encode()).hexdigest()
    }
    # Commit to DB
    new_record = Users(**data)
    new_record.create()
    return await update_usertoken(user)

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
    data = {'uid': user['id']}
    if update_user.email:
        data['email'] = update_user.email
    if update_user.password is not None:
        if len(update_user.password) != 32:
            raise HTTPException(status_code=400, detail="Invalid parameter")
        data['password'] = hashlib.sha1(update_user.password.encode()).hexdigest()
    new_record = Users(**data)
    new_record.update()

@router.delete("/users/profile", tags=["User"])
async def delete_userprofile(user: dict = Depends(get_user)):
    raise HTTPException(status_code=403, detail="Method Not Allowed")
    # raise HTTPException(status_code=501, detail="Not Implemented")

# CURD of conversation
@router.get("/conversations/all", tags=["Conversations"],
            response_model=ConversationResponse)
async def get_all_conversations(user: dict = Depends(get_user)):
    """Get all conversations for the authenticated user.

    Returns
    -------
    dict
        A dictionary containing all conversations for the user.
    """
    return ConversationResponse(
        message='List of conversation configurations',
        detail=[ConversationResponseMessage(id=record["id"],
                                            title=record["title"],
                                            description=record["description"],
                                            creator_id=record["creator_id"])
                for record in Conversations.get_all_conversation(user['id'])]
    )

@router.get("/conversations/{cid}", tags=["Conversations"],
            response_model=ResponseMessage)
async def get_conversation(cid: int,
                           user: dict = Depends(get_user)):
    """Get a conversation by ID.

    Returns
    -------
    dict
        A dictionary containing the conversation details.
    """
    record = Conversations(cid=cid)
    record = record.get_conversation_from_id()
    return ResponseMessage(
        message='Conversation configurations',
        detail=ConversationResponseMessage(id=record["id"],
                                           title=record["title"],
                                           description=record["description"],
                                           creator_id=record["creator_id"])
    )

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
    if user['role'] not in ['user']:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if update_conversation.id is None:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    data = {
        'creator_id': user['id'],
        'cid': update_conversation.id
    }
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
@router.get("/comments/{cid}/", tags=["Comments"],
            response_model=CommentResponse)
async def get_comments(cid: int,
                       random: bool = True,
                       moderated: bool = False,
                       user: dict = Depends(get_user)):
    comment = Comments(conversation_id=cid,
                       random=random,
                       moderated=moderated)
    return CommentResponse(
        message='List of Comments in the conversation',
        detail=[CommentResponseMessage(id=record['id'],
                                       create_date=record['create_date'],
                                       comment=record['comment'],
                                       user_id=record['user_id'],
                                       conversation_id=record['conversation_id'],
                                       moderated=record['moderated'],
                                       approved=record['approved'])
                for record in comment.get_comments_from_conversation()]
    )

@router.get("/comments/{cid}/moderate", tags=["Comments"],
            response_model=CommentResponse)
async def get_comments_for_moderation(cid: int, user: dict = Depends(get_user)):
    """Get comments waiting for moderation from a conversation.

    Returns
    -------
    dict
        A dictionary containing comments waiting for moderation.
    """
    # waiting to be moderated comments if conversation moderation enabled
    record = Conversations(cid=cid)
    data = record.get_conversation_from_id()
    # if the conversation is moderation enabled
    if data['moderation'] is True:
        comment = Comments(conversation_id=cid)
        return CommentResponse(
            message='List of Comments waiting for moderation in the conversation',
            detail=[CommentResponseMessage(id=record['id'],
                                           create_date=record['create_date'],
                                           comment=record['comment'],
                                           user_id=record['user_id'],
                                           conversation_id=record['conversation_id'],
                                           moderated=record['moderated'],
                                           approved=record['approved'])
                    for record in comment.get_comments_waiting_for_moderate()])
    err = "Invalid parameter, the conversation is not moderation enabled"
    return CommentResponse(status_code=400,
                           detail=err,
                           error=err)

@router.post("/comments/", tags=["Comments"])
async def create_comment(comment: CommentModel,
                         user: dict = Depends(get_user)):
    """Create a new comment.
    """
    if user['role'] not in ['guest', 'user']:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if None in [comment.comment,
                comment.conversation_id]:
        raise HTTPException(status_code=400, detail="Invalid parameter")
    comment.user_id = user['id']
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
    if comment.task == 'approve':
        record.approve()
    elif comment.task == 'reject':
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
