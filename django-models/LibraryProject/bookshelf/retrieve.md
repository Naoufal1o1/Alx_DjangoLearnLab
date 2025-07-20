# Retrieve Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title)  # Output: 1984
print(book.author)  # Output: George Orwell
print(book.publication_year)  # Output: 1949
