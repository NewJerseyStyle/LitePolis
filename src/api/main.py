"""This module defines the FastAPI application and includes routers for public and secure APIs.

Routers
-------

* `public`: The public API router, available at `/api/v1/public`.
* `secure`: The secure API router, available at `/api/v1/secure`, which requires authentication.

Dependencies
------------

* `auth.py`: A module that manage user login.

Getting Started
---------------
To run the API, execute the following command:
$ SQLUSER="root" SQLPASS="mysecret" SQLHOST="localhost" SQLPORT="9030" ui="streamlit" fastapi dev main.py --host 0.0.0.0 --port 8000

This will start the API on `http://0.0.0.0:8000` in development mode.

Notes
-----
    The API documentation is available at `http://0.0.0.0:8000/docs` through Swagger.
"""


from fastapi import FastAPI, Depends

from routers import secure, public
from auth import get_user

app = FastAPI()

app.include_router(
    public.router,
    prefix="/api/v1/public"
)
app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)
