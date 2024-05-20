"""
Role Permission APIs

Description:
    - This module is used to handle all role permission routes.

"""

from flask_restx import Resource

from flask_boilerplate.namespaces.role_permission import ns_role_permission
from flask_boilerplate.decorator.authorization import auth
from flask_boilerplate.schemas.role_permission import (
    role_permission_patch_expect,
    role_permission_patch_response,
)
from flask_boilerplate.services.role_permission import RolePermissionService
from flask_boilerplate.responses.role_permission import RolePermissionResponse


@ns_role_permission.route("/")
class RolePermissionPatchResource(Resource):
    """
    Role Permission update Resource

    Description:
        - This class is used to handle updation of role_permission.

    """

    # @auth()
    @ns_role_permission.expect(role_permission_patch_expect, validate=True)
    @ns_role_permission.marshal_with(role_permission_patch_response)
    def post(self):
        """
        Update Role_Permission

        Description:
            - This function is used to add a new permission against a role.

        Args:
            - `role_id (int)`: Id of role. **(Required)**
            - `permission_id (int)`: Id of permission. **(Optional)**

        Returns:
        Role and Permission details along with following information:
            - `id (int)`: ID of permission.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role update.

        """

        role_permission = RolePermissionService().create_record(
            role_id=ns_role_permission.payload["role_id"],
            permission_id=ns_role_permission.payload["permission_id"],
        )
        if not role_permission:
            return RolePermissionResponse.failure(
                "Permission already exist against this role"
            )

        return RolePermissionResponse.success(data=role_permission)


@ns_role_permission.route("/<int:role_id>")
class RolePermissionListResource(Resource):
    @auth("Create Role")
    @ns_role_permission.marshal_with(role_permission_patch_response)
    def get(self, role_id):
        """
        Lis Role_Permission

        Description:
            - This function is used to list permissions against a role.

        Args:
            - `role_id (int)`: Id of role. **(Required)**

        Returns:
        Role and Permission details along with following information:
            - `id (int)`: ID of permission.
            - `created_at (str)`: Datetime of role creation.
            - `updated_at (str)`: Datetime of role update.
        """
        role_permissions = RolePermissionService().get_role_permission(role_id)

        return RolePermissionResponse.success(data=role_permissions)
