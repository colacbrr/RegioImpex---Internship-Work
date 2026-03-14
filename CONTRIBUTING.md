# Contributing

## Local Workflow

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
```

## Before Opening A Change

Run:

```bash
make check
make test
make lint
```

## Scope

Keep changes focused on:

- operational workflow quality
- maintainable Django code
- public-ready documentation
- secure default configuration
