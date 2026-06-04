from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from . import models


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user1", password="password")
        self.user2 = User.objects.create(username="user2", password="password")

        self.category1 = models.Category.objects.create(name="Beauties", user=self.user1)
        self.category2 = models.Category.objects.create(name="Freshes", user=self.user1)
        self.category_user2 = models.Category.objects.create(name="Flowers", user=self.user2)

    def test_user_cannot_access_other_users_category(self):
        self.client.force_authenticate(user=self.user1)
        
        response = self.client.get(reverse("category-detail", args=[self.category_user2.pk]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create(self):
        self.client.force_authenticate(user=self.user1)

        data = {
            "name": "Colors",
            "user": self.user1
        }
        response = self.client.post(reverse("category-list"), data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Category.objects.filter(user=self.user1).count(), 3)
        self.assertTrue(models.Category.objects.get(name=data["name"]))

    def test_list(self):
        self.client.force_authenticate(user=self.user1)

        response = self.client.get(reverse("category-list"))
        data = response.json()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]["name"], "Beauties")
        self.assertEqual(data[1]["name"], "Freshes")

    def test_retrieve(self):
        self.client.force_authenticate(user=self.user1)

        response = self.client.get(reverse("category-detail", args=[self.category1.pk]))
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.category1.name)
    
    def test_update(self):
        self.client.force_authenticate(user=self.user1)

        data = {
            "name": "Wonders"
        }
        response = self.client.put(reverse("category-detail", args=[self.category1.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Category.objects.get(name=data["name"]))

    def test_partial_update(self):
        self.client.force_authenticate(user=self.user1)

        data = {
            "name": "Wonders"
        }
        response = self.client.patch(reverse("category-detail", args=[self.category1.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Category.objects.get(name=data["name"]))
    
    def test_delete(self):
        self.client.force_authenticate(user=self.user1)

        response = self.client.delete(reverse("category-detail", args=[self.category1.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Category.objects.count(), 2)


class BookmarkTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", password="password")
        self.user2 = User.objects.create(username="user2", password="password")
        self.category = models.Category.objects.create(name="Interests", user=self.user)
        self.category_user2 = models.Category.objects.create(name="Positives", user=self.user2)

        data = {
            "title": "Libre Text",
            "url": "https://libretexts.org",
            "user": self.user,
            "category": self.category,
            "description": "Libre texts for free."
        }
        data2 = {
            "title": "Google Colab",
            "url": "https://colaboratory.com",
            "user": self.user,
            "category": self.category,
            "description": "Google Colaboratory."
        }
        data3 = {
            "title": "Google Colab",
            "url": "https://colaboratory.com",
            "user": self.user2,
            "category": self.category_user2,
            "description": "Google Colaboratory."
        }
        self.bookmark = models.Bookmark.objects.create(**data)
        self.bookmark2 = models.Bookmark.objects.create(**data2)
        self.bookmark_user2 = models.Bookmark.objects.create(**data3)

    def test_user_cannot_access_other_users_bookmark(self):
        self.client.force_authenticate(user=self.user)
        
        response = self.client.get(reverse("category-bookmark-detail", args=[self.category_user2.pk ,self.bookmark_user2.pk]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "Scholar",
            "url": "https://scholar.google.com",
            "user": self.user,
            "category": self.category.pk,
            "description": "Google Scholar for technical literature."
        }
        response = self.client.post(reverse("category-bookmark-list", args=[self.category.pk]), data)

        filtered_data = models.Bookmark.objects.filter(user=self.user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(filtered_data.count(), 3)
        self.assertTrue(filtered_data.get(title=data["title"]))

    def test_list(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse("category-bookmark-list", args=[self.category.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse("category-bookmark-detail", args=[self.category.pk, self.bookmark.pk]))
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["title"], self.bookmark.title)
    
    def test_update(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "Librrrrrre Text",
            "url": "https://libretexts.org",
            "user": self.user,
            "category": self.category.pk,
            "description": "Libre texxxxxxts for free."
        }
        response = self.client.put(reverse("category-bookmark-detail", args=[self.category.pk, self.bookmark.pk]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Bookmark.objects.get(title=data["title"], description=data["description"]))

    def test_partial_update(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "Librrrrrre Texxxxxt"
        }
        response = self.client.patch(reverse("category-bookmark-detail", args=[self.category.pk, self.bookmark.pk]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Bookmark.objects.get(title=data["title"]))

    def test_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse("category-bookmark-detail", args=[self.category.pk, self.bookmark.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Bookmark.objects.filter(user=self.user).count(), 1)


class GlobalBookmarksTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", password="password")
        self.user2 = User.objects.create(username="user2", password="password")
        self.category = models.Category.objects.create(name="web", user=self.user)
        self.category_user2 = models.Category.objects.create(name="video", user=self.user2)

        data = {
            "title": "Libre Text",
            "url": "https://libretexts.org",
            "user": self.user,
            "category": self.category,
            "description": "Libre texts for free."
        }
        data2 = {
            "title": "Google Colab",
            "url": "https://colaboratory.com",
            "user": self.user,
            "category": self.category,
            "description": "Google Colaboratory."
        }
        self.data3 = {
            "title": "Prime",
            "url": "https://primevideos.com",
            "user": self.user2,
            "category": self.category_user2,
            "description": "Video streaming platform."
        }
        self.bookmark = models.Bookmark.objects.create(**data)
        self.bookmark2 = models.Bookmark.objects.create(**data2)
        self.bookmark3 = models.Bookmark.objects.create(**self.data3)

    def test_user_cannot_access_other_users_global_bookmarks(self):
        self.client.force_authenticate(user=self.user)
        
        response = self.client.get(reverse("global-bookmarks"))
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(self.data3, data)

    def test_list(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse("global-bookmarks"))
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[1]["title"], "Google Colab")
        self.assertEqual(len(data), 2)

class MakeFavoriteTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", password="password")
        self.user2 = User.objects.create(username="user2", password="password")
        self.category = models.Category.objects.create(name="Interests", user=self.user)
        self.category_user2 = models.Category.objects.create(name="Leaves", user=self.user2)

        data = {
            "title": "Libre Text",
            "url": "https://libretexts.org",
            "user": self.user,
            "category": self.category,
            "description": "Libre texts for free."
        }
        data2 = {
            "title": "Libre Text",
            "url": "https://libretexts.org",
            "user": self.user2,
            "category": self.category_user2,
            "description": "Libre texts for free."
        }
        self.bookmark = models.Bookmark.objects.create(**data)
        self.bookmark2 = models.Bookmark.objects.create(**data2)


    def test_user_cannot_toggle_favorite_bookmark_of_other_users(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.put(reverse("favorite", args=[self.bookmark2.pk]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_favorite(self):
        self.client.force_authenticate(user=self.user)
        # Initial state
        self.assertFalse(self.bookmark.is_favorite)

        # First toggle
        response = self.client.put(reverse("favorite", args=[self.bookmark.pk]))
        data = response.json()
        self.bookmark.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(data["is_favorite"])
        
        # Second toggle
        response = self.client.put(reverse("favorite", args=[self.bookmark.pk]))
        data = response.json()
        self.bookmark.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(data["is_favorite"])


class SummaryTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", password="password")
        self.category = models.Category.objects.create(name="Interests", user=self.user)
        self.category = models.Category.objects.create(name="Beauties", user=self.user)
        self.category = models.Category.objects.create(name="Colors", user=self.user)

        data1 = {
            "title": "Libre Text",
            "url": "https://libretexts.org",
            "user": self.user,
            "category": self.category,
            "description": "Libre texts for free.",
            "is_favorite": True
        }
        data2 = {
            "title": "Libre Text",
            "url": "https://libretexts.org",
            "user": self.user,
            "category": self.category,
            "description": "Libre texts for free."
        }
        self.bookmark1 = models.Bookmark.objects.create(**data1)
        self.bookmark2 = models.Bookmark.objects.create(**data2)

        self.client.force_authenticate(user=self.user)

    def test_get_summary(self):
        response = self.client.get(reverse("summary"))
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["n_categories"], 3)
        self.assertEqual(data["n_bookmarks"], 2)
        self.assertEqual(data["n_favorite_bookmarks"], 1)
