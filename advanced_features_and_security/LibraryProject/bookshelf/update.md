# Update Book Title

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book = Book.objects.get(id=book.id)
print(book.title)  # Output: Nineteen Eighty-Four
