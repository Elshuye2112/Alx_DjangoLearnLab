import os
import django

# Setup Django environment for standalone script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Adjust if your settings module name differs
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # related_name='books'
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in the library '{library_name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

def query_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # related_name='librarian'
        print(f"Librarian for library '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library_name}'")

if __name__ == "__main__":
    # Example usage:
    query_books_by_author("George Orwell")
    query_books_in_library("Central Library")
    query_librarian_for_library("Central Library")
