from django.db import models

class Author(models.Model):
    # Simple Author model with a name field.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Book model with title, publication_year and FK to Author.
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
