# Flask-API

[Cookiecutter](https://github.com/cookiecutter/cookiecutter.git) template to create new [flask](https://github.com/pallets/flask) application to build a Web API.

## Layout

Project Layout from [miguelgrinberg/flasky: Companion code to my O'Reilly book "Flask Web Development", second edition.](https://github.com/miguelgrinberg/flasky)

```text
│  .gitignore
│  config.py
│  README.md
│  {{cookiecutter.application_name}}.py
│
├─tests
└─{{cookiecutter.application_name}}
    │  exceptions.py  # your custom exceptions
    │  __init__.py  # create_app function here
    │
    ├─main  # your main blueprint
    │      errors.py  # web errors like 404, 403
    │      views.py  # just have index route
    │      __init__.py
    │
    └─models  # database models here
            __init__.py
```

## How to use

### With [Cookiecutter](https://github.com/cookiecutter/cookiecutter.git)

#### Install Cookiecutter

```bash
pip install --upgrade cookiecutter
```

#### Create a new project

```bash
cookiecutter https://github.com/jennier0107/Flask-API
```

### With [Flasky-Cli](https://github.com/jennier0107/flasky-cli)

#### Install Flasky-Cli

```bash
pip install --upgrade flasky-cli
```

#### Create a new project

```bash
flasky-cli create
```

and choice `Flask-API` template.

## Initialize project and run

You can use tools like pdm, pipenv, poetry or rye to init and run your project.