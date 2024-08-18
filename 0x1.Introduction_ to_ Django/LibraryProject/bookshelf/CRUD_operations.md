# CRUD Operations for Book Model

## Create Operation
```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Retrieve and display the book instance
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# Update the title of the book instance
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Delete the book instance
book.delete()

# Confirm deletion by trying to retrieve all books
books = Book.objects.all()
print(list(books))

