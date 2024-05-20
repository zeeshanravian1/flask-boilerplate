"""
Role Permission Repository

Description:
    - This module contains role permission repository.

"""

from sqlalchemy.orm.query import Query

from flask_boilerplate.models.role import RoleTable
from flask_boilerplate.models.role_permission import RolePermissionTable

from .base import BaseRepository, db


class RolePermissionRepository(BaseRepository[RolePermissionTable]):
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

    def create_role_permission(
        self, role_id, permission_id
    ) -> RolePermissionTable | None:
        """
        Add Permission against a role

        Description:
            - This is used to add permissions against the role.

        Args:
            - `role_id (int)`: Role ID. **(Required)**
            - `permission_id (int)`: Permission ID. **(Required)**

        Returns:
            - `row (RolePermissionTable)`: Role Permission object.

        """

        role_permission: Query[RolePermissionTable] = db.session.query(
            self.model
        ).filter(
            self.model.role_id == role_id,
            self.model.permission_id == permission_id,
        )

        if role_permission.count():
            return None

        row: RolePermissionTable = super().create(
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
