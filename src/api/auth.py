"""This middleware will manage authentication of clients connect to server.

This module depend on `db` module for data retrieval of user record.
And this module is a dependency of `route.secure` API endpoints.

Example
-------
To use this module in API endpoints, you have to import the functions
you want to use in this case we use default `get_user` function for
authentication, and then apply the function in API endpoint as the
default value of function parameter.

    from auth import get_user
    
    router = APIRouter()
    
    @router.get("/")
    async def get_testroute(user: dict = Depends(get_user)):
        return user


Above example is the default example function of `route.secure`
the endpoints that required API key to access where this project start.
"""

from uuid import UUID

from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

from db import check_api_key, Users

api_key_header = APIKeyHeader(name="X-API-Key")

def get_user(api_key_header: str = Security(api_key_header)):
    """This middleware will verify API clients with API key.

    By retrieving coresponding user information with API key `api_key_header`
    and return the coresponding user object, the middleware identify the user
    of the API key and authenticate the client to access other APIs in server.

    Parameters
    ----------
    api_key_header : str
        The API key included in the HTTP header.

    Returns
    -------
    tuple
        A tuple object contain (ID, EMAIL, PRIVILEGE)
        if successful, None otherwise.

    Notes
    -----
    For future development, automated login process through public key
    signature verification similar to SSL handshake would be a nice upgrade.
    """
    if is_valid_uuid(api_key_header) and check_api_key(api_key_header):
        user = Users.get_user_from_api_key(api_key_header)
        if user is not None:
            return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing or invalid API key"
    )


def is_valid_uuid(uuid_to_test, version=4):
    """Check if uuid_to_test is a valid UUID.
    
     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}
    
     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.
    
     Examples
    --------
    .. highlight:: python
    .. code-block:: python
        is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
        # return: True
        is_valid_uuid('c9bf9e58')
        # return: False
    """
    
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test