from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Author model to store author information.
    """
    name = models.CharField(max_length=100)

    #
class Book(models.Model):
    """
    Book model to store book information.
    """
    title = models.CharField(max_length=200)  # Field to store the book's title
    publication_year = models.IntegerField()  # Field for the year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    