# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 6.0+ starter project using **Python 3.13** and **uv** as the package manager. The project is a template for learning and building Django applications with best practices.

## Environment & Dependencies

- **Package Manager**: `uv` (replaces pip/pipenv)
- **Python Version**: 3.13 (specified in `.python-version`)
- **Key Dependencies**: Django 6.0.2+
- **Virtual Environment**: `.venv/` (created automatically by `uv`)

## Setup & Common Commands

### Initial Setup
```bash
# Sync dependencies from pyproject.toml and generate uv.lock
uv sync

# Run the main module
uv run python main.py
```

### Django Project & App Management
```bash
# Create a new Django project (replaces manage.py startproject)
uv run django-admin startproject <project_name>

# Create a new app within the project
uv run python manage.py startapp <app_name>

# Run migrations
uv run python manage.py migrate

# Create a superuser
uv run python manage.py createsuperuser

# Run the development server (with debugger support via django-extensions)
uv run python manage.py runserver_plus

# Or standard development server
uv run python manage.py runserver
```

### Code Quality & Formatting (Ruff)
```bash
# Check for linting issues
uv run ruff check .

# Auto-fix issues where possible
uv run ruff check --fix .

# Format code (matches Black style)
uv run ruff format .

# Check and format together
uv run ruff check --fix . && uv run ruff format .
```

### Enhanced Django Shell
```bash
# Use shell_plus for an enhanced shell with auto-imported models and apps
uv run python manage.py shell_plus

# Within the shell, all models and common Django utilities are pre-imported
# Example: User.objects.all() works immediately without importing User
```

### Running Tests
```bash
# Run all tests
uv run python manage.py test

# Run tests for a specific app
uv run python manage.py test <app_name>

# Run a specific test class or method
uv run python manage.py test <app_name>.tests.<test_module>.<TestClass>.<test_method>
```

### Shell & Debugging
```bash
# Start Django shell (interactive Python with Django context)
uv run python manage.py shell

# Run a Python script with Django environment
uv run python manage.py shell < script.py
```

### Recommended Alias (Add to .zshrc)
```bash
alias django='uv run python manage.py'
```
This allows simplified commands like `django runserver` or `django migrate`.

## Architecture & Project Structure

This is a starter template. When you create a Django project and apps, the typical structure becomes:

```
django-startup/
├── <project_name>/           # Main project directory (created by startproject)
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing for project
│   ├── asgi.py               # ASGI application
│   └── wsgi.py               # WSGI application
├── <app_name>/               # Django apps (created by startapp)
│   ├── migrations/           # Database migrations
│   ├── models.py             # ORM models
│   ├── views.py              # View handlers
│   ├── urls.py               # App-specific URL routing
│   ├── tests.py              # App tests
│   └── admin.py              # Django admin configuration
├── manage.py                 # Django management script (generated)
├── pyproject.toml            # Project dependencies
└── main.py                   # Optional: Entry point for scripts
```

## Development Practices

Based on this project's best practices:

1. **Use Class-Based Views (CBV)**: CBVs encapsulate boilerplate and are easier to test and extend compared to function-based views.

2. **Type Annotation**: All Python code should be type annotated for better IDE support, error detection, and code clarity.

3. **Testing**: Write tests for all models, views, and business logic. Use Django's test framework with `uv run python manage.py test`.

4. **Models Design**: Each Django app typically represents a distinct domain model or set of related dataclasses. Keep models focused and well-organized.

5. **Object-Oriented Design**: All code should be organized around classes. Avoid standalone functions except for utilities and decorators.

6. **Dependency Injection**: Use constructor injection to pass dependencies into classes. This promotes loose coupling and testability.

7. **Abstract Base Classes**: Make heavy use of abstract base classes and interfaces to define contracts and enforce consistent behavior across implementations.

8. **Method Length**: Aim for methods and functions to be no longer than 6 lines. This encourages single responsibility and clarity. Exceptions are allowed when necessary, but the intent is to keep methods concise.

9. **File Organization**: Store each class in its own dedicated file. This keeps the codebase organized and makes navigation easier.

## Environment Variables

- `.env` file is ignored by git (listed in `.gitignore`)
- Store sensitive configuration (API keys, database URLs, secret keys) in `.env`
- Load environment variables in Django settings using `python-dotenv` or Django's built-in support

**Important**: Never commit `.env` files containing credentials.

## Package Management

### Adding Dependencies
```bash
# Add a new package
uv add <package_name>

# Add a development-only package
uv add --dev <package_name>
```

### Lock File
- `uv.lock` is committed to the repository (tracked in git)
- It ensures reproducible builds across environments
- Regenerate with `uv sync` when dependencies change

## Database & Migrations

Django uses migrations to manage database schema changes:

```bash
# Create migration files for model changes
uv run python manage.py makemigrations

# Apply pending migrations
uv run python manage.py migrate

# Check migration status
uv run python manage.py showmigrations

# Revert a migration
uv run python manage.py migrate <app_name> <migration_number>
```

## Django Admin

- After creating a superuser, access the admin at `http://localhost:8000/admin/`
- Register models in `admin.py` to manage data through the web interface
- Use `admin.site.register(ModelName)` to expose models in the admin panel

## Notes for Development

- The project uses Django's standard MVT (Model-View-Template) architecture
- When adding new apps, ensure to add them to `INSTALLED_APPS` in `settings.py`
- Static files and media files should be configured in settings based on deployment environment
- Consider using Django REST Framework (DRF) for API endpoints if building an API-based project
