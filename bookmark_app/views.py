from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from bookmark_app import models, serializers


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class BookmarkViewSet(ModelViewSet):
    queryset = models.Bookmark.objects.all()
    serializer_class = serializers.BookmarkSerializer


class GlobalBookmarksView(ListAPIView):
    queryset = models.Bookmark.objects.all()
    serializer_class = serializers.BookmarkSerializer


class MakeFavoriteView(APIView):
    def post(self, request, pk):
        bookmark = models.Bookmark.objects.get(pk=pk)
        bookmark.is_favorite = not bookmark.is_favorite
        bookmark.save(update_fields=["is_favorite"])
        
        return Response(bookmark, status=status.HTTP_200_OK)


class SummaryView(APIView):
    def get(self, request):
        categories = models.Category.objects.count()
        bookmarks = models.Bookmark.objects.count()
        favorites = models.Bookmark.objects.filter(is_favorite=True).count()
        data = {
            "categories": categories,
            "bookmarks": bookmarks,
            "favorite_bookmarks": favorites
        }
        return Response(data, status=status.HTTP_200_OK)
