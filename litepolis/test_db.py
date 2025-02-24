import unittest

from db import Users, Conversations, Comments, API_Keys


class TestUsers(unittest.TestCase):
    def test_init(self):
        user = Users("john.doe@example.com", "mysecretpassword", "user", 1)
        self.assertEqual(user.data, {'id': 1,
                                     'privilege': 'user',
                                     'password': 'mysecretpassword',
                                     'email': "john.doe@example.com"})

    def test_create(self):
        user = Users("john.doe@example.com", "mysecretpassword", "user", 1)
        user.create()
        self.assertEqual(Users.get_user_id_from_email("john.doe@example.com"), 1)

    def test_update(self):
        user = Users("john.doe.newemail@example.com", "mynewpassword", "user", 1)
        user.update()
        self.assertEqual(Users.get_user_id_from_email("john.doe@example.com"), None)
        self.assertEqual(Users.get_user_id_from_email("john.doe.newemail@example.com"), 1)

    def test_delete(self):
        user = Users("john.doe@example.com")
        with self.assertRaises(NotImplementedError):
            user.delete()


class TestConversations(unittest.TestCase):
    def test_init(self):
        conversation = Conversations(cid=1, creator_id=1,
                                     title='Test Conversation')
        self.assertEqual(conversation.data,
                         {'id': 1, 'creator_id': 1, 'title': 'Test Conversation'})

    def test_create_and_get_all_conversation(self):
        conversation = Conversations(creator_id=1,
                                     title='Test Conversation',
                                     desc='Test Description')
        conversation.create()
        lst = Conversations.get_all_conversation(1)
        self.assertGreater(len(lst), 0)
        self.assertEqual(lst[0]["title"], 'Test Conversation')
        conversation = Conversations(cid=lst[0]["id"],
                                     creator_id=1,
                                     title='Updated Conversation Title')
        c = conversation.get_conversation_from_id()
        self.assertIsNotNone(c)
        self.assertEqual(c["title"], 'Test Conversation')
        conversation.update()
        c = conversation.get_conversation_from_id()
        self.assertIsNotNone(c)
        self.assertEqual(c["title"], 'Updated Conversation Title')

    def test_delete(self):
        # conversation = Conversations(cid=1)
        # conversation.delete()
        pass


class TestComments(unittest.TestCase):
    def test_init(self):
        comment = Comments(comment_id=1, user_id=1, comment='This is a test comment')
        self.assertEqual(comment.data, {'id': 1,
                                        'user_id': 1,
                                        'comment': 'This is a test comment',
                                        'moderated': False,
                                        'random': False,
                                       })

    def test_create(self):
        comment = Comments(user_id=1,
                           conversation_id=1,
                           comment='This is a test comment')
        comment.create()
        self.assertEqual(comment.get_comment_from_id(1)["comment"], 'This is a test comment')
        lst = comment.get_comments_from_conversation()
        self.assertGreater(len(lst), 0)
        self.assertEqual(lst[0]["comment"], 'This is a test comment')
        lst = comment.get_comments_waiting_for_moderate()
        self.assertGreater(len(lst), 0)
        self.assertEqual(lst[0]["comment"], 'This is a test comment')
        comment.data['id'] = id
        comment.data['moderated'] = True
        comment.update()
        comment.data['moderated'] = False
        lst = comment.get_comments_from_conversation()
        self.assertEqual(len(lst), 1)
        lst = comment.get_comments_waiting_for_moderate()
        self.assertEqual(len(lst), 0)
        comment.data['moderated'] = True
        lst = comment.get_comments_from_conversation()
        self.assertGreater(len(lst), 0)

    def test_delete(self):
        # comment = Comments(comment_id=1,
        #                    conversation_id=0,
        #                    user_id=1,
        #                    comment='This is a test comment')
        # comment.delete()
        pass


class TestAPI_Keys(unittest.TestCase):
    def test_init(self):
        api_key = API_Keys(api_key='my_api_key', user_id=1)
        self.assertEqual(api_key.data, {'api_key': 'my_api_key', 'user_id': 1})

    def test_create(self):
        api_key = API_Keys(api_key='my_api_key', user_id=1)
        api_key.create()
        # verify that the API key is created in the database
        self.assertEqual(api_key.get_user_id_from_apikey(), 1)

    def test_update(self):
        api_key = API_Keys(api_key='my_api_key2', user_id=1)
        api_key.update()
        # verify that the API key is updated in the database
        self.assertEqual(api_key.get_user_id_from_apikey(), 1)
        api_key_old = API_Keys(api_key='my_api_key', user_id=1)
        self.assertEqual(api_key_old.get_user_id_from_apikey(), None)

    def test_expire(self):
        api_key = API_Keys(api_key='my_api_key', user_id=1)
        api_key.expire()
        self.assertEqual(api_key.get_user_id_from_apikey(), None)

if __name__ == '__main__':
    unittest.main()
