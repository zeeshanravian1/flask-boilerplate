"""
Migration environment for database.

Description:
    - This file is used to configure migration environment for database.

"""

import logging
from logging.config import fileConfig

from alembic import context
from alembic.config import Config
from alembic.operations.ops import MigrationScript
from flask import current_app
from sqlalchemy import MetaData
from sqlalchemy.engine.base import Engine

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config: Config = context.config  # pylint: disable=E1101

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)  # type: ignore
logger: logging.Logger = logging.getLogger("alembic.env")


def get_engine() -> Engine:
    """
    Get the engine from the current app.

    Description:
        - This function is used to get the engine from the current app.

    Args:
        - `None`

    Returns:
        - `engine (Engine)`: Engine from the current app.

    """

    try:
        # this works with Flask-SQLAlchemy<3 and Alchemical
        return current_app.extensions["migrate"].db.get_engine()
    except (TypeError, AttributeError):
        # this works with Flask-SQLAlchemy>=3
        return current_app.extensions["migrate"].db.engine


def get_engine_url() -> str:
    """
    Get the engine URL from the current app.

    Description:
        - This function is used to get the engine URL from the current app.

    Args:
        - `None`

    Returns:
        - `engine_url (str)`: Engine URL from the current app.

    """

    try:
        return (
            get_engine()
            .url.render_as_string(hide_password=False)
            .replace("%", "%%")
        )
    except AttributeError:
        return str(get_engine().url).replace("%", "%%")


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
config.set_main_option("sqlalchemy.url", get_engine_url())
target_db = current_app.extensions["migrate"].db

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_metadata() -> MetaData:
    """
    Get the metadata from the target database.

    Description:
        - This function is used to get the metadata from the target database.

    Args:
        - `None`

    Returns:
        - `target_db`: Metadata from the target database.

    """

    if hasattr(target_db, "metadatas"):
        return target_db.metadatas[None]
    return target_db.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url: str | None = config.get_main_option("sqlalchemy.url")
    context.configure(  # pylint: disable=E1101
        url=url, target_metadata=get_metadata(), literal_binds=True
    )

    with context.begin_transaction():  # pylint: disable=E1101
        context.run_migrations()  # pylint: disable=E1101


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    # this callback is used to prevent an auto-migration from being generated
    # when there are no changes to the schema
    # reference: http://alembic.zzzcomputing.com/en/latest/cookbook.html
    def process_revision_directives(  # pylint: disable=W0613, W0621
        context, revision, directives
    ) -> None:
        if getattr(config.cmd_opts, "autogenerate", False):
            script: MigrationScript = directives[0]
            if script.upgrade_ops and script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info("No changes in schema detected.")

    conf_args: dict = current_app.extensions["migrate"].configure_args
    if conf_args.get("process_revision_directives") is None:
        conf_args["process_revision_directives"] = process_revision_directives

    connectable: Engine = get_engine()

    with connectable.connect() as connection:
        context.configure(  # pylint: disable=E1101
            connection=connection, target_metadata=get_metadata(), **conf_args
        )

        with context.begin_transaction():  # pylint: disable=E1101
            context.run_migrations()  # pylint: disable=E1101


if context.is_offline_mode():  # pylint: disable=E1101
    run_migrations_offline()
else:
    run_migrations_online()
