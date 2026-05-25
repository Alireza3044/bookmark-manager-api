from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from bookmark_app import models


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user1", password="password")
        self.token1 = Token.objects.create(user=self.user1)

        self.user2 = User.objects.create(username="user2", password="password")
        self.token2 = Token.objects.create(user=self.user2)

        self.category1 = models.Category.objects.create(name="Beuties", user=self.user1)
        self.category2 = models.Category.objects.create(name="Freshes", user=self.user1)

        self.client.force_authenticate(user=self.user1, token=self.token1)

    def test_create(self):
        data = {
            "name": "Colors",
            "user": self.user1
        }
        response = self.client.post(reverse("category-list"), data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Category.objects.filter(user=self.user1).count(), 3)
        self.assertEqual(models.Category.objects.get(name="Colors").name, "Colors")

    def test_list(self):
        response = self.client.get(reverse("category-list"))
        data = response.json()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]["name"], "Beuties")
        self.assertEqual(data[1]["name"], "Freshes")

    def test_retrieve(self):
        response = self.client.get(reverse("category-detail", args=[self.category1.pk]))
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.category1.name)
    
    def test_update(self):
        data = {
            "name": "Wonders"
        }
        response = self.client.put(reverse("category-detail", args=[self.category1.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Category.objects.get(name=data["name"]))

    def test_partial_update(self):
        data = {
            "name": "Wonders"
        }
        response = self.client.patch(reverse("category-detail", args=[self.category2.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Category.objects.get(name=data["name"]))
    
    def test_delete(self):
        response = self.client.delete(reverse("category-detail", args=[self.category1.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Category.objects.count(), 1)
