from tests.base import BaseTestCase
import unittest
import json


class TestUserVeiwsRoutes(BaseTestCase):
    def test_user_registration(self):
        with self.client:
            response = self.register_user(
              "mercy",
              "mercy1",
              "mercy@gmail.com",
              "256739876542",
              False)

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        with self.client:
            self.register_user(
              "mercy",
              "mercy1",
              "mercy@gmail.com",
              "256739876542",
              False)

            response = self.login_user(
              "mercy",
              "mercy1")

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
