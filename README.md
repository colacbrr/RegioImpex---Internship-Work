# regio-updated

Cleaned and documented Django web application for managing bypass tickets and
operator/admin workflows in a transport-support context.

This public version focuses on the actual web project and removes unrelated
personal files, committed virtual environments, runtime database files, and
other non-project artifacts.

## Project Overview

The application provides:

- authentication for operators and administrators
- a bypass ticket form for recording operational cases
- a dashboard for navigating the workflow
- profile and user-management pages
- Django admin for managing reference data

## Stack

- Python
- Django
- SQLite for local development
- HTML templates
- custom CSS and JavaScript

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Main Routes

- `/` dashboard
- `/bypass/` bypass form
- `/login/` login
- `/logout/` logout
- `/profile/` profile
- `/users/` user list
- `/users/add/` add user
- `/admin/` Django admin

## Public Cleanup Applied

- removed unrelated personal notes and files
- removed committed `venv/`
- removed committed `db.sqlite3`
- removed Python cache files and backup files
- simplified project structure to a normal Django repo layout
- improved views, forms, navigation, and documentation
