import json
from unittest import TestCase
from app import DatabaseConnection
from app import app

class BaseTestCase(TestCase):
  def setUp(self):
    cursor = DatabaseConnection.cursor()
    self.client = app.test_client()

  def tearDown(self):
    pass

  def register_user(self, username, password, email, phone_number, is_admin):
    return self.client.post(
      "auth/signup",
      content_type ="application/json",
      data = json.dumps(dict(username=username, password=password, email=email, phone_number=phone_number, is_admin=is_admin)))

  def login_user(self, username, password):
    return self.client.post(
      "auth/login",
      content_type = "application/json",
      data = json.dumps(dict(username=username, password=password))

    )

    