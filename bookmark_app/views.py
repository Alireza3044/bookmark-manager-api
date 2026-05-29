from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
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


class MakeFavoriteView(CreateAPIView):
    queryset = models.Bookmark.objects.all()
    serializer_class = serializers.BookmarkSerializer

    def create(self, request):
        pass


class SummaryView(APIView):
    def get(self, request):
        pass
