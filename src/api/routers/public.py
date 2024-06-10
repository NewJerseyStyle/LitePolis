from fastapi import APIRouter

from db import check_db_conn_health

router = APIRouter()

@router.get("/")
async def get_testroute():
    return "OK" if check_db_conn_health() else "DB conn failed"
