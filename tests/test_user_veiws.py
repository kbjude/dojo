from app.models.user_model import User
from tests.base import BaseTestCase
import unittest
import json

class TestUserVeiwsRoutes(BaseTestCase):
  def test_user_registration(self):
    with self.client:
      response = self.register_user("benny", "benny1", "benny@gmail.com", 245704567893, False)
      data = json.loads(response.data.decode())
      self.assertEqual(response.status_code, 201)
      # self.assertEqual(data["data"][0]["message"] == "User created successfully")

  def test_login_user(self):
    with self.client:
      response = self.login_user("jane", "james2")
      data = json.loads(response.data.decode())
      self.assertEqual(response.status_code, 200)
      # self.assertEqual(data["data"][0]["message"] == "Login sucessful")