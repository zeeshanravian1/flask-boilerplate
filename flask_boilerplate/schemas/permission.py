"""
Permission Validation Schemas

Description:
    - This file contains all permission schemas used by API.

"""

from datetime import datetime, timezone

from flask_restx import Model, OrderedModel
from flask_restx.fields import Integer, String, Nested, Boolean, DateTime

from flask_boilerplate.constants.pemrission import (
    PERMISSION_DESCRIPTION,
    PERMISSION_NAME,
)
from flask_boilerplate.namespaces.permission import ns_permission

# Permission Base Schema
permission_base_schema: Model | OrderedModel = ns_permission.model(
    name="PermissionBaseSchema",
    model={
        "permission_name": String(
            min_length=3, max_length=250, example=PERMISSION_NAME
        ),
        "permission_description": String(
            min_length=1, max_length=2_55, example=PERMISSION_DESCRIPTION
        ),
    },
    strict=True,
)

# Permission Create Schema
permission_create_expect = ns_permission.inherit(
    "PermissionCreateSchema",
    permission_base_schema,
    {"permission_name": String(required=True)},
)


# Permission Read Schema
permission_read_schema: Model | OrderedModel = ns_permission.model(
    "PermissionReadSchema",
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
        "permission_name": String(),
        "permission_description": String(),
    },
)

# Permission Read Schema
permission_read_schema: Model | OrderedModel = ns_permission.model(
    name="PermissionReadSchema",
    model={
        "success": Boolean(default=True),
        "data": Nested(permission_read_schema),
    },
    strict=True,
)
