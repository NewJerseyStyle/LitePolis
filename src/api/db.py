"""This module defined the way how the APIs interact with database

The model part of the MVC pattern handles the access to database
and also defines the CRUD methods (Create, Read, Update, Delete)
of tables in the database.

Each class in this module handles the access and all four CRUD
(Create, Read, Update, Delete) operations to a table in database.
- The class `Users` contains methods to do all CRUD operations to the
table `userdata`.
- The class `Conversations` contains methods to do all CRUD operations
to the table `conversationdata`.
- The class `Comments` contains methods to do all CRUD operations to the
table `commentdata`.

In case your environment is manually setup, please ensure the following
environment variables, the connection to database rely on them:
- SQLUSER
- SQLPASS
- SQLHOST
- SQLPORT

Example
-------
To use this module in API endpoints, you have to import the module which
will initialize the database connection using `mysql-connector-python`
library.

.. highlight:: python
.. code-block:: python
    import db


To insert a new record to `userdata`.
.. highlight:: python
.. code-block:: python
    user = Users(email='test@example.com', password='12345678')
    user.create()


Notes
-----
    All classes in this module share same database connection session.
    Creating instances of the classes in the module only initialize the
    data structure of the row about to be affected, *do not* affect the
    existing connection and *do not* establish new connection.
"""

import os
import mysql.connector
from pypika import Query, Table, Values

config = {
    "user": os.environ.get('SQLUSER'),
    "password": os.environ.get('SQLPASS'),
    "host": os.environ.get('SQLHOST'),
    "port": os.environ.get('SQLPORT'),
    "charset": "utf8"
}

# connect to starrocks
try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print("connect to starrocks failed. {}".format(err))
else:
    print("connect to starrocks successfully")

cursor = cnx.cursor()

def check_db_conn_health():
    return cnx.is_connected()

# default apikey read from env for frontend to establish connection
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
    """Verify the API key from client side.

    Parameters
    ----------
    api_key : str
        The API key from client side.

    Returns
    -------
    bool
        True if record of given API Key exist, False otherwise.

    Notes
    -----
        Expire should be added to the API Key records in the future.
    """
    if api_key in api_keys:
        # expire this default one time API key
        return True
    table = Table('apikeys')
    query = Query.from_(table).select('COUNT(*)').where(table.API_KEY == api_key)
    try:
        rows_count = cursor.execute(query.get_sql())
    except mysql.connector.Error as err:
        print("query data failed. {}".format(err))
    return rows_count > 0

# CURD of users
class Users:
    """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note
    ----
    Do not include the `self` parameter in the ``Parameters`` section.

    Parameters
    ----------
    msg : str
        Human readable string describing the exception.
    code : :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    table : PyPika.Table
        Human readable string describing the exception.
    code : int
        Numeric error code.

    """
    table = Table('userdata')
    def __init__(self, email: str, password: str, privilege: str = 'user'):
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
        self.data = dict()
        if email:
            self.data['email'] = email
        if password:
            self.data['password'] = password
        if privilege:
            self.data['privilege'] = privilege

    @staticmethod
    def get_user_from_api_key(api_key: str):
        """Example function with types documented in the docstring.
    
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:
    
        Parameters
        ----------
        api_key : str
            The second parameter.
    
        Returns
        -------
        tuple
            (EMAIL, PRIVILEGE) if successful, None otherwise.
        """
        table = Table('apikeys')
        query = Query.from_(Users.table).join(table).on(table.USER_ID == Users.table.ID) \
                    .select(Users.table.ID, Users.table.EMAIL, Users.table.PRIVILEGE) \
                    .where(table.API_KEY == api_key)
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchone()

    @staticmethod
    def set_user_from_json(user: dict):
        """Example function with types documented in the docstring.
    
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:
    
        Parameters
        ----------
        param1 : int
            The first parameter.
        """
        query = Query.into(Users.table).columns(*user.keys()).insert(*user.values())
        if 'email' in user:
            query = query.on_duplicate_key_update(Users.table.email, Values(Users.table.email))
        if 'password' in user:
            query = query.on_duplicate_key_update(Users.table.password, Values(Users.table.password))
        if 'privilege' in user:
            query = query.on_duplicate_key_update(Users.table.privilege, Values(Users.table.privilege))
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def create(self):
        """Example function with types documented in the docstring.
    
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:
        """
        # validate for create
        assert 'email' in self.data
        assert 'password' in self.data
        query = Query.into(Users.table).columns(*self.data.keys()).insert(*self.data.values())
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def update(self):
        """Example function with types documented in the docstring.
    
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:
        """
        # validate for update
        self.set_user_from_json(self.data)
    
    def delete(self):
        """Example function with types documented in the docstring.
    
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:
        """
        raise NotImplementedError

# CURD of conversation
class Conversations:
    table = Table('conversationdata')
    def __init__(self, title: str, desc: str, creator_email: str):
        self.data = dict()
        if title:
            self.data['title'] = title
        if desc:
            self.data['desc'] = desc
        if creator_email:
            self.data['creator_email'] = creator_email

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
        raise NotImplementedError

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
        raise NotImplementedError
