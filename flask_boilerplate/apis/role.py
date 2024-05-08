# -*- coding: utf-8 -*-
"""
Role APIs

Description:
    - This module is used to handle all role routes.

"""

from flask import Blueprint, request

from flask_boilerplate.constants.role import ROLE_COLUMN
from flask_boilerplate.schemas.role import RoleReadSchema
from flask_boilerplate.services.role import RoleService

role_router = Blueprint(name="role", import_name=__name__, url_prefix="/role")


# Create Role
@role_router.route("", methods=["POST"])
def create_role():
    """
    Create Role

    Description:
        - This is used to create a new role.

    Request:
        - `role (RoleCreateSchema)`: Role object.

    Returns:
        - `role (RoleCreateSchema)`: Role object.

    """

    role = RoleService().create(request.json)

    return RoleReadSchema().dump(role)


# Get role by ID
@role_router.route("/<int:role_id>", methods=["GET"])
def read_role_by_id(role_id: int):
    """
    Read Role by ID

    Description:
        - This is used to read role by ID.

    Args:
        - `role_id (int)`: Role ID. **(Required)**

    Returns:
        - `role (RoleCreateSchema)`: Role object.

    """

    role = RoleService().read_by_id(role_id)

    return RoleReadSchema().dump(role)


# Get role by name
@role_router.route("/<string:role_name>", methods=["GET"])
def read_role_by_name(role_name: str):
    """
    Read Role by Name

    Description:
        - This is used to read role by name.

    Args:
        - `role_name (str)`: Role Name. **(Required)**

    Returns:
        - `role (RoleCreateSchema)`: Role object.

    """

    role = RoleService().read_by_name(
        entity_column=ROLE_COLUMN, entity_name=role_name
    )

    return RoleReadSchema().dump(role)


# Get all roles
@role_router.route("", methods=["GET"])
def read_all_roles():
    """
    Read All Roles

    Description:
        - This is used to read all roles.

    Returns:
        - `roles (List[RoleCreateSchema])`: List of role objects.

    """

    roles = RoleService().read_all()

    return RoleReadSchema().dump(roles, many=True)


# Update role by ID
@role_router.route("/<int:role_id>", methods=["PUT"])
def update_role(role_id: int):
    """
    Update Role by ID

    Description:
        - This is used to update role by ID.

    Args:
        - `role_id (int)`: Role ID. **(Required)**

    Request:
        - `role (RoleCreateSchema)`: Role object.

    Returns:
        - `role (RoleCreateSchema)`: Role object.

    """

    role = RoleService().update(role_id, request.json)

    return RoleReadSchema().dump(role)


# Delete role by ID
@role_router.route("/<int:role_id>", methods=["DELETE"])
def delete_role(role_id: int) -> dict[str, str]:
    """
    Delete Role by ID

    Description:
        - This is used to delete role by ID.

    Args:
        - `role_id (int)`: Role ID. **(Required)**

    Returns:
        - `message (str)`: Success message.

    """

    RoleService().delete(role_id)

    return {"message": "Role deleted successfully."}
