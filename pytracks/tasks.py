MANAGE_SCRIPT = "manage.py"
REQUIREMENTS_FILE = "requirements.txt"
ROUTES_FILE = "config/routes.py"
CORE_FILE = "pytracks/core.py"


def create_manage_script():
    """Creates a manage script"""
    with open(MANAGE_SCRIPT, "w") as f:
        f.write(
            """#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to PyTracks!'

if __name__ == '__main__':
    app.run(debug=True)
"""
        )


def create_requirements_file():
    """Creates a requirements.txt file"""
    with open(REQUIREMENTS_FILE, "w") as f:
        f.write("flask\nclick\n")


def create_routes_file():
    """Creates a routes module"""
    with open(ROUTES_FILE, "w") as f:
        f.write("# Define your routes here\n")


def create_core_file():
    """Creates a core module"""
    with open(CORE_FILE, "w") as f:
        f.write("# Core framework logic will go here\n")
