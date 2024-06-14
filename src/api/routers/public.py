from fastapi import APIRouter

from db import check_db_conn_health

router = APIRouter()

@router.get("/")
async def get_testroute():
    if check_db_conn_health():
        return {"detail": "OK"}
    return {"detail": "DB conn failed"}
