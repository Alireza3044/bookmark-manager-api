from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class AccountTest(APITestCase):
    def setUp(self):
        self.data = {
            "username": "user1",
            "email": "user1@example.com",
            "password": "password",
        }
        self.user = User.objects.create_user(**self.data)
        self.token = Token.objects.create(user=self.user).key

    def test_register(self):
        data2 = {
            "username": "user2",
            "email": "user2@example.com",
            "password": "password",
            "password2": "password",
        }
        response = self.client.post(reverse("register"), data2)
        success_msg = "Registration was successful!"

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["response"], success_msg)
        self.assertEqual(response.json()["username"], data2["username"])

    def test_login(self):
        data = {
            "username": self.data["username"],
            "password": self.data["password"],
        }
        response = self.client.post(reverse("login"), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["token"], self.token)

    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

        response = self.client.post(reverse("logout"))
        self.user.refresh_from_db()

        with self.assertRaises(Token.DoesNotExist):
            self.user.auth_token
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
