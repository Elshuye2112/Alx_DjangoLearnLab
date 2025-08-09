from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields. Also implements custom validation for
    `publication_year` to ensure it is not in the future.

    The serializer handles creation and update of Book instances by
    delegating to `ModelSerializer`'s default `create` and `update`.
    """

    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year', 'author')
        read_only_fields = ('id',)

    def validate_publication_year(self, value):
        """Field-level validator for publication_year.

        Ensures the year is not greater than the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"publication_year ({value}) cannot be in the future (current year: {current_year})."
            )
        return value


class NestedBookSerializer(serializers.ModelSerializer):
    """
    A slim serializer used when nesting book data inside AuthorSerializer.
    We often exclude `author` to avoid circular nested IDs.
    """

    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year')
        read_only_fields = ('id',)


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author and includes a nested list of the author's books.

    - `books` field uses NestedBookSerializer to serialize related Book objects
      (accessed via the `related_name='books'` on the Book model's FK).
    - `books` is read-only by default here; we only show existing books.
      If you want to allow creating/updating books when creating/updating
      an author, you can implement `create()`/`update()` to accept nested
      writable representations.
    """

    # `many=True` because an author can have multiple books. `read_only=True`
    # prevents writes through this nested field in this example.
    books = NestedBookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')
        read_only_fields = ('id',)