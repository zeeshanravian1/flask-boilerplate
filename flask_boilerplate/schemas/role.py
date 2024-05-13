"""
Role Validation Schemas

Description:
    - This file contains all role schemas used by API.

"""

from datetime import datetime, timezone

from flask_restx import Model, OrderedModel
from flask_restx.fields import Boolean, DateTime, Integer, Nested, String

from flask_boilerplate.constants.role import ROLE_DESCRIPTION, ROLE_NAME
from flask_boilerplate.namespaces.role import ns_role

# Role Base Schema
role_base_schema: Model | OrderedModel = ns_role.model(
    name="RoleBaseSchema",
    model={
        "role_name": String(
            required=True, min_length=1, max_length=2_55, example=ROLE_NAME
        ),
        "role_description": String(
            min_length=1, max_length=2_55, example=ROLE_DESCRIPTION
        ),
    },
    strict=True,
)

# Role Create Schema
role_create_schema = ns_role.inherit(
    "RoleCreateSchema",
    role_base_schema,
    {"role_name": String(required=True)},
)

# Role Read Base Schema
role_read_base_schema: Model | OrderedModel = ns_role.inherit(
    "RoleReadBaseSchema",
    role_base_schema,
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

# Role Read Schema
role_read_schema: Model | OrderedModel = ns_role.model(
    name="RoleReadSchema",
    model={
        "success": Boolean(default=True),
        "data": Nested(role_read_base_schema),
    },
    strict=True,
)

# Role Read All Schema
role_read_all_schema: Model | OrderedModel = ns_role.model(
    name="RoleReadAllSchema",
    model={
        "success": Boolean(default=True),
        "data": Nested(role_read_base_schema, as_list=True),
    },
    strict=True,
)

# Role Update Schema
role_update_schema: Model | OrderedModel = ns_role.inherit(
    "RoleUpdateSchema", role_base_schema
)
