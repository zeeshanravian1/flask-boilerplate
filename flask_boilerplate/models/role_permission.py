"""
Role_Permission Model

Description:
    - This file contains model for role_permission table.

"""

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_boilerplate.database.base import BaseTable
from flask_boilerplate.models.permission import PermissionTable
from flask_boilerplate.models.role import RoleTable


class RolePermissionTable(BaseTable):
    """
    Role Permission Table

    Description:
        - This table is used to create role_permission in database.

    """

    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(RoleTable.id, ondelete="CASCADE"),
    )
    permission_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(PermissionTable.id, ondelete="CASCADE"),
    )

    # Relationships
    role: Mapped[RoleTable] = relationship(back_populates="permissions")
    permission: Mapped[PermissionTable] = relationship(back_populates="roles")
