"""This module defined the way how the APIs interact with database

The model part of the MVC pattern handles the access to database
and also defines the CRUD methods (Create, Read, Update, Delete)
of tables in the database.

What is included in this module?

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

# read from env
api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8",
    "5f0c7127-3be9-4488-b801-c7b6415b45e9": "mUP7PpTHmFAkxcQLWKMY8t"
}

# with default user from env
users = {
    "7oDYjo3d9r58EJKYi5x4E8": {
        "name": "Bob"
    },
    "mUP7PpTHmFAkxcQLWKMY8t": {
        "name": "Alice"
    },
}

def check_api_key(api_key: str):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    return api_key in api_keys

# CURD of users
class Users:
    def __init__(self, user_data: dict):
        self.data = user_data

    @staticmethod
    def get_user_from_api_key(api_key: str):
        return users[api_keys[api_key]]

    @staticmethod
    def set_user_from_json(user: dict):
        pass

    def create(self):
        # validate for create
        self.set_user_from_json(self.data)

    def update(self):
        # validate for update
        self.set_user_from_json(self.data)
    
    def delete(self):
        pass

# CURD of conversation
class Conversation:
    def __init__(self, conv_conf: dict):
        self.data = conv_conf

    @staticmethod
    def get_all_conversation(user):
        return list()

    def get_conversation_from_id(self):
        return "conversation"
    
    @staticmethod
    def set_conversation_from_json(conv_config: dict):
        pass
    
    def create(self):
        # validate for create
        self.set_conversation_from_json(self.data)

    def update(self):
        # validate for update
        self.set_conversation_from_json(self.data)

    def delete(self):
        pass

# CURD of comments
class Comments:
    def __init__(self, comment: dict):
        self.data = comment

    def get_comment_from_id(self, uuid: str):
        pass

    def get_comments_from_conversation(self, moderated=True, random=False):
        uuid = self.data.uuid
        if random is True:
            sql = "SELECT * FROM comments WHERE conversation_uuid=uuid"
            if moderated is True:
                sql += " AND approved=TRUE"
            # random
            # weighted random by popularity
            # return mix comments
            pass
        else:
            # return all comments

    def get_comments_waiting_for_moderate(self):
        uuid = self.data.uuid
        sql = "SELECT * FROM comments WHERE conversation_uuid=uuid AND moderated=TRUE"
        # get comments in conversation that is not moderated before

    @staticmethod
    def set_comments_from_json(comment):
        uuid = comment.conversation
        # insert or update

    def create(self):
        # validate for create
        self.set_comments_from_json(self.data)

    def update(self):
        # validate for update
        self.set_comments_from_json(self.data)

    def delete(self):
        pass
