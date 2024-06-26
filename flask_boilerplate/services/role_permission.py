"""
Role Permission Service

Description:
    - This module contains role permission service.

"""

from flask_boilerplate.repositories.role_permission import (
    RolePermissionRepository,
)

from flask_boilerplate.services.base import BaseService
from flask_boilerplate.services.redis import redis


class RolePermissionService(BaseService):
    """
    Role Permission Service

    Description:
        - This is used to interact with role permission repository.

    """

    def __init__(self) -> None:
        """
        Role Permission Service Constructor

        Description:
            - Initializes Role Permission Service object

        """

        super().__init__(RolePermissionRepository)

    def create_record(self, role_id, permission_id):
        record = self.repository.create_role_permission(role_id, permission_id)
        if record:
            redis.delete(role_id)
            permissions, role_name = self.repository.get_role_permissions(
                role_id
            )
            if permissions:
                name = []
                for perm in permissions:
                    name.append(perm.permission.permission_name)
                redis.set(role_name, name)
        return record

    def get_role_permission(self, role_id):
        """
        Get all permissions against a role

        Args:
            - `role_id (int)`: Role id **(Required)**

        """
        list, _ = self.repository.get_role_permissions(role_id)

        return list, len(list)

    def get_role_n_permission(self, role_id, permission_id):
        """
        Get the role and permission

        Args:
            - `role_id (int)`: Role id **(Required)**
            -  `permission_id (int)`: Permission id **(Required)**

        """
        row = self.repository.get_role_permission(role_id, permission_id)

        return row
