from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

     # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Configure filtering
    filterset_fields = ['title', 'author', 'publication_year']
    ...
    # Add searchable fields
    search_fields = ['title', 'author']

    ...
    # Allow ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']

    """
    A viewset for viewing and editing books.
    
    Supports filtering by title, author, and publication year.
    Supports searching by title and author.
    Supports ordering by title and publication year.
    """
    ...

