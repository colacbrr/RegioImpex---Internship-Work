.PHONY: help install migrate run check test lint format

help:
	@printf "Available targets:\n"
	@printf "  install  Install Python dependencies\n"
	@printf "  migrate  Apply database migrations\n"
	@printf "  run      Start the development server\n"
	@printf "  check    Run Django system checks\n"
	@printf "  test     Run the test suite\n"
	@printf "  lint     Run Ruff\n"
	@printf "  format   Format Python files with Ruff\n"

install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

run:
	python manage.py runserver

check:
	python manage.py check

test:
	python manage.py test

lint:
	ruff check .

format:
	ruff format .
