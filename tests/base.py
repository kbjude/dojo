import json
from unittest import TestCase
from app.database.connection import cursor
from app import app
from app.models.user_model import User

user = User()


class BaseTestCase(TestCase):
  def setUp(self):
    self.client = app.test_client()
   

    def tearDown(self):
        user.drop_table_users()

    def register_user(self, username, password, email, phone_number, is_admin):
        return self.client.post(
            "auth/signup",
            content_type="application/json",
            data=json.dumps(dict(username=username, password=password,
                                 email=email, phone_number=phone_number,
                                 is_admin=is_admin)))

    def register_user_with_wrong_content_type(self, username, password, email,
                                              phone_number, is_admin):
        return self.client.post(
            "auth/signup",
            content_type="application/text",
            data=json.dumps(dict(username=username, password=password,
                                 email=email, phone_number=phone_number,
                                 is_admin=is_admin)))
