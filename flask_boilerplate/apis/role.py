"""
Role APIs

Description:
    - This module is used to handle all role routes.

"""

from http import HTTPStatus

from flask import request
from flask_restx import Resource

from flask_boilerplate.constants.role import ROLE, ROLE_DELETE_SUCCESS
from flask_boilerplate.namespaces.role import ns_role
from flask_boilerplate.responses.role import RoleResponse
from flask_boilerplate.schemas.role import (
    role_create_schema,
    role_read_all_schema,
    role_read_schema,
    role_update_schema,
)
from flask_boilerplate.services.role import RoleService
from flask_boilerplate.constants.permissions import RolePermissions
from flask_boilerplate.decorator.authorization import auth


# Resource to handle listing and adding roles
@ns_role.route("/")
class RoleListResource(Resource):
    """
    Role List Resource

    Description:
        - This class is used to handle listing and adding roles.

    """

    @auth(RolePermissions.Create_Role.value)
    @ns_role.expect(role_create_schema, validate=True)
    @ns_role.marshal_with(fields=role_read_schema, code=HTTPStatus.CREATED)
    def post(self):
        """
        Add Role

        Description:
            - This function is used to add a new role.

        Args:
        Role details to be created with following fields:
            - `role_name (str)`: Name of role. **(Required)**
            - `role_description (str)`: Description of role. **(Optional)**

        Returns:
        Role details along with following information:
            - `id (int)`: ID of role.
            - `role_name (str)`: Name of role.
            - `role_description (str)`: Description of role.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role updation.

        """

        role = RoleService().create(entity=request.get_json())

        return RoleResponse.create_response(data=role)

    @auth(RolePermissions.GET_ALL_ROLE.value)
    @ns_role.marshal_with(fields=role_read_all_schema, code=HTTPStatus.OK)
    def get(self):
        """
        Get all Roles

        Description:
            - This function is used to get all roles.

        Args:
            - `None`

        Returns:
        Get all roles with following information:
            - `id (int)`: ID of role.
            - `role_name (str)`: Name of role.
            - `role_description (str)`: Description of role.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role updation.

        """

        # Get all roles
        roles = RoleService().read_all()

        return RoleResponse.read_all_response(data=roles)


# Resource to handle get, update, delete single role
@ns_role.route("/<int:role_id>")
class RoleResource(Resource):
    """
    Role Resource

    Description:
        - This class is used to handle get, update, delete single role.

    """

    @auth(RolePermissions.GET_ROLE.value)
    @ns_role.marshal_with(fields=role_read_schema, code=HTTPStatus.OK)
    def get(self, role_id):
        """
        Get Role

        Description:
            - This function is used to get a single role by providing role ID.

        Args:
            - `role_id (int)`: ID of role. **(Required)**

        Returns:
        Single Role details along with following information:
            - `id (int)`: ID of role.
            - `role_name (str)`: Name of role.
            - `role_description (str)`: Description of role.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role updation.

        """

        role = RoleService().read_by_id(entity_id=role_id)

        if not role:
            return RoleResponse.not_found_response(data=ROLE)

        return RoleResponse.read_response(data=role)

    @auth(RolePermissions.UPDATE_ROLE.value)
    @ns_role.expect(role_update_schema, validate=True)
    @ns_role.marshal_with(fields=role_read_schema, code=HTTPStatus.ACCEPTED)
    def put(self, role_id):
        """
        Update Role

        Description:
            - This function is used to update a single role by providing role
            ID.

        Args:
            - `role_id (int)`: ID of role. **(Required)**
            Role details to be updated with following fields:
            - `role_name (str)`: Name of role. **(Required)**
            - `role_description (str)`: Description of role. **(Optional)**

        Returns:
        Updated Role details along with following information:
            - `id (int)`: ID of role.
            - `role_name (str)`: Name of role.
            - `role_description (str)`: Description of role.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role updation.

        """

        role = RoleService().update(
            entity_id=role_id, entity=request.get_json()
        )

        if not role:
            return RoleResponse.not_found_response(data=ROLE)

        return RoleResponse.update_response(data=role)

    @auth(RolePermissions.DELETE_ROLE.value)
    @ns_role.response(
        code=HTTPStatus.NO_CONTENT, description=ROLE_DELETE_SUCCESS
    )
    def delete(self, role_id):
        """
        Delete Role

        Description:
            - This function is used to delete a role.

        Args:
            - `role_id (int)`: ID of role. **(Required)**

        Returns:
            - `None`

        """

        role = RoleService().delete(entity_id=role_id)

        if not role:
            return RoleResponse.not_found_response(data=ROLE)

        return RoleResponse.delete_response()
