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
import datetime
import mysql.connector
from pypika import Query, Table

# connect to starrocks
def do_db_conn():
    config = {
        "user": os.environ.get('SQLUSER'),
        "password": os.environ.get('SQLPASS'),
        "host": os.environ.get('SQLHOST'),
        "port": os.environ.get('SQLPORT'),
        "database": "litepolis",
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
    table = Table('apikeys')
    query = Query.from_(table).select('COUNT(*)') \
                .where(table.API_KEY == api_key)
    try:
        cursor.execute(query.get_sql().replace('"', ''))
    except mysql.connector.Error as err:
        print("query data failed. {}".format(err))
    rows_count = cursor.fetchone()
    return rows_count is not None and rows_count[0] > 0

# CURD of users
class Users:
    """Represents a user in the system.

    Attributes
    ----------
    table : PyPika.Table
        The database table for users.

    Methods
    -------
    __init__(email, password, privilege, uid)
        Initializes a new user object.

    get_user_id_from_email(email)
        Retrieves the user ID from the database based on the email address.

    get_user_from_api_key(api_key)
        Retrieves the user information from the database based on the API key.

    create()
        Creates a new user in the database.

    update()
        Updates an existing user in the database.

    delete()
        Deletes a user from the database (not implemented).

    Parameters
    ----------
    email : str
        The email address of the user.
    password : str, optional
        The password of the user.
    privilege : str, optional
        The privilege level of the user (default: 'user').
    uid : int, optional
        The user ID (default: None).

    Examples
    --------
    .. highlight:: python
    .. code-block:: python
        user = Users("john.doe@example.com", "mysecretpassword", "user")

    Notes
    -----
    This class provides a simple interface for managing users in the system.
    """
    table = Table('userdata')
    def __init__(self, email: str, password: str = None,
                 privilege: str = 'user', uid: int = None):
        """Initializes a new user object.
    
        Parameters
        ----------
        email : str
            The email address of the user.
        password : str, optional
            The password of the user.
        privilege : str, optional
            The privilege level of the user (default: 'user').
        uid : int, optional
            The user ID (default: None).
            """
        self.data = dict()
        self.data['email'] = email
        if password is not None:
            self.data['password'] = password
        if uid is not None:
            self.data['id'] = uid
        self.data['privilege'] = privilege

    @staticmethod
    def verify_user(id: int, passwd: str):
        query = Query.from_(Users.table) \
                    .select(Users.table.ID) \
                    .where(Users.table.ID == id) \
                    .where(Users.table.PASSWORD == passwd)
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        result = cursor.fetchone()
        return result if result is None else result[0]


    @staticmethod
    def get_user_id_from_email(email: str):
        """Retrieves the user ID from the database based on the email address.

        It is a static method so initialization of the class is not required.

        Parameters
        ----------
        email : str
            The email address of the user.

        Returns
        -------
        int
            The user ID associated with the email address, or None if not found.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            user_id = Users.get_user_id_from_email("john.doe@example.com")
            print(user_id)  # Output: 1 (assuming the user ID is 1)

        Notes
        -----
        This method executes a SQL query to retrieve the user ID from the database.
        """
        query = Query.from_(Users.table) \
                    .select(Users.table.ID) \
                    .where(Users.table.EMAIL == email)
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        result = cursor.fetchone()
        return result if result is None else result[0]

    @staticmethod
    def get_user_from_api_key(api_key: str):
        """Retrieves the user information from the database based on the API key.

        It is a static method so initialization of the class is not required.

        Parameters
        ----------
        api_key : str
            The API key associated with the user.

        Returns
        -------
        dict
            A dictionary containing the user's "id", "email", and "role"
            if database retrieval is successful, otherwise return `None`.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            api_key = "my_secret_api_key"
            user_info = Users.get_user_from_api_key(api_key)
            print(user_info)  # Output: {"id": 1, "email": "john.doe@example.com", "role": "user"}

        Notes
        -----
        This method executes a SQL query to retrieve the user information from the database based on the API key.
        """
        table = Table('apikeys')
        query = Query.from_(Users.table).join(table) \
                    .on(table.USER_ID == Users.table.ID) \
                    .select(Users.table.ID,
                            Users.table.EMAIL,
                            Users.table.PRIVILEGE) \
                    .where(table.API_KEY == api_key)
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        data = cursor.fetchone()
        return {
            "id": data[0],
            "email": data[1],
            "role": data[2]
        }

    def create(self):
        """Creates a new user in the database based on the information provided
        to initialize the instance.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            user = Users("john.doe@example.com", "mysecretpassword", "admin")
            user.create()

        Notes
        -----
        This method executes a SQL query to insert a new user into the database.
        """
        # validate for create
        assert 'email' in self.data
        assert 'password' in self.data
        query = Query.into(Users.table) \
                    .columns(*self.data.keys()) \
                    .insert(*self.data.values())
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def update(self):
        """Updates an existing user in the database based on the information provided
        to initialize the instance.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            user = Users("john.doe.newemail@example.com", "mynewpassword", "user", 1)
            user.update()

        Notes
        -----
        This method executes a SQL query to update an existing user in the database.
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
        query = query.where(Users.table.ID == self.data['id'])
        assert has_data_for_update
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
    
    def delete(self):
        """Deletes a user from the database.

        Notes
        -----
        This method is not implemented yet. It will raise a NotImplementedError.

        Raises
        ------
        NotImplementedError
            This method is not implemented yet.
        """
        raise NotImplementedError

# CURD of conversation
class Conversations:
    """Represents a conversation in polis.

    A conversation is a space to contain comments
    and allow users to submit or vote on comments.

    The title and description of conversation should build context
    for users to know what are they doing in the conversation page
    what are the expected behavior and the background information 
    they need to know before take any action on the web page.

    Attributes
    ----------
    title : str
        The title of the conversation.
    desc : str
        The description of the conversation.
    creator_id : int
        The ID of the user who created the conversation.
    cid : int
        The ID of the conversation.

    Methods
    -------
    get_all_conversation(user_id: int = None, user_email: str = None)
        Retrieves all conversations for a given user.
    get_conversation_from_id()
        Retrieves a conversation by ID.
    create()
        Creates a new conversation.
    update()
        Updates an existing conversation.
    delete()
        Deletes a conversation (not implemented).

    Examples
    --------
    .. highlight:: python
    .. code-block:: python
        conversation = Conversations("My Conversation", "This is a conversation", 1)

    Notes
    -----
    The `delete` method is not implemented yet and will raise a NotImplementedError.
    """
    table = Table('conversationdata')
    def __init__(self, title: str = None, desc: str = None,
                 creator_id: int = None, cid: int = None):
        """Initializes a Conversation object.

        Parameters
        ----------
        title : str, optional
            The title of the conversation.
        desc : str, optional
            The description of the conversation.
        creator_id : int, optional
            The ID of the user who created the conversation.
        cid : int, optional
            The ID of the conversation.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            conversation = Conversations("My Conversation", "This is a conversation", 1)
        """
        self.data = dict()
        if title is not None:
            self.data['title'] = title
        if desc is not None:
            self.data['desc'] = desc
        if creator_id is not None:
            self.data['creator_id'] = creator_id
        if cid is not None:
            self.data['id'] = cid
        # enable moderation or not

    @staticmethod
    def get_all_conversation(user_id: int = None,
                             user_email: str = None):
        """Retrieves all conversations for a given user.

        This method executes a SQL query to retrieve all conversations for a given user.
        If `user_id` is not provided, it will be retrieved from the `user_email`.

        Parameters
        ----------
        user_id : int, optional
            The ID of the user.
        user_email : str, optional
            The email of the user.

        Returns
        -------
        list
            A list of conversations for the given user.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            conversations = Conversations.get_all_conversation(user_id=1)
            for conversation in conversations:
                print(conversation)

        .. highlight:: python
        .. code-block:: python
            conversations = Conversations.get_all_conversation(user_email="john.doe@example.com")
            for conversation in conversations:
                print(conversation)
            # [
            #     {
            #         "id": 1,
            #         "title": "Test conversation",
            #         "description": "A demo",
            #         "creator_id": 1,
            #     }
            # ]
        """
        if user_id is None:
            assert user_email
            user_id = Users.get_user_id_from_email(user_email)
        query = Query.from_(Conversations.table).select('*') \
                    .where(Conversations.table.CREATOR_ID == user_id)
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        data = []
        for record in cursor.fetchall():
            data.append({
                "id": record[0],
                "title": record[1],
                "description": record[2],
                "creator_id": record[3],
                # "moderation": record[4]
            })
        return data

    def get_conversation_from_id(self):
        """Retrieves a conversation by ID.

        This method executes a SQL query to retrieve a conversation by ID.
        The `id` must be present in the `data` attribute of the Conversation object.

        Returns
        -------
        dict
            A dictionary containing the conversation data 
            ("id", "title", "description", "creator_id").

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            conversation = Conversations(cid=1)
            conversation_data = conversation.get_conversation_from_id()
            print(conversation_data)
            # {
            #     "id": 1,
            #     "title": "Test conversation",
            #     "description": "A demo",
            #     "creator_id": 1,
            # }
        """
        assert 'id' in self.data
        query = Query.from_(self.table).select('*') \
                    .where(self.table.ID == self.data['id'])
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        record = cursor.fetchone()
        return {
            "id": record[0],
            "title": record[1],
            "description": record[2],
            "creator_id": record[3],
            # "moderation": record[4]
            "moderation": False # moderation implemented in database yet
        }
    
    def create(self):
        """Creates a new conversation.

        This method executes a SQL query to create a new conversation.
        The `title`, `desc`, and `creator_id` must be present in the `data` attribute of the Conversation object.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            conversation = Conversations("My Conversation", "This is a conversation", 1)
            conversation.create()
        """
        # validate for create
        assert 'title' in self.data
        assert 'desc' in self.data
        assert 'creator_id' in self.data
        query = Query.into(self.table) \
                    .columns('NAME', 'DESCRIPTION', 'CREATOR_ID') \
                    .insert(self.data['title'],
                            self.data['desc'],
                            self.data['creator_id'])
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
 
    def update(self):
        """Updates an existing conversation.

        This method executes a SQL query to update an existing conversation.
        The `id` must be present in the `data` attribute of the Conversation object.
        At least one of `title` or `desc` must be present in the `data` attribute to update.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            conversation = Conversations(title="New Title", cid=1)
            conversation.data['desc'] = 'New Description'
            conversation.update()
        """
        # validate for update
        assert 'id' in self.data
        query = Query.update(self.table)
        has_data_for_update = False
        if 'title' in self.data:
            query = query.set(self.table.NAME,
                              self.data['title'])
            has_data_for_update = True
        if 'desc' in self.data:
            query = query.set(self.table.DESCRIPTION,
                              self.data['desc'])
            has_data_for_update = True
        query = query.where(self.table.ID == self.data['id'])
        assert has_data_for_update
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
    
    def delete(self):
        """Deletes a conversation.

        Raises
        ------
        NotImplementedError
            This method is not implemented.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            conversation = Conversations(cid=1)
            conversation.delete() # NotImplementedError: This method is not implemented.

        Notes
        -----
        This method is not implemented and will raise a NotImplementedError.
        """
        raise NotImplementedError

# CURD of comments
class Comments:
    """Represents a comment in a conversation.

    Parameters
    ----------
    comment_id : int, optional
        The ID of the comment.
    comment : str, optional
        The text of the comment.
    user_id : int, optional
        The ID of the user who made the comment.
    conversation_id : int, optional
        The ID of the conversation that the comment belongs to.
    moderated : bool, optional
        Whether the comment has been moderated.
    random : bool, optional
        Whether the comment should be displayed randomly.

    Attributes
    ----------
    data : dict
        A dictionary containing the comment data.

    Examples
    --------
    .. highlight:: python
    .. code-block:: python
        comment = Comments(comment="Hello, world!", user_id=1, conversation_id=1)

    Methods
    -------
    get_comment_from_id(comment_id: int) -> tuple
        Retrieves a comment by ID.

    get_comments_from_conversation() -> list
        Retrieves comments from a conversation.

    get_comments_waiting_for_moderate() -> list
        Retrieves comments in a conversation that are not moderated.

    create() -> None
        Creates a new comment.

    update() -> None
        Updates an existing comment.

    delete() -> None
        Deletes a comment.
    """
    table = Table('commentdata')
    def __init__(self, comment_id: int = None,  comment: str = None,
                 user_id: int = None, conversation_id: int = None,
                 moderated: bool = False, random: bool = False):
        """Initializes a new Comment object.

        This method initializes a new Comment object with the provided parameters.
        The `data` attribute is a dictionary that stores the comment data.

        Parameters
        ----------
        comment_id : int, optional
            The ID of the comment.
        comment : str, optional
            The text of the comment.
        user_id : int, optional
            The ID of the user who made the comment.
        conversation_id : int, optional
            The ID of the conversation that the comment belongs to.
        moderated : bool, optional
            Whether the comment has been moderated. Defaults to False.
        random : bool, optional
            Whether the comment should be displayed randomly. Defaults to False.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments(comment="Hello, world!", user_id=1, conversation_id=1)
        """
        self.data = dict()
        if comment_id is not None:
            self.data['id'] = comment_id
        if comment is not None:
            self.data['comment'] = comment
        if user_id is not None:
            self.data['user_id'] = user_id
        if conversation_id is not None:
            self.data['conversation_id'] = conversation_id
        self.data['moderated'] = moderated
        self.data['random'] = random

    @staticmethod
    def get_comment_from_id(comment_id: int):
        """Retrieves a comment by ID.

        This method executes a SQL query to retrieve a comment by ID.
        It returns a tuple containing the comment data.

        Parameters
        ----------
        comment_id : int
            The ID of the comment to retrieve.

        Returns
        -------
        dict
            A dictionary object containing the comment data.
            Keys including ("id", "create_date", "comment",
            "user_id", "conversation_id", "moderated", "approved")
        }

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments.get_comment_from_id(1)
            print(comment)
            # {"id": 1, "create_date": "2012-11-15 00:00:00",
            #  "comment": 'Hello, world!', "user_id": 1,
            #  "conversation_id": 1, "moderated": False,
            #  "approved": False)
        """
        query = Query.from_(Comments.table).select('*') \
                    .where(Comments.table.ID == comment_id)
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        record = cursor.fetchone()
        return {
            "id": record[0],
            "create_date": record[1],
            "comment": record[2],
            "user_id": record[3],
            "conversation_id": record[4],
            "moderated": record[5],
            "approved": record[6],
        }

    def get_comments_from_conversation(self):
        """Retrieves comments from a conversation.

        This method executes a SQL query to retrieve comments from a conversation.
        It returns a list of dictionaries containing the comment data.
        The query can be filtered by moderated or random flags.

        Returns
        -------
        list
            A list of dict containing the comment data.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments(conversation_id=1, moderated=True, random=False)
            comments = comment.get_comments_from_conversation()
            for comment in comments:
                print(comment)
            # {"id": 1, "create_date": "2014-01-24", "comment": 'Comment 1!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)
            # {"id": 2, "create_date": "2014-09-25", "comment": 'Comment 2!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)
            # {"id": 3, "create_date": "2014-11-26", "comment": 'Comment 3!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)

            
        .. highlight:: python
        .. code-block:: python
            comment = Comments(conversation_id=1, moderated=True, random=True)
            comments = comment.get_comments_from_conversation()
            for comment in comments:
                print(comment)
            # {"id": 2, "create_date": "2014-09-25", "comment": 'Comment 2!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)
            # {"id": 3, "create_date": "2014-11-26", "comment": 'Comment 3!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)
            # {"id": 1, "create_date": "2014-01-24", "comment": 'Comment 1!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)
        """
        assert 'moderated' in self.data
        assert 'random' in self.data
        assert 'conversation_id' in self.data
        query = Query.from_(self.table).select('*')
        column = self.table.CONVERSATION_ID
        query = query.where(column == self.data['conversation_id'])
        if self.data['moderated'] is True:
            query = query.where(self.table.MODERATED == True)
            query = query.where(self.table.APPROVED == True)
        if self.data['random'] is True:
            # random
            # weighted random by popularity
            # return mix comments
            raise NotImplementedError
            # add vote to database
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        data = []
        for record in cursor.fetchall():
            data.append({
                "id": record[0],
                "create_date": record[1],
                "comment": record[2],
                "user_id": record[3],
                "conversation_id": record[4],
                "moderated": record[5],
                "approved": record[6],
            })
        return data

    def get_comments_waiting_for_moderate(self):
        """Retrieves comments from a conversation that are waiting for moderation.

        This method executes a SQL query to retrieve comments from a conversation
        that are waiting for moderation.
        The query filters comments that have not been moderated before.

        Returns
        -------
        list
            A list of dict containing the comment data.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments(conversation_id=1)
            comments = comment.get_comments_waiting_for_moderate()
            for comment in comments:
                print(comment)
            # {"id": 1, "create_date": "2014-01-24", "comment": 'Comment 1!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)
            # {"id": 2, "create_date": "2014-09-25", "comment": 'Comment 2!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)
            # {"id": 3, "create_date": "2014-11-26", "comment": 'Comment 3!',
            #  "user_id": 1, "conversation_id": 1, "moderated": False,
            #  "approved": False)
        """
        # get comments in conversation that is not moderated before
        assert 'conversation_id' in self.data
        column = self.table.CONVERSATION_ID
        query = Query.from_(self.table).select('*') \
                    .where(column == self.data['conversation_id']) \
                    .where(self.table.MODERATED == False)
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        data = []
        for record in cursor.fetchall():
            data.append({
                "id": record[0],
                "create_date": record[1],
                "comment": record[2],
                "user_id": record[3],
                "conversation_id": record[4],
                "moderated": record[5],
                "approved": record[6],
            })
        return data

    def create(self):
        """Creates a new comment in the database.

        This method executes a SQL query to create a new comment in the database.
        It validates the required fields before creating the comment.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments(comment='Hello, world!', user_id=1, conversation_id=1)
            comment.create()
        """
        # validate for create
        assert 'comment' in self.data
        assert 'user_id' in self.data
        assert 'conversation_id' in self.data
        column = self.table.CONVERSATION_ID
        data = dict([(k, v) for k, v in self.data.items() if k not in ['random']])
        data['CREATE_DATE'] = str(datetime.datetime.now())
        query = Query.into(self.table) \
                    .columns(*data.keys()) \
                    .insert(*data.values())
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def update(self):
        """Updates an existing comment in the database.

        This method executes a SQL query to update an existing comment in the database.
        It validates the required fields before updating the comment.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments(id=1, moderated=True)
            comment.update()
        """
        # validate for update
        assert 'id' in self.data
        assert ('vote' in self.data or
                'moderated' in self.data or
                'approved' in self.data)
        query = Query.update(self.table)
        has_data_for_update = False
        if 'moderated' in self.data:
            query = query.set(self.table.MODERATED,
                              self.data['moderated'])
            has_data_for_update = True
        if 'approved' in self.data:
            query = query.set(self.table.APPROVED,
                              self.data['approved'])
            has_data_for_update = True
        assert has_data_for_update
        query = query.where(self.table.ID == self.data['id'])
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def approve(self):
        """Updates an existing comment in the database status approved.

        This method executes a SQL query to update an existing comment in the database.
        It validates the required fields before updating the comment.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments(id=1)
            comment.approve()
        """
        # validate for update
        assert 'id' in self.data
        self.data['moderated'] = True
        self.data['approved'] = True
        self.update()

    def reject(self):
        """Updates an existing comment in the database status rejected.

        This method executes a SQL query to update an existing comment in the database.
        It validates the required fields before updating the comment.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments(id=1)
            comment.approve()
        """
        # validate for update
        assert 'id' in self.data
        self.data['moderated'] = True
        self.data['approved'] = False
        self.update()

    def delete(self):
        """Deletes a comment from the database.

        This method executes a SQL query to delete a comment from the database.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            comment = Comments(id=1)
            comment.delete()

        Notes
        -----
        **NOT IMPLEMENTED YET**
        """
        raise NotImplementedError

class API_Keys:
    """Represents an API key and its associated user ID.

    This class provides methods for creating, updating, and expiring API keys.
    It also provides a method for retrieving the user ID associated with an API key.

    Parameters
    ----------
    api_key : str
        The API key.
    user_id : int, optional
        The user ID associated with the API key.

    Attributes
    ----------
    data : dict
        A dictionary containing the API key and user ID.

    Methods
    -------
    get_user_id_from_apikey()
        Retrieves the user ID associated with the API key.
    create()
        Creates a new API key in the database.
    update()
        Updates an existing API key in the database.
    expire()
        Expires an API key by setting it to a default value.

    Examples
    --------
    .. highlight:: python
    .. code-block:: python
        api_key = API_Keys(api_key='my_api_key', user_id=1)
        api_key.create()
        api_key.get_user_id_from_apikey()
        # 1
        api_key.update()
        api_key.expire()
    """
    table = Table('apikeys')
    def __init__(self, api_key: str, user_id: int = None):
        """Initializes an API key object.

        This method initializes an API key object with the provided API key and
        user ID. If no user ID is provided, it defaults to None and assuming
        that you want to expire the api_key or you are trying to find the record
        of the user associated with the api_key.

        Parameters
        ----------
        api_key : str
            The API key.
        user_id : int, optional
            The user ID associated with the API key. Defaults to None.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            api_key = API_Keys(api_key='my_api_key', user_id=1)
        """
        self.data = dict()
        self.data['api_key'] = api_key
        if user_id is not None:
            self.data['user_id'] = user_id

    def get_user_id_from_apikey(self):
        """Retrieves the user ID associated with the API key.

        This method executes a SQL query to retrieve the user ID associated with
        the API key. It returns a user ID. It will return None if no record were
        found related to the apikey or associated with the apikey.

        Returns
        -------
        int
            The user ID associated with the API key.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            api_key = API_Keys(api_key='my_api_key', user_id=1)
            api_key.get_user_id_from_apikey()
        """
        query = Query.from_(self.table).select(self.table.USER_ID) \
                    .where(self.table.API_KEY == self.data['api_key'])
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
        # get the first element of tuple (1,)
        result = cursor.fetchone()
        return result if result is None else result[0]

    def create(self):
        """Creates a new API key in the database.

        This method executes a SQL query to create a new API key in the database.
        It validates the required fields before creating the API key.
        Uses for new user, login, expire and renew.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            api_key = API_Keys(api_key='my_api_key', user_id=1)
            api_key.create()
        """
        # validate for create
        assert 'user_id' in self.data
        assert 'api_key' in self.data
        query = Query.into(self.table) \
                    .columns(*self.data.keys()) \
                    .insert(*self.data.values())
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def update(self):
        """Updates an existing API key in the database.

        This method executes a SQL query to update an existing API key in the database.
        It validates the required fields before updating the API key.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            api_key = API_Keys(api_key='my_api_key', user_id=1)
            api_key.update()
        """
        # validate for update
        assert 'user_id' in self.data
        assert 'api_key' in self.data
        self.expire()
        query = Query.into(self.table) \
                    .columns(*self.data.keys()) \
                    .insert(*self.data.values())
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))

    def expire(self):
        """Expires an API key by removing the record.

        This method executes a SQL query to expire an API key by removing it from database,
        effectively expiring it.

        Examples
        --------
        .. highlight:: python
        .. code-block:: python
            api_key = API_Keys(api_key='my_api_key', user_id=1)
            api_key.expire()
        """
        query = Query.from_(self.table).delete() \
                    .where(self.table.API_KEY == self.data['api_key'])
        try:
            cursor.execute(query.get_sql().replace('"', ''))
        except mysql.connector.Error as err:
            print("query data failed. {}".format(err))
