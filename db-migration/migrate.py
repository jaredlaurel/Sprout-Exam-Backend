import typer
from alembic.command import revision as alembic_revision
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig

from app.core.config import ALEMBIC_INI, DATABASE_URI, MIGRATIONS_PATH

app = typer.Typer()


@app.command()
def makemigrations(message: str):
    alembic_config = AlembicConfig(ALEMBIC_INI)
    alembic_config.set_main_option("script_location", MIGRATIONS_PATH)
    alembic_config.set_main_option("sqlalchemy.url", DATABASE_URI)
    alembic_upgrade(alembic_config, "head")
    alembic_revision(alembic_config, autogenerate=True, message=message)


@app.command()
def migrate():
    # run migration
    alembic_config = AlembicConfig(ALEMBIC_INI)
    alembic_config.set_main_option("script_location", MIGRATIONS_PATH)
    alembic_config.set_main_option("sqlalchemy.url", DATABASE_URI)
    alembic_upgrade(alembic_config, "head")


if __name__ == "__main__":
    app()
