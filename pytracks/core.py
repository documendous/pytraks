import os
import click

APP_STRUCTURE = [
    "app/models",
    "app/views",
    "app/controllers",
    "app/templates",
    "config",
    "db/migrations",
    "pytracks"
]

@click.group()
def cli():
    pass

@cli.command()
@click.argument('app_name')
def new(app_name):
    os.makedirs(app_name, exist_ok=True)
    os.chdir(app_name)

    for path in APP_STRUCTURE:
        os.makedirs(path, exist_ok=True)

    with open("manage.py", "w") as f:
        f.write("""#!/usr/bin/env python
if __name__ == '__main__':
    print('PyTracks manage script placeholder')
""")

    with open("requirements.txt", "w") as f:
        f.write("flask\nclick\n")

    with open("config/routes.py", "w") as f:
        f.write("# Define your routes here\n")

    with open("pytracks/core.py", "w") as f:
        f.write("# Core framework logic will go here\n")

    click.echo(f"PyTracks app '{app_name}' created.")

