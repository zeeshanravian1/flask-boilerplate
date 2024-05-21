"""
Permission Validation Schemas

Description:
    - This file contains all permission schemas used by API.

"""

from datetime import datetime, timezone

from flask_restx import Model, OrderedModel
from flask_restx.fields import Boolean, DateTime, Integer, Nested, String

from flask_boilerplate.constants.permission import (
    PERMISSION_DESCRIPTION,
    PERMISSION_NAME,
)
from flask_boilerplate.namespaces.permission import ns_permission

# Permission Base Schema
permission_base_schema: Model | OrderedModel = ns_permission.model(
    name="PermissionBaseSchema",
    model={
        "permission_name": String(
            min_length=3, max_length=2_55, example=PERMISSION_NAME
        ),
        "permission_description": String(
            min_length=1, max_length=2_55, example=PERMISSION_DESCRIPTION
        ),
    },
    strict=True,
)

# Permission Create Schema
permission_create_schema = ns_permission.inherit(
    "PermissionCreateSchema",
    permission_base_schema,
    {"permission_name": String(required=True)},
)


# Permission Read Base Schema
permission_read_base_schema: Model | OrderedModel = ns_permission.inherit(
    "PermissionReadBaseSchema",
    permission_base_schema,
    {
        "id": Integer(readonly=True),
        "created_at": DateTime(
            required=True,
            readonly=True,
            example=datetime.now(tz=timezone.utc).isoformat(),
        ),
        "updated_at": DateTime(
            example=datetime.now(tz=timezone.utc).isoformat()
        ),
    },
)


# Permission Read Schema
permission_read_schema: Model | OrderedModel = ns_permission.model(
    name="PermissionReadSchema",
    model={
        "success": Boolean(default=True),
        "total_rows": Integer(),
        "data": Nested(permission_read_base_schema),
    },
    strict=True,
)


# Permission Read All Schema
permission_read_all_schema: Model | OrderedModel = ns_permission.model(
    name="PermissionReadAllSchema",
    model={
        "success": Boolean(default=True),
        "data": Nested(permission_read_base_schema, as_list=True),
    },
    strict=True,
)


# Permission Update Schema
permission_update_schema: Model | OrderedModel = ns_permission.model(
    "PermissionUpdateSchema",
    {"permission_description": String()},
)
