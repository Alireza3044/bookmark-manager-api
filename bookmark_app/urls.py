from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter
from bookmark_app import views

category_router = SimpleRouter()
category_router.register("categories", views.CategoryViewSet, "category")

bookmark_router = NestedSimpleRouter(category_router, "categories", lookup="category")
bookmark_router.register("bookmarks", views.BookmarkViewSet, "category-bookmark")

urlpatterns = [
    path("", include(category_router.urls)),
    path("", include(bookmark_router.urls)),
    path("bookmarks/", views.GlobalBookmarksView.as_view(), name="global-bookmarks"),
    path("favorite/<int:pk>/", views.MakeFavoriteView.as_view(), name="favorite"),
    path("summary/", views.SummaryView.as_view(), name="summary"),
]
