# Advanced API Project (ready-to-run)

This is a minimal Django project prepared to satisfy the **Advanced API Development with Django REST Framework**
project tasks. It includes:

- `Author` and `Book` models.
- Custom serializers with nested relationships and validation.
- Generic views for CRUD.
- Filtering, searching and ordering for the book list.
- Unit tests in `api/test_views.py`.

How to run:

1. Create a virtual environment and install dependencies:
   ```
   python -m venv .venv
   source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

2. Run migrations and start server:
   ```
   python manage.py migrate
   python manage.py runserver
   ```

3. API endpoints:
   - List/create books:    `GET/POST  /api/books/`
   - Retrieve/update/delete book: `GET/PUT/PATCH/DELETE /api/books/<pk>/`
   - Authors list: `GET /api/authors/`

Notes:
- Default DB is SQLite (db.sqlite3).
- For testing, run `python manage.py test api`.
