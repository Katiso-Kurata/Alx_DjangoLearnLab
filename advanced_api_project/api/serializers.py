from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for the publication_year field
    def validate_publication_year(self, value):
        """
        Ensure that the publication year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes nested serialization of related Book objects.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer to display related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include author's name and related books
