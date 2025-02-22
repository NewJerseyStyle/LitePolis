import base64
import binascii
from uuid import UUID, uuid4

from starlette.authentication import (AuthenticationBackend,
                                      AuthenticationError,
                                      SimpleUser,
                                      AuthCredentials)
from starlette.middleware.authentication import AuthenticationMiddleware

from db import check_api_key, Users

def get_user(api_key_header: str):
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
    dict
        A dictionary object contain keys ("id", "email", "role")
        if successful, None otherwise.
    """
    user = None
    if is_valid_uuid(api_key_header) and check_api_key(api_key_header):
        user = Users.get_user_from_api_key(api_key_header)
    return user


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


class BasicHeaderAuth(AuthenticationBackend):
    """
    Authentication backend that uses the x-polis header for authentication.
    """
    async def authenticate(self, request):
        """
        Authenticates the user based on the x-polis header.

        Parameters
        ----------
        request : Request
            The incoming request.

        Returns
        -------
        tuple
            A tuple containing the authentication credentials and the user object.
            Returns None if the x-polis header is not present or the authentication fails.
        """
        if "x-polis" not in request.headers:
            return None
        auth = request.headers["x-polis"]
        user = get_user(auth)
        if user is None:
            raise AuthenticationError("Invalid basic auth credentials")
        return AuthCredentials(["authenticated"]), SimpleUser(user[2])


def add_middleware(app):
    """
    Adds the authentication middleware to the FastAPI application.

    Parameters
    ----------
    app : FastAPI
        The FastAPI application.

    Returns
    -------
    FastAPI
        The FastAPI application with the authentication middleware added.
    """
    app.add_middleware(AuthenticationMiddleware, backend=BasicHeaderAuth())
    return app
