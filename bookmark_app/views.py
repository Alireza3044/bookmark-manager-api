from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookmarkViewSet(ModelViewSet):
    serializer_class = serializers.BookmarkSerializer

    def get_queryset(self):
        return models.Bookmark.objects.filter(
            category_id=self.kwargs.get('category_pk'),
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GlobalBookmarksView(ListAPIView):
    serializer_class = serializers.BookmarkSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["title", "user", "category", "is_favorite"]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return models.Bookmark.objects.filter(user=self.request.user)


class MakeFavoriteView(UpdateAPIView):
    serializer_class = serializers.BookmarkSerializer

    def get_queryset(self):
        return models.Bookmark.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        bookmark = self.get_object()
        bookmark.is_favorite = not bookmark.is_favorite
        bookmark.save(update_fields=["is_favorite"])
        
        serializer = self.get_serializer(bookmark)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SummaryView(APIView):
    def get(self, request):
        categories = models.Category.objects.filter(user=request.user).count()
        bookmarks = models.Bookmark.objects.filter(user=request.user).count()
        favorites = models.Bookmark.objects.filter(user=request.user, is_favorite=True).count()
        data = {
            "n_categories": categories,
            "n_bookmarks": bookmarks,
            "n_favorite_bookmarks": favorites
        }
        return Response(data, status=status.HTTP_200_OK)
