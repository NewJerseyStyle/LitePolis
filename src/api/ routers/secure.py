import os

from fastapi import APIRouter, Depends

from auth import get_user

router = APIRouter()

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return user

# user CRUD
@router.get("/users/role")
async def get_userrole(user: dict = Depends(get_user)):
    return user.role

if os.environ['ui'] == 'streamlit':
    @router.get("/users/auth")
    async def get_userauth(user: dict = Depends(get_user)):
        return useryaml

@router.get("/users/profile")
async def get_userprofile(user: dict = Depends(get_user)):
    return user

@router.post("/users/profile")
async def create_userprofile(user: dict = Depends(get_user)):
    return user

@router.put("/users/profile")
async def update_userprofile(user: dict = Depends(get_user)):
    return user

@router.delete("/users/profile")
async def delete_userprofile(user: dict = Depends(get_user)):
    return user

# CURD of conversation
@router.get("/conversations/profile")
async def get_userprofile(user: dict = Depends(get_user)):
    return user

@router.post("/conversations/profile")
async def create_userprofile(user: dict = Depends(get_user)):
    return user

@router.put("/conversations/profile")
async def update_userprofile(user: dict = Depends(get_user)):
    return user

@router.delete("/conversations/profile")
async def delete_userprofile(user: dict = Depends(get_user)):
    return user

# CURD of comments
@router.get("/comments/random")
async def get_comment(user: dict = Depends(get_user)):
    return user

@router.get("/comments/moderate")
async def get_comments(user: dict = Depends(get_user)):
    return user

@router.post("/comments/moderate")
async def create_comment(user: dict = Depends(get_user)):
    return user

@router.put("/comments/moderate")
async def update_comment(user: dict = Depends(get_user)):
    return user

@router.delete("/comments/moderate")
async def delete_comment(user: dict = Depends(get_user)):
    return user
