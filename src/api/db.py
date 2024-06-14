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

    `mysql-connector-python` used in this module seem to be a bad idea
    for the performance should change to `mysqlclient` in later version.
    Benchmark reference [here](https://stackoverflow.com/questions/43102442/whats-the-difference-between-mysqldb-mysqlclient-and-mysql-connector-python).
"""

import os
import mysql.connector
from pypika import Query, Table

# connect to starrocks
def do_db_conn():
    config = {
        "user": os.environ.get('SQLUSER'),
        "password": os.environ.get('SQLPASS'),
        "host": os.environ.get('SQLHOST'),
        "port": os.environ.get('SQLPORT'),
        "charset": "utf8"
    }

    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print("connect to starrocks failed. {}".format(err))
    print("connect to starrocks successfully")
    return cnx

cnx = do_db_conn()
cursor = cnx.cursor()

def check_db_conn_health():
    return cnx.is_connected()

# default apikey read from env for frontend to establish connection
api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8"
}

# with default user from env
users = {
    "7oDYjo3d9r58EJKYi5x4E8": {
        "uid": 0,
        "email": "root",
        "password": "abc",
        "privilege": "root"
    }
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
    query = Query.from_(table).select('COUNT(*)') \
                .where(table.API_KEY == api_key)
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
    def __init__(self, email: str = None, password: str = None,
                 privilege: str = 'user', uid: int = None):
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
        if uid:
            self.data['id'] = uid
        self.data['privilege'] = privilege

    @staticmethod
    def get_user_id_from_email(email: str):
        query = Query.from_(Users.table) \
                    .select(Users.table.ID) \
                    .where(Users.table.EMAIL == email)
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchone()

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
            (ID, EMAIL, PRIVILEGE) if successful, None otherwise.
        """
        table = Table('apikeys')
        query = Query.from_(Users.table).join(table) \
                    .on(table.USER_ID == Users.table.ID) \
                    .select(Users.table.ID,
                            Users.table.EMAIL,
                            Users.table.PRIVILEGE) \
                    .where(table.API_KEY == api_key)
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchone()

    def create(self):
        """Example function with types documented in the docstring.
    
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:
        """
        # validate for create
        assert 'email' in self.data
        assert 'password' in self.data
        query = Query.into(Users.table) \
                    .columns(*self.data.keys()) \
                    .insert(*self.data.values())
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
        assert 'id' in self.data
        query = Query.update(Users.table)
        has_data_for_update = False
        if 'email' in self.data:
            query = query.set(Users.table.EMAIL,
                              self.data['email'])
            has_data_for_update = True
        if 'password' in self.data:
            query = query.set(Users.table.PASSWORD,
                              self.data['password'])
            has_data_for_update = True
        if 'privilege' in self.data:
            query = query.set(Users.table.PRIVILEGE,
                              self.data['privilege'])
            has_data_for_update = True
        query = query.where(Users.table.ID, self.data['id'])
        assert has_data_for_update
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
    
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
    def __init__(self, title: str = None, desc: str = None,
                 creator_id: int = None, cid: int = None):
        self.data = dict()
        if title:
            self.data['title'] = title
        if desc:
            self.data['desc'] = desc
        if creator_id:
            self.data['creator_id'] = creator_id
        if cid:
            self.data['id'] = cid
        # enable moderation or not

    @staticmethod
    def get_all_conversation(user_id: int = None,
                             user_email: str = None):
        if user_id is None:
            assert user_email
            user_id = Users.get_user_id_from_email(user_email)
        query = Query.from_(Conversations.table).select('*') \
                    .where(Conversations.table.CREATOR_ID == user_id)
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchall()

    def get_conversation_from_id(self):
        assert 'id' in self.data
        query = Query.from_(self.table).select('*') \
                    .where(self.table.ID == self.data['id'])
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchone()
    
    def create(self):
        # validate for create
        assert 'title' in self.data
        assert 'desc' in self.data
        assert 'creator_id' in self.data
        query = Query.into(self.table) \
                    .columns(*self.data.keys()) \
                    .insert(*self.data.values())
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def update(self):
        # validate for update
        assert 'id' in self.data
        query = Query.update(self.table)
        has_data_for_update = False
        if 'title' in self.data:
            query = query.set(self.table.TITLE,
                              self.data['title'])
            has_data_for_update = True
        if 'desc' in self.data:
            query = query.set(self.table.DESCRIPTION,
                              self.data['desc'])
            has_data_for_update = True
        query = query.where(self.table.ID, self.data['id'])
        assert has_data_for_update
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
    
    def delete(self):
        raise NotImplementedError

# CURD of comments
class Comments:
    table = Table('commentdata')
    def __init__(self, comment_id: int = None,  comment: str = None,
                 user_id: int = None, conversation_id: int = None,
                 moderated: bool = False, random: bool = False):
        self.data = dict()
        if comment_id:
            self.data['id'] = comment_id
        if comment:
            self.data['comment'] = comment
        if user_id:
            self.data['user_id'] = user_id
        if conversation_id:
            self.data['conversation_id'] = conversation_id
        self.data['moderated'] = moderated
        self.data['random'] = random

    @staticmethod
    def get_comment_from_id(comment_id: int):
        query = Query.from_(Comments.table).select('*') \
                    .where(Comments.table.ID == comment_id)
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchone()

    def get_comments_from_conversation(self):
        assert 'moderated' in self.data
        assert 'random' in self.data
        assert 'conversation_id' in self.data
        query = Query.from_(self.table).select('*')
        column = self.table.CONVERSATION_ID
        query = query.where(column == self.data['conversation_id'])
        if moderated is True:
            query = query.where(self.table.MODERATED == True)
            query = query.where(self.table.APPROVED == True)
        if random is True:
            # random
            # weighted random by popularity
            # return mix comments
            raise NotImplementedError
            # add vote to database
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchall()

    def get_comments_waiting_for_moderate(self):
        # get comments in conversation that is not moderated before
        assert 'conversation_id' in self.data
        column = self.table.CONVERSATION_ID
        query = Query.from_(self.table).select('*') \
                    .where(column == self.data['conversation_id']) \
                    .where(self.table.MODERATED == False)
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchall()

    def create(self):
        # validate for create
        assert 'comment' in self.data
        assert 'user_id' in self.data
        assert 'conversation_id' in self.data
        column = self.table.CONVERSATION_ID
        query = Query.into(self.table) \
                    .columns(*self.data.keys()) \
                    .insert(*self.data.values())
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def update(self):
        # validate for update
        raise NotImplementedError
        # assert 'id' in self.data
        # assert 'vote' in self.data
        # query = Query.update(self.table) \
        #             .set(self.table.UPVOTE, 1) \
        #             .where(self.table.ID, self.data['id'])
        # try:
        #     cursor.execute(query.get_sql())
        # except mysql.connector.Error as err:
        #     print("query data failed. {}".format(err))

    def delete(self):
        raise NotImplementedError

class API_Keys:
    table = Table('apikeys')
    def __init__(self, apikey: str, user_id: int = None):
        self.data = dict()
        self.data['api_key'] = apikey
        self.data['user_id'] = user_id

    def get_user_id_from_apikey(self):
        query = Query.from_(self.table).select(self.table.USER_ID) \
                    .where(self.table.API_KEY == self.data['api_key'])
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        return cursor.fetchone()

    def create(self):
        # validate for create
        assert 'user_id' in self.user_id
        query = Query.into(self.table) \
                    .columns(*self.data.keys()) \
                    .insert(*self.data.values())
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def update(self):
        # validate for update
        assert 'user_id' in self.user_id
        query = Query.update(self.table) \
                    .set(self.table.API_KEY, self.data['api_key']) \
                    .where(self.table.USER_ID == self.data['user_id'])
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def expire(self):
        query = Query.update(self.table) \
                    .set(self.table.API_KEY, "e65537") \
                    .where(self.table.API_KEY == self.data['api_key'])
        try:
            cursor.execute(query.get_sql())
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
