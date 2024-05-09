"""
Role APIs

Description:
    - This module is used to handle all role routes.

"""

from http import HTTPStatus

from flask import Blueprint, request
from marshmallow import ValidationError

from flask_boilerplate.constants.base import CONTENT_TYPE_JSON
from flask_boilerplate.constants.role import ROLE, ROLE_COLUMN
from flask_boilerplate.responses.role import RoleResponse
from flask_boilerplate.schemas.role import (
    RoleCreateSchema,
    RoleReadSchema,
    RoleUpdateSchema,
)
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

    # Validate JSON data
    try:
        json_data = RoleCreateSchema().load(data=request.get_json())

    except ValidationError as err:
        return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY, CONTENT_TYPE_JSON

    # Create role
    role = RoleService().create(entity=json_data)

    return RoleResponse.create_response(data=RoleReadSchema().dump(role))


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

    role = RoleService().read_by_id(entity_id=role_id)

    if not role:
        return RoleResponse.not_found_response(data=ROLE)

    return RoleResponse.read_response(data=RoleReadSchema().dump(role))


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

    if not role:
        return RoleResponse.not_found_response(data=ROLE)

    return RoleResponse.read_response(data=RoleReadSchema().dump(role))


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

    return RoleResponse.read_all_response(
        data=RoleReadSchema().dump(roles, many=True)
    )


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

    # Validate JSON data
    try:
        json_data = RoleUpdateSchema().load(data=request.get_json())

    except ValidationError as err:
        return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY, CONTENT_TYPE_JSON

    role = RoleService().update(entity_id=role_id, entity=json_data)

    if not role:
        return RoleResponse.not_found_response(data=ROLE)

    return RoleResponse.update_response(data=RoleReadSchema().dump(role))


# Delete role by ID
@role_router.route("/<int:role_id>", methods=["DELETE"])
def delete_role(role_id: int):
    """
    Delete Role by ID

    Description:
        - This is used to delete role by ID.

    Args:
        - `role_id (int)`: Role ID. **(Required)**

    Returns:
        - `message (str)`: Success message.

    """

    role = RoleService().delete(role_id)

    if not role:
        return RoleResponse.not_found_response(data=ROLE)

    return RoleResponse.delete_response()
