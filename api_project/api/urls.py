from django.urls import path, include
from .views import BookListAPIView
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Initialize the router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path("api/books/", BookListAPIView.as_view(), name="book_list_create"),
    path('', include(router.urls)),
]

