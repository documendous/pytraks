from .tasks import (
    create_core_file,
    create_manage_script,
    create_requirements_file,
    create_routes_file,
)


APP_STRUCTURE = [
    "app/models",
    "app/views",
    "app/controllers",
    "app/templates",
    "config",
    "db/migrations",
    "pytracks",
]

TASKS = [
    create_manage_script,
    create_requirements_file,
    create_routes_file,
    create_core_file,
]
