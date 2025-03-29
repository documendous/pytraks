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
@click.option("--port", "-p", type=int, default=None, help="Port to run the server on")
@click.option(
    "--host", "-h", default=None, help="Host or host:port combo (e.g. 0.0.0.0:8000)"
)
def s(port, host):
    """Starts the development server"""
    if host and ":" in host:
        host, extracted_port = host.split(":", 1)
        port = int(extracted_port)

    host = host or "127.0.0.1"
    port = port or 5000

    try:
        subprocess.run(["python", "manage.py", str(port), host], check=True)
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
