from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITests(APITestCase):
    def setUp(self):
        # Set up a user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Set up Author and Book instances for testing
        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(title='Book One', publication_year=2023, author=self.author)
        
        # URLs for the API endpoints
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})


# Test Create Operation
def test_create_book(self):
    self.client.login(username='testuser', password='testpassword')  # Log in the user
    data = {
        'title': 'Book Two',
        'publication_year': 2024,
        'author': self.author.id
    }
    response = self.client.post(self.book_list_url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 2)
    self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Book Two')

# Test Read Operation
def test_get_books(self):
    response = self.client.get(self.book_list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], 'Book One')

# Test Update Operation
def test_update_book(self):
    self.client.login(username='testuser', password='testpassword')  # Log in the user
    data = {'title': 'Updated Book One'}
    response = self.client.patch(self.book_detail_url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book.refresh_from_db()
    self.assertEqual(self.book.title, 'Updated Book One')

# Test Delete Operation
def test_delete_book(self):
    self.client.login(username='testuser', password='testpassword')  # Log in the user
    response = self.client.delete(self.book_detail_url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 0)



# Test Filtering by Title
def test_filter_books_by_title(self):
    response = self.client.get(self.book_list_url, {'title': 'Book One'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], 'Book One')

# Test Searching by Title
def test_search_books(self):
    response = self.client.get(self.book_list_url, {'search': 'Book'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

# Test Ordering by Publication Year
def test_order_books_by_publication_year(self):
    Book.objects.create(title='Book Three', publication_year=2022, author=self.author)
    response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['publication_year'], 2022)


# Test Create Operation without Authentication
def test_create_book_without_authentication(self):
    data = {
        'title': 'Book Three',
        'publication_year': 2025,
        'author': self.author.id
    }
    response = self.client.post(self.book_list_url, data)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# Test List View Permission for Unauthenticated User
def test_list_books_without_authentication(self):
    response = self.client.get(self.book_list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookAPITests(APITestCase):
    """
    Tests for the Book API endpoints:
    - CRUD operations: Create, Read, Update, Delete
    - Advanced queries: Filtering, Searching, Ordering
    - Permissions: Ensure proper access control
    """
