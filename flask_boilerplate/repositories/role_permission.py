"""
Role Permission Repository

Description:
    - This module contains role permission repository.

"""

from flask_boilerplate.models.role_permission import RolePermissionTable
from flask_boilerplate.models.role import RoleTable

from .base import BaseRepository, db


class RolePermissionRepository(BaseRepository):
    """
    Role Permission Repository

    Description:
        - This is used to interact with role permission table.

    """

    def __init__(self) -> None:
        """
        Role Permission Repository Constructor

        Description:
            - This is used to initialize role permission repository.

        """

        super().__init__(RolePermissionTable)

    def create_role_permission(self, role_id, permission_id):
        """
        Add Permission against a role

        Description:
            - this is used to add permissions against the role

        """

        role_permission = db.session.query(RolePermissionTable).filter(
            RolePermissionTable.role_id == role_id,
            RolePermissionTable.permission_id == permission_id,
        )
        if role_permission.count():
            return None

        row = super().create(
            {"role_id": role_id, "permission_id": permission_id}
        )
        return row

    def get_role_permissions(self, role_id):
        role = db.session.query(RoleTable).filter(RoleTable.id == role_id)
        if role:
            role_permissions = db.session.query(RolePermissionTable).filter(
                RolePermissionTable.role_id == role_id
            )
            return role_permissions.all(), role.first().role_name

        return None

    def get_role_permission(self, role_id, permission_id):
        row = db.session.query(RolePermissionTable).filter(
            RolePermissionTable.role_id == role_id,
            RolePermissionTable.permission_id == permission_id,
        )
        return row
