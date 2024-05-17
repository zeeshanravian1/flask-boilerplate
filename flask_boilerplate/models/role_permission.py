"""
Role_Permission Model

Description:
    - This file contains model for role_permission table.

"""

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_boilerplate.database.base import BaseTable
from flask_boilerplate.models.role import RoleTable
from flask_boilerplate.models.permission import PermissionTable


class RolePermissionTable(BaseTable):
    """
    Role Permission Table

    Description:
        - This table is used to create role_permission in database.

    """

    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(RoleTable.id, ondelete="CASCADE"),
        nullable=False,
        unique=False,
    )
    permission_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(PermissionTable.id, ondelete="CASCADE"),
        nullable=False,
        unique=False,
    )

    role = relationship("Role", backref="role_to_role_permission")
    permission = relationship(
        "Permission", backref="permission_to_role_permission"
    )
