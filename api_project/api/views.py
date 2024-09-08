from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

#["generics.ListAPIView"]
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # QuerySet for all Book instances
    serializer_class = BookSerializer  # Serializer class for Book
    permission_classes = [IsAuthenticated]
#space
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]  # Any authenticated user can list or retrieve
        else:
            permission_classes = [IsAdminUser]  # Only admin users can create, update, or delete
        return [permission() for permission in permission_classes]
