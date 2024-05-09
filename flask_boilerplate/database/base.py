"""
Base Module

Description:
    - This module is used to configure database connection and configure base
    model.

"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
)
from sqlalchemy.sql.functions import now

from flask_boilerplate.core.config import DB_SCHEMA


class BaseTable(DeclarativeBase):
    """
    Base Table

    Description:
        - This is base model for all tables.

    Attributes:
        - `id (int)`: Primary key.
        - `created_at (datetime)`: Created at timestamp.
        - `updated_at (datetime)`: Updated at timestamp.

    """

    __abstract__ = True
    metadata = MetaData(schema=DB_SCHEMA)

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True, onupdate=now()
    )

    @declared_attr.directive
    def __tablename__(self) -> str:
        """
        Generate table name automatically.

        """
        return self.__name__.lower().replace("table", "")

    # Convert to dictionary
    def to_dict(self) -> dict:
        """
        Convert to dictionary.

        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# Initialize SQLAlchemy with BaseTable
db = SQLAlchemy(model_class=BaseTable)
