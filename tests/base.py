import json
from unittest import TestCase
from app import DatabaseConnection
from app import app
from app.models.user_model import User



class BaseTestCase(TestCase):
  def setUp(self):
    cursor = DatabaseConnection.cursor()
    self.client = app.test_client()
   


  def tearDown(self):
    pass
    # User.drop_tables()
    
  
  def register_user(self, username, password, email, phone_number, is_admin):
    return self.client.post(
      "auth/signup",
      content_type ="application/json",
      data = json.dumps(dict(username=username, password=password, email=email, phone_number=phone_number, is_admin=is_admin)))

  # def login_user(self, username, password):
  #   return self.client.post(
  #     "auth/login",
  #     content_type = "application/json",
  #     data = json.dumps(dict(username=username, password=password)))

  def register_user_with_wrong_content_type(self, username, password, email, phone_number, is_admin):
    return self.client.post(
      "auth/signup",
      content_type ="application/text",
      data = json.dumps(dict(username=username, password=password, email=email, phone_number=phone_number, is_admin=is_admin)))
