# Django Startup 🚀

A Django 6.0+ starter project template for learning best practices and rapid development.

---

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Project Setup](#project-setup)
- [Available Commands](#available-commands)
- [Dependencies Overview](#dependencies-overview)
- [Best Practices](#best-practices)
- [Contributing](#contributing)

---

## Quick Start

Get up and running in 3 steps:

```bash
# 1. Clone the repository
git clone https://github.com/YourUsername/YourProject.git
cd YourProject

# 2. Install dependencies
uv sync

# 3. Start developing!
django startproject <project_name>
django startapp <app_name>
```

---

## Project Setup

### Prerequisites

Install the `uv` package manager (faster and simpler than pip):

```bash
brew install uv
```

### Initial Configuration

#### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/YourProject.git
cd YourProject
```

#### 2. Sync Dependencies

This installs all packages from `pyproject.toml`:

```bash
uv sync
```

#### 3. (Recommended) Add Shell Alias

Add this to your `.zshrc` or `.bashrc` to simplify Django commands:

```bash
alias django='uv run python manage.py'
```

Then you can use:
- `django migrate` instead of `uv run python manage.py migrate`
- `django runserver` instead of `uv run python manage.py runserver`
- etc.

### Creating Your First Project

Once setup is complete, create a new Django project:

```bash
django startproject <project_name>
```

Then create your first app within the project:

```bash
django startapp <app_name>
```

> **Note:** Apps represent distinct features or domains. For example: `users`, `blog`, `products`, etc.

---

## Available Commands

### Common Django Operations

```bash
# Create and apply database migrations
django makemigrations
django migrate

# Create a superuser for admin access
django createsuperuser

# Run development server with debugger
django runserver_plus

# Or standard development server
django runserver

# Enhanced Django shell (auto-imports your models)
django shell_plus
```

### Code Quality & Formatting

Keep your code clean with Ruff:

```bash
# Check for issues
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .

# Format code
uv run ruff format .

# Do both at once
uv run ruff check --fix . && uv run ruff format .
```

### Running Tests

```bash
# Run all tests
django test

# Run tests for a specific app
django test <app_name>

# Run a specific test
django test <app_name>.tests.<module>.<TestClass>.<method>
```

---

## Dependencies Overview

### Core & Utilities

- **django-environ** - Load environment variables from `.env` files securely
  - Usage: Store sensitive config (API keys, database URLs) in `.env`

- **django-extensions** - Extra management commands for convenience
  - `shell_plus`: Enhanced shell with auto-imported models
  - `runserver_plus`: Development server with debugger

### UI & Frontend

- **django-tailwind** - Integrate Tailwind CSS for styling
  - Setup: `django tailwind install`
  - Development: `django tailwind start` (watch for CSS changes)

- **django-unfold** - Modern Django admin interface
  - Replaces the default admin automatically
  - Better UX for managing your data

### Code Quality

- **ruff** - Fast Python linter and formatter
  - Check issues: `ruff check .`
  - Auto-fix: `ruff check --fix .`
  - Format: `ruff format .`

### Development Tools (Dev Dependencies)

- **django-debug-toolbar** - Debug your Django app in the browser
  - Shows SQL queries, templates, timing, and more
  - Auto-enabled when `DEBUG=True`

- **django-stubs** - Type hints for Django
  - Better IDE autocomplete
  - Static type checking support

---

## Best Practices

Follow these conventions to write better Django code:

### 1. **Use Class-Based Views**

Prefer class-based views (CBVs) over function-based views. They're more organized and easier to test.

```python
# ✅ Good: Class-based view
from django.views import View

class ProductListView(View):
    def get(self, request):
        # Handle GET request
        pass
```

### 2. **Type Annotate Your Code**

Add type hints for better IDE support and fewer bugs:

```python
# ✅ Good: Typed function
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

### 3. **Write Tests**

Test your models, views, and business logic:

```bash
django test <app_name>
```

### 4. **Protect Sensitive Information**

- Store API keys, database URLs, and secrets in `.env` (never commit this!)
- Use `django-environ` to load them safely
- See `.gitignore` for files that are protected

---

## Contributing

### Making a Pull Request

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/description-of-changes
   ```

2. **Make your changes**:
   - Write code
   - Run tests: `django test`
   - Check formatting: `ruff check --fix .`

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Clear description of what you changed"
   ```

4. **Push to GitHub**:
   ```bash
   git push origin feature/description-of-changes
   ```

5. **Open a Pull Request**:
   - Go to the repository on GitHub
   - Click "Compare & pull request"
   - Describe your changes
   - Click "Create pull request"

6. **Wait for review** - Your code will be reviewed and merged once approved!

---

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [uv Package Manager](https://github.com/astral-sh/uv)
- [Tailwind CSS](https://tailwindcss.com/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/misc/design-philosophies/)
