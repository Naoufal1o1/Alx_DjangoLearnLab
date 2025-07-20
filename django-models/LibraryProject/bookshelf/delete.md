# Delete Book

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# ---- DELETE ----
book.delete()

# ---- VERIFY DELETION ----
print(Book.objects.all())  # Output: <QuerySet []>
