# django_blog (Alx_DjangoLearnLab/django_blog)

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
# open http://127.0.0.1:8000/posts/
```
Features: Auth (register/login/logout/profile), Posts CRUD with permissions, Comments, Tags (django-taggit), Search.
