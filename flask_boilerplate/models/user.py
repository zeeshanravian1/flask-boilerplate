"""
User Model

Description:
    - This file contains model for user table.

"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_boilerplate.database.base import BaseTable, db

from .role import RoleTable


class UserTable(BaseTable, db.Model):
    """
    User Table

    Description:
        - This table is used to create user in database.

    """

    first_name: Mapped[str] = mapped_column(String(2_55))
    last_name: Mapped[str] = mapped_column(String(2_55))
    contact: Mapped[str] = mapped_column(String(2_55), nullable=True)
    username: Mapped[str] = mapped_column(String(2_55), unique=True)
    email: Mapped[str] = mapped_column(String(2_55), unique=True)
    password: Mapped[str] = mapped_column(String(2_55))
    address: Mapped[str] = mapped_column(String(2_55), nullable=True)
    city: Mapped[str] = mapped_column(String(2_55), nullable=True)
    state: Mapped[str] = mapped_column(String(2_55), nullable=True)
    country: Mapped[str] = mapped_column(String(2_55), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(2_55), nullable=True)

    # Foreign Keys
    role_id: Mapped[int] = mapped_column(
        ForeignKey(RoleTable.id, ondelete="CASCADE")
    )

    # Relationships
    role: Mapped[RoleTable] = relationship(back_populates="users")
