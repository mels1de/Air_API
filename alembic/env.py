import os
from logging.config import fileConfig
from sqlalchemy import pool, create_engine  
from sqlalchemy.engine import Connection
from alembic import context

from app.db.base import Base
from app.core.config import settings

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

raw_url = (
    os.getenv("SYNC_DATABASE_URL")
    or str(settings.DATABASE_URL).replace("+asyncpg", "")
)

if not raw_url:
    raise RuntimeError("Database URL for Alembic is not set")

config.set_main_option("sqlalchemy.url", raw_url)


def run_migrations_offline():
    context.configure(
        url=raw_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(
        raw_url,
        poolclass=pool.NullPool,
        future=True,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
