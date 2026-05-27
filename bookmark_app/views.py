from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from bookmark_app import models, serializers


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

    def get_queryset(self):
        return models.Bookmark.objects.filter(user=self.request.user)


class MakeFavoriteView(APIView):
    def post(self, request, pk):
        bookmark = models.Bookmark.objects.get(pk=pk, user=request.user)
        bookmark.is_favorite = not bookmark.is_favorite
        bookmark.save(update_fields=["is_favorite"])
        
        return Response(bookmark, status=status.HTTP_200_OK)


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
