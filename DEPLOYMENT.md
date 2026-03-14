# Deployment

## Recommended Production Shape

Use the application behind a WSGI server such as Gunicorn or uWSGI and a
reverse proxy such as Nginx or Caddy.

## Environment Variables

Copy `.env.example` and provide production values for:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=0`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DJANGO_SESSION_COOKIE_SECURE=1`
- `DJANGO_CSRF_COOKIE_SECURE=1`
- `DJANGO_SECURE_SSL_REDIRECT=1`

## Database

Local development uses SQLite. For production, switch to a managed database or
another persistent backend and configure `DJANGO_DB_ENGINE` and
`DJANGO_DB_NAME` accordingly.

## Static Files

Run:

```bash
python manage.py collectstatic --noinput
```

and serve the generated `staticfiles/` directory from the reverse proxy or app
server setup.

## Basic Release Checklist

1. Set production environment variables.
2. Apply migrations.
3. Collect static files.
4. Create or verify the admin account.
5. Run `python manage.py check`.
6. Run `python manage.py test`.
