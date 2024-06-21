"""This module defines a FastAPI router for a health check endpoint.

The endpoint `/` checks the health of the database connection by calling
the `check_db_conn_health` function from the `db` module.

Example:
-------
To use this module in your FastAPI application, import the router and include
it in your main application.

.. highlight:: python
.. code-block:: python
    from fastapi import FastAPI
    from health_check import router

    app = FastAPI()
    app.include_router(router)
"""

from fastapi import APIRouter

from db import check_db_conn_health

router = APIRouter()

@router.get("/")
async def get_testroute():
    """This endpoint is used to check if the database connection is healthy.

    Returns
    -------
    dict
        A dictionary containing the status of the database connection.
        - If the connection is healthy, the dictionary will contain
        {"detail": "OK"}.
        - If the connection is not healthy, the dictionary will contain
        {"detail": "DB conn failed"}.
    """
    if check_db_conn_health():
        return {"detail": "OK"}
    return {"detail": "DB conn failed"}
