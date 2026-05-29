from django.contrib.auth.models import User
from rest_framework import serializers
from bookmark_app import models


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Category
        fields = "__all__"


class BookmarkSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=models.Category.objects.all(),
        slug_field="name"
    )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Bookmark
        fields = "__all__"
