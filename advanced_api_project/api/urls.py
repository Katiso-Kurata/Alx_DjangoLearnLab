from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register your viewsets with it
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Wire up the API using automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
