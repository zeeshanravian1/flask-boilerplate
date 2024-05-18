"""
Permission Model

Description:
    - This file contains model for permission table.

"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_boilerplate.database.base import BaseTable


class PermissionTable(BaseTable):
    """
    Permission Table

    Description:
        - This table is used to create permission in database.

    """

    permission_name: Mapped[str] = mapped_column(String(2_55), unique=True)
    permission_description: Mapped[str] = mapped_column(
        String(2_55), nullable=True
    )

    # Relationships
    roles: Mapped[list["RolePermissionTable"]] = relationship(  # noqa:F821
        back_populates="permission", cascade="all, delete-orphan"
    )
