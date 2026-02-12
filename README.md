# Quick django startup to learn best practices

### Project setup

- brew install uv
    - This is a package manager far easier to work with than pip

- add alias in .zshrc -- `alias django='uv run python manage.py'`
    - this will make it easier to run django specific commands

- git clone project: `git clone https://github.com/YourUsername/YourProject.git`
    - pull remote files in local device

- cd project && uv sync
    - change directory and sync uv environment with the pyproject.toml file

- start coding and write something in django; some django specific commands are listed below
    - `django startproject <project:name>` - starts an entirely new project with starter files (already done)
    - `django startapp <app:name>` - add a new app to the project; apps are usually a module that describe a dataclass or set of dataclasses

- Best practices:
    - Use class based views instead of functions; they encapsulate boiler plate and a far easier to work with
    - Type annotate everything
    - Write tests
    - Don't commit sensitive info to git such as api keys

### Dependencies Overview

**Core & Utilities:**
- **django-environ** - Manages environment variables from `.env` files. Use `from django_environ import Env` in settings to load config.
- **django-extensions** - Provides extra management commands like `shell_plus` (enhanced shell with imports) and `runserver_plus` (debugger support)

**UI & Frontend:**
- **django-tailwind** - Integrates Tailwind CSS for styling. Run `django tailwind install` to set up, then `django tailwind start` to watch for changes during development.
- **django-unfold** - Modern, polished Django admin interface replacing the default admin. Automatically replaces the admin with a better UX.

**Code Quality:**
- **ruff** - Fast Python linter and formatter. Run `ruff check` to find issues, `ruff format` to auto-format code, or `ruff check --fix` to auto-fix issues.

**Development (Dev dependencies):**
- **django-debug-toolbar** - Shows debugging info in the browser (SQL queries, templates, timing). Automatically loads when `DEBUG=True` in development.
- **django-stubs** - Provides type hints for Django, enabling better IDE autocomplete and static type checking with mypy/pyright.

### Making a Pull Request

To contribute your code for review:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/YourProject.git
   cd YourProject
   uv sync
   ```

2. **Create a new branch** for your feature/fix:
   ```bash
   git checkout -b feature/description-of-changes
   ```

3. **Make your changes** and commit:
   ```bash
   git add .
   git commit -m "Clear description of what you changed"
   ```

4. **Push your branch**:
   ```bash
   git push origin feature/description-of-changes
   ```

5. **Open a Pull Request** on GitHub:
   - Go to https://github.com/YourUsername/YourProject
   - You'll see a "Compare & pull request" button for your branch
   - Click it and fill in a description of your changes
   - Click "Create pull request"

6. **Wait for review**: Your PR will be reviewed and merged once approved!
