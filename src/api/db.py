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
    return api_key in api_keys

# CURD of users
def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]

def set_user_from_json(user):
    pass

def delete_user(user_email: str):
    pass

# CURD of conversation
def get_conversation_from_id(uuid: str):
    if uuid is None:
        return list()
    else:
        return "conversation"

def set_conversation_from_json(conv_config):
    pass

def delete_conversation_from_id(uuid: str):
    pass

# CURD of comments
def get_comment_from_id(uuid: str):
    pass

def get_comments_from_conversation(uuid: str, moderated=True, random=False):
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

def get_comments_waiting_for_moderate(uuid: str):
    sql = "SELECT * FROM comments WHERE conversation_uuid=uuid AND moderated=TRUE"
    # get comments in conversation that is not moderated before

def set_comments_from_json(comment):
    uuid = comment.conversation
    # insert or update

def delete_comment_from_uuid(uuid: str):
    pass
