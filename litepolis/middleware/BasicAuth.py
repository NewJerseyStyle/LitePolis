import base64
import binascii

from starlette.authentication import (AuthenticationBackend,
                                      AuthenticationError,
                                      SimpleUser,
                                      AuthCredentials)
from starlette.middleware.authentication import AuthenticationMiddleware

from db import Users

class BasicAuth(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return None

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise AuthenticationError("Invalid basic auth credentials")

        username, _, password = decoded.partition(":")
        user = Users.verify_user(username, password)
        if user is None:
            raise AuthenticationError("Invalid user or password")
        return AuthCredentials(["authenticated"]), SimpleUser(user[2])


def add_middleware(app):
    app.add_middleware(AuthenticationMiddleware, backend=BasicAuth())
    return app
