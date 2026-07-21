# regio-updated

`regio-updated` is a cleaned Django support-desk application for managing
bypass tickets, operator accounts, and internal workflow records in a
transport-support setting.

This public-ready version removes unrelated local files and reorganizes the
project into a normal Django repository that is easier to understand, run, and
extend.

Portfolio case study: https://cristiancolacel.com/projects/regioimpex-internal-support-desk

## Features

- authenticated dashboard for operators and administrators
- bypass creation flow with validation for carrier, driver, and tanker
- searchable bypass records view with CSV export
- admin-only user management
- Django admin for reference data and operational review
- responsive templates with a cleaner internal web UI

## Stack

- Python
- Django
- SQLite for local development
- HTML templates, custom CSS, and small progressive JavaScript

## Architecture

- `config/` Django project configuration
- `pages/` dashboard and shared error pages
- `app/` bypass models, forms, views, admin, and tests
- `users/` authentication, profile, and operator management
- `templates/` server-rendered UI
- `static/` shared styles and scripts

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Development Commands

```bash
make check
make test
make lint
make run
```

## Main Routes

- `/` dashboard
- `/bypass/` create a bypass record
- `/bypass/records/` search and review bypass history
- `/bypass/export/` export records as CSV
- `/login/` login
- `/profile/` account profile
- `/users/` admin-only user list
- `/admin/` Django admin

## Production Notes

- configure settings from environment variables
- use a production database instead of local SQLite
- set secure cookie and SSL settings through env vars
- run `python manage.py collectstatic`
- place the app behind a real WSGI server and reverse proxy

More detail is in [DEPLOYMENT.md](DEPLOYMENT.md).

## Security And Privacy

- no sample production credentials are stored in the repo
- runtime database files and local environments are ignored
- user-management views are restricted to administrators
- the public repo is intentionally documentation-first and excludes personal
  local artifacts from the original private workspace

## Repository Cleanup Applied

- removed unrelated personal directories and notes
- removed committed virtual environments and local database files
- removed cache files and backup artifacts
- simplified routing, forms, tests, and templates
- added CI, linting, deployment notes, and public-facing documentation
