"""
Permission APIs

Description:
    - This module is used to handle all role routes.

"""

from flask_restx import Resource

from flask_boilerplate.namespaces.permission import ns_permission
from flask_boilerplate.schemas.permission import (
    permission_create_expect,
    permission_read_schema,
)
from flask_boilerplate.decorator.authorization import auth
from flask_boilerplate.services.permission import PermissionService
from flask_boilerplate.responses.permission import PermissionResponse


@ns_permission.route("/")
class PermissionListResource(Resource):
    """
    Permission List Resource

    Description:
        - This class is used to handle listing and adding permission.

    """

    @auth()
    @ns_permission.expect(permission_create_expect, validate=True)
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

    @auth()
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
        return PermissionResponse.read_all_response(data=permissions)
