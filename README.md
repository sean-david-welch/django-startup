# Quick django startup to learn best practices

### Project setup 

- brew install uv
    - This is a package manager far easier to work with than pip

- add alias is .zshrc -- alias django='uv run python manage.py'
    - this will make it easier to run django specific commands

- git clone project: git clone https://github.com/YourUsername/YourProject.git
    - pull remote files in local device

- cd project && uv sync
    - change directory and sync uv environment with the pyproject.toml file

- start coding and write something in django; some django specific commands are listed below
    - python manage.py startproject <project:name> - starts an entirely new project with starter files (already done)
    - python manage.py startapp <app:name> - add a new app to the project; apps are usually a module that describe a dataclass or set of dataclasses

- Best practices:
    - Use class based views instead of functions; they encapsulate boiler plate and a far easier to work with
    - Type annotate everything
    - Write tests
    - Don't commit sensitive info to git such as api keys
