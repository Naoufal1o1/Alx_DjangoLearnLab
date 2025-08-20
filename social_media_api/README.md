# Social Media API (Django + DRF)

A fully functional Social Media API implementing:
- Custom User + Token auth (register, login, profile)
- Posts & Comments CRUD
- Follow/Unfollow + Feed
- Likes
- Notifications (follow, like, comment)
- Filtering, search, ordering, pagination

## Quickstart

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Initial setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Run
python manage.py runserver
```

## API Overview

Auth base: `/api/accounts/`
- `POST /register/` -> { token, user }
- `POST /login/` -> { token, user_id }
- `GET/PATCH /profile/`

Follow:
- `POST /follow/<user_id>/`
- `POST /unfollow/<user_id>/`

Posts base: `/api/`
- `GET/POST /posts/`
- `GET/PATCH/DELETE /posts/{id}/`
- `POST /posts/{id}/like/`
- `POST /posts/{id}/unlike/`
- `GET /comments/` CRUD
- `GET /feed/`

Notifications base: `/api/`
- `GET /notifications/`
- `POST /notifications/mark-read/`

## Deployment notes
Set environment variables in production:
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=0`
- `DJANGO_ALLOWED_HOSTS=your.domain,localhost`

Use Postgres in prod and configure `DATABASE_URL` or update `DATABASES` accordingly.
Run `python manage.py collectstatic` and serve static with a web server or CDN.
