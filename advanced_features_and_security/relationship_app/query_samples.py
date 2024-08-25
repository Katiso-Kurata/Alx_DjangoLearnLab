from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

if __name__ == "__main__":
    # Example usage:
    author_name = "Author Name"
    library_name = "Library Name"

    print("Books by author:", query_books_by_author(author_name))
    print("Books in library:", list_books_in_library(library_name))
    print("Librarian for library:", get_librarian_for_library(library_name))
