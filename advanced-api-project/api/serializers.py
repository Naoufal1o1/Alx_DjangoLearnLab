from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        # Ensure publication_year is not in the future.
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('publication_year cannot be in the future.')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to include the author's books.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
