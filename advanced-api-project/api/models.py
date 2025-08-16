from django.db import models

# Author model represents a writer who can have many Book instances.
class Author(models.Model):
    # name: stores the full name of the author as a short string.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model represents a published book and references an Author.
class Book(models.Model):
    # title: the book's title.
    title = models.CharField(max_length=255)

    # publication_year: integer year the book was published.
    # We will validate in serializers to avoid future years.
    publication_year = models.IntegerField()

    # author: foreign key linking to Author. This creates a one-to-many
    # relationship (one Author -> many Books). `related_name` allows
    # reverse access from Author instance via `author.books`.
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    isbn = models.CharField(max_length=13, unique=True,default="0000000000000")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

