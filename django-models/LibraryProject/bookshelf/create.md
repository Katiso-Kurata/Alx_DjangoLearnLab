# CRUD Operations for Book Model

## Create Operation
```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
