from tests.base import BaseTestCase
import unittest
import json

class TestUserVeiwsRoutes(BaseTestCase):
  def test_user_registration(self):
    with self.client:
      response = self.register_user("mercy", "mercy1", "mercy@gmail.com", 256739876542, False)
      data = json.loads(response.data.decode())
      self.assertEqual(response.status_code, 201)
      self.assertEqual(data["message"], "User created successfully")


  def test_user_register_with_wrong_content_type(self):
    with self.client:
      response = self.register_user_with_wrong_content_type("mercy", "mercy1", "mercy@gmail.com", 256739876542, False)
      data = json.loads(response.data.decode())
      self.assertEqual(response.status_code, 400)
      self.assertEqual(data["message"], "Wrong content Type")

  # def test_login_user(self):
  #   with self.client:
  #     response = self.login_user("mercy", "mercy1")
  #     data = json.loads(response.data.decode())
  #     self.assertEqual(response.status_code, 200)
  #     self.assertEqual(data["data"][0]["message"], "Login sucessful")