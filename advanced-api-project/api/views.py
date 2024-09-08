from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
["from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]
["from django_filters import rest_framework"]
# List View for retrieving all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access for unauthenticated users

# Detail View for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Example of adding custom logic before saving
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update

    def perform_update(self, serializer):
        # Custom update logic if needed
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

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

