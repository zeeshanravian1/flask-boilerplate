"""
This file will add all the permissions/role in the DB for first time
"""

from logging import Logger
from flask_boilerplate.constants.enum import (
    UserPermissions,
    RolePermissions,
    PermissionPermissions,
    Roles,
)
from flask_boilerplate.services.permission import PermissionService
from flask_boilerplate.services.role import RoleService
from flask_boilerplate.services.role_permission import RolePermissionService
from flask_boilerplate.core.logger import AppLogger

logger: Logger = AppLogger().get_logger()


def add_permissions():
    """
    Insert all the permissions into the db
    """
    module_list = [UserPermissions, RolePermissions, PermissionPermissions]
    for module in module_list:
        permission_list = module.list()
        for perm in permission_list:
            permission = PermissionService().read_by_name(
                "permission_name", perm
            )
            if permission:
                logger.error("Permission already exist")
            else:
                PermissionService().create({"permission_name": perm})


def add_roles():
    """
    Insert all the roles into the db
    """
    roles = Roles.list()
    for role in roles:
        data = RoleService().read_by_name("role_name", role)
        if data:
            logger.error("Role already exist")
        else:
            RoleService().create({"role_name": role})


def add_admin_permissions():
    """
    This function will add all permissions against admin role
    """
    admin_id = RoleService().read_by_name("role_name", Roles.ADMIN.value).id
    permissions = PermissionService().read_all()
    for permission in permissions:
        role_permission = RolePermissionService().get_role_n_permission(
            admin_id, permission.id
        )
        if role_permission.first():
            logger.error("This Permission already exist for this role")
        else:
            RolePermissionService().create(
                {"role_id": admin_id, "permission_id": permission.id}
            )
