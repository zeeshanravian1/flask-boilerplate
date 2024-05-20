"""
Role Permission Validation Schemas

Description:
    - This file contains all role permission schemas used by API.

"""

from flask_restx import Model, OrderedModel
from flask_restx.fields import Integer, String, Nested, List

from flask_boilerplate.constants.role_permission import ROLE_ID, PERMISSION_ID
from flask_boilerplate.namespaces.role_permission import ns_role_permission

role_permission_patch_expect: Model | OrderedModel = ns_role_permission.model(
    "RolePermissionPatchExpect",
    {
        "role_id": Integer(requried=True, example=ROLE_ID),
        "permission_id": Integer(required=True, example=PERMISSION_ID),
    },
    strict=True,
)

role_data: Model | OrderedModel = ns_role_permission.model(
    "RoleData",
    {"id": Integer(), "role_name": String(), "role_description": String()},
)

permission_data: Model | OrderedModel = ns_role_permission.model(
    "PermissionData",
    {
        "id": Integer(),
        "permission_name": String(),
        "permission_description": String(),
    },
)

role_permission_patch: Model | OrderedModel = ns_role_permission.model(
    "RolePermissionPatchResponse",
    {
        "id": Integer(),
        "role": Nested(role_data),
        "permission": Nested(permission_data),
    },
)

role_permission_patch_response = ns_role_permission.model(
    "UserLoginResponse",
    {
        "status": String(description="ok|nok"),
        "object": Nested(
            role_permission_patch, skip_none=True, allow_null=True
        ),
        "errors": List(String),
    },
)
