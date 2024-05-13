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


# Resource to handle listing and adding roles
@ns_role.route("/")
class RoleListResource(Resource):
    """
    Role List Resource

    Description:
        - This class is used to handle listing and adding roles.

    """

    @ns_role.expect(role_create_schema, validate=True)
    @ns_role.marshal_with(fields=role_read_schema, code=HTTPStatus.CREATED)
    def post(self):
        """
        Add Role

        Description:
            - This function is used to add a new role.

        Args:
            - `None`

        Returns:
            - `dict`: A dictionary containing the newly created role.

        """

        role = RoleService().create(entity=request.get_json())

        return RoleResponse.create_response(data=role)

    @ns_role.marshal_with(fields=role_read_all_schema, code=HTTPStatus.OK)
    def get(self):
        """
        List Roles

        Description:
            - This function is used to list all roles.

        Args:
            - `None`

        Returns:
            - `dict`: A dictionary containing list of roles.

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

    @ns_role.marshal_with(fields=role_read_schema, code=HTTPStatus.OK)
    def get(self, role_id):
        """
        Get Role

        Description:
            - This function is used to get a role.

        Args:
            - `role_id (int)`: Role ID. **(Required)**

        Returns:
            - `dict`: A dictionary containing the role.

        """

        role = RoleService().read_by_id(entity_id=role_id)

        if not role:
            return RoleResponse.not_found_response(data=ROLE)

        return RoleResponse.read_response(data=role)

    @ns_role.expect(role_update_schema, validate=True)
    @ns_role.marshal_with(fields=role_read_schema, code=HTTPStatus.ACCEPTED)
    def put(self, role_id):
        """
        Update Role

        Description:
            - This function is used to update a role.

        Args:
            - `role_id (int)`: Role ID. **(Required)**

        Returns:
            - `dict`: A dictionary containing the updated role.

        """

        role = RoleService().update(
            entity_id=role_id, entity=request.get_json()
        )

        if not role:
            return RoleResponse.not_found_response(data=ROLE)

        return RoleResponse.update_response(data=role)

    @ns_role.response(
        code=HTTPStatus.NO_CONTENT, description=ROLE_DELETE_SUCCESS
    )
    def delete(self, role_id):
        """
        Delete Role

        Description:
            - This function is used to delete a role.

        Args:
            - `role_id (int)`: Role ID. **(Required)**

        Returns:
            - `dict`: A dictionary containing the deleted role.

        """

        role = RoleService().delete(entity_id=role_id)

        if not role:
            return RoleResponse.not_found_response(data=ROLE)

        return RoleResponse.delete_response()
