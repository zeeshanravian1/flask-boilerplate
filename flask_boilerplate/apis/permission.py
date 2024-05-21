"""
Permission APIs

Description:
    - This module is used to handle all role routes.

"""

from flask_restx import Resource

from flask_boilerplate.decorator.authorization import auth
from flask_boilerplate.namespaces.permission import ns_permission
from flask_boilerplate.responses.permission import PermissionResponse
from flask_boilerplate.schemas.permission import (
    permission_create_schema,
    permission_read_schema,
    permission_update_schema,
)
from flask_boilerplate.services.permission import PermissionService
from flask_boilerplate.constants.enum import PermissionPermissions
from flask_boilerplate.constants.permission import PERMISSION
from scripts.update_redis import remove_permission_from_roles


@ns_permission.route("/")
class PermissionListResource(Resource):
    """
    Permission List Resource

    Description:
        - This class is used to handle listing and adding permission.

    """

    @auth(PermissionPermissions.CREATE_PERMISSION.value)
    @ns_permission.expect(permission_create_schema, validate=True)
    @ns_permission.marshal_with(permission_read_schema, skip_none=True)
    def post(self):
        """
        Add Permission

        Description:
            - This function is used to add a new permission.

        Args:
        Permission details to be created with following fields:
            - `permission_name (str)`: Name of permission. **(Required)**
            - `permission_description (str)`: Description of permission. **(Optional)**

        Returns:
        Permission details along with following information:
            - `id (int)`: ID of permission.
            - `permission_name (str)`: Name of permission.
            - `permission_description (str)`: Description of permission.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role update.

        """

        permission = PermissionService().create(entity=ns_permission.payload)

        return PermissionResponse.create_response(data=permission)

    @auth(PermissionPermissions.GET_ALL_PERMISSION.value)
    @ns_permission.marshal_with(permission_read_schema, skip_none=True)
    def get(self):
        """
        Get all Permissions

        Description:
            - This function is used to get all permissions.

        Args:
            - `None`

        Returns:
        Get all permissions with following information:
            - `id (int)`: ID of permission.
            - `permission_name (str)`: Name of permission.
            - `permission_description (str)`: Description of permission.
            - `created_at (str)`: Datetime of permission creation.
            - `updated_at (str)`: Datetime of permission update.

        """

        permissions = PermissionService().read_all()
        return PermissionResponse.success(
            data=permissions, total_rows=len(permissions)
        )


# Resource to handle get, update, delete single permission
@ns_permission.route("/<int:id>")
class PermissionResource(Resource):
    """
    Permission Resource

    Description:
        - This class is used to handle get, update, delete single permission.

    """

    @auth(PermissionPermissions.GET_PERMISSION.value)
    @ns_permission.marshal_with(permission_read_schema)
    def get(self, id):
        """
        Get Permission

        Description:
            - This function is used to get a single permission by providing role ID.

        Args:
            - `id (int)`: ID of permission. **(Required)**

        Returns:
        Single Permission details along with following information:
            - `id (int)`: ID of permission.
            - `permission_name (str)`: Name of permission.
            - `permission_description (str)`: Description of permission.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role updation.

        """

        permission = PermissionService().read_by_id(entity_id=id)

        if not permission:
            return PermissionResponse.not_found_response(data=PERMISSION)

        return PermissionResponse.success(data=permission)

    @auth(PermissionPermissions.UPDATE_PERMISSION.value)
    @ns_permission.expect(permission_update_schema, validate=True)
    @ns_permission.marshal_with(permission_read_schema)
    def patch(self, id):
        """
        Update Permission

        Description:
            - This function is used to update a single permission by providing permission
            ID.

        Args:
            - `id (int)`: ID of permission. **(Required)**
            Permission details to be updated with following fields:
            - `permission_name (str)`: Name of permission. **(Required)**
            - `permission_description (str)`: Description of permission. **(Optional)**

        Returns:
        Updated Permission details along with following information:
            - `id (int)`: ID of permission.
            - `permission_name (str)`: Name of permission.
            - `permission_description (str)`: Description of permission.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role updation.

        """

        permission = PermissionService().update(
            entity_id=id, entity=ns_permission.payload
        )

        if not permission:
            return PermissionResponse.not_found_response(data=PERMISSION)

        return PermissionResponse.update_response(data=permission)

    @auth(PermissionPermissions.DELETE_PERMISSION.value)
    def delete(self, id):
        """
        Delete Permission

        Description:
            - This function is used to delete a permission.

        Args:
            - `role_id (int)`: ID of role. **(Required)**

        Returns:
            - `None`

        """
        permission_name = PermissionService().read_by_id(id)
        permission = PermissionService().delete(entity_id=id)

        if not permission:
            return PermissionResponse.not_found_response(data=PERMISSION)

        remove_permission_from_roles(permission_name.permission_name)
        return PermissionResponse.delete_response()
