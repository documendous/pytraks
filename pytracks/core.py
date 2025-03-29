import os
import subprocess
import click

from .config import (
    APP_STRUCTURE,
    TASKS,
)


@click.group()
def cli():
    pass


@cli.command()
def s():
    """Starts the development server"""
    try:
        subprocess.run(["python", "manage.py"], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument("app_name")
def new(app_name):
    if os.path.exists(app_name):
        click.echo(f"Error: Directory '{app_name}' already exists.")
        return

    os.makedirs(app_name)
    os.chdir(app_name)

    for path in APP_STRUCTURE:
        os.makedirs(path, exist_ok=True)

    for run_task in TASKS:
        run_task()

    click.echo(f"PyTracks app '{app_name}' created.")
