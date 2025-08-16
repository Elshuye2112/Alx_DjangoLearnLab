from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields, including custom validations.
    """

    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year', 'isbn', 'author')
        read_only_fields = ('id',)

    def validate_publication_year(self, value):
        """
        Ensures the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"publication_year ({value}) cannot be in the future (current year: {current_year})."
            )
        return value

    def validate_isbn(self, value):
        """
        Ensures ISBN is numeric.
        """
        if not value.isdigit():
            raise serializers.ValidationError("ISBN must be numeric.")
        return value


class NestedBookSerializer(serializers.ModelSerializer):
    """
    Slim version of BookSerializer for nested display in AuthorSerializer.
    """

    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year')
        read_only_fields = ('id',)


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author and includes nested books (read-only).
    """
    books = NestedBookSerializer(many=True, read_only=True)  # related_name='books' in Book model

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')
        read_only_fields = ('id',)
