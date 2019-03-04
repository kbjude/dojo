import json
from unittest import TestCase
from app.database.connection import cursor
from app import app
from app.models.user_model import User

user = User()


class BaseTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()
        user.create_table_users()

    def tearDown(self):
        user.drop_table_users()

    def register_user(self, username, password, email, phone_number,
                      is_admin):
        return self.client.post(
            "api/v1/auth/signup",
            content_type="application/json",
            data=json.dumps(dict(username=username, password=password,
                            email=email, phone_number=phone_number,
                            is_admin=is_admin)))

    def login_user(self, username, password):        
        return self.client.post(
            "api/v1/auth/login",
            content_type="application/json",
            data=json.dumps(dict(username=username, password=password)))
