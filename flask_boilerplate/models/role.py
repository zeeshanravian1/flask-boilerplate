"""
Role Model

Description:
    - This file contains model for role table.

"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_boilerplate.database.base import BaseTable


class RoleTable(BaseTable):
    """
    Role Table

    Description:
        - This table is used to create role in database.

    """

    role_name: Mapped[str] = mapped_column(String(2_55), unique=True)
    role_description: Mapped[str] = mapped_column(String(2_55), nullable=True)

    # Relationships
    users: Mapped[list["UserTable"]] = relationship(  # noqa:F821 # type:ignore
        back_populates="role", cascade="all, delete-orphan"
    )
    permissions: Mapped[list["RolePermissionTable"]] = (  # noqa:F821
        relationship(back_populates="role", cascade="all, delete-orphan")
    )
