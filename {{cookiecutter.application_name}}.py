import os

from {{cookiecutter.package_name}} import create_app


{{cookiecutter.application_name}} = create_app(os.getenv('FLASK_CONFIG') or 'default')