from django.contrib.auth.models import User
from rest_framework import serializers
from bookmark_app import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"
        read_only_fields = ["user"]


class BookmarkSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=models.Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = models.Bookmark
        fields = "__all__"
        read_only_fields = ["user"]
