from relationship_app.models import Book, Author

# Replace 'author_name' with the actual name of the author you want to query
author_name = "John Doe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

print("Books by", author_name, ":", [book.title for book in books_by_author])

from relationship_app.models import Library, Librarian

# Replace 'library_name' with the actual name of the library you want to query
library_name = "Central Library"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)

print("Librarian for", library_name, ":", librarian.name)

# Assuming 'library_name' is already defined above
books_in_library = library.books.all()

print("Books in", library_name, ":", [book.title for book in books_in_library])
