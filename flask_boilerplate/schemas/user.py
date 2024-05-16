"""
User Validation Schemas

Description:
    - This file contains all user schemas used by API.

"""

from datetime import datetime, timezone

from flask_restx import Model, OrderedModel
from flask_restx.fields import Boolean, DateTime, Integer, Nested, String, List

from flask_boilerplate.constants.user import (
    ADDRESS,
    CITY,
    CONTACT,
    COUNTRY,
    EMAIL,
    FIRST_NAME,
    LAST_NAME,
    PASSWORD,
    POSTAL_CODE,
    ROLE_ID,
    STATE,
    USERNAME,
)
from flask_boilerplate.namespaces.user import ns_user

# User Base Schema
user_base_schema: Model | OrderedModel = ns_user.model(
    name="UserBaseSchema",
    model={
        "first_name": String(
            min_length=1, max_length=2_55, example=FIRST_NAME
        ),
        "last_name": String(min_length=1, max_length=2_55, example=LAST_NAME),
        "contact": String(min_length=1, max_length=2_55, example=CONTACT),
        "username": String(min_length=1, max_length=2_55, example=USERNAME),
        "email": String(min_length=1, max_length=2_55, example=EMAIL),
        "address": String(min_length=1, max_length=2_55, example=ADDRESS),
        "city": String(min_length=1, max_length=2_55, example=CITY),
        "state": String(min_length=1, max_length=2_55, example=STATE),
        "country": String(min_length=1, max_length=2_55, example=COUNTRY),
        "postal_code": String(
            min_length=1, max_length=2_55, example=POSTAL_CODE
        ),
        "role_id": Integer(minimum=1, example=ROLE_ID),
    },
    strict=True,
)

# User Create Schema
user_create_schema = ns_user.clone(
    "UserCreateSchema",
    user_base_schema,
    {
        "first_name": String(
            required=True, min_length=1, max_length=2_55, example=FIRST_NAME
        ),
        "last_name": String(
            required=True, min_length=1, max_length=2_55, example=LAST_NAME
        ),
        "username": String(
            required=True, min_length=1, max_length=2_55, example=USERNAME
        ),
        "email": String(
            required=True, min_length=1, max_length=2_55, example=EMAIL
        ),
        "password": String(required=True, example=PASSWORD),
        "role_id": Integer(required=True, minimum=1, example=ROLE_ID),
    },
)

# User Read Base Schema
user_read_base_schema: Model | OrderedModel = ns_user.inherit(
    "UserReadBaseSchema",
    user_base_schema,
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

# User Read Schema
user_read_schema: Model | OrderedModel = ns_user.model(
    name="UserReadSchema",
    model={
        "success": Boolean(default=True),
        "data": Nested(user_read_base_schema),
    },
    strict=True,
)

# User Read All Schema
user_read_all_schema: Model | OrderedModel = ns_user.model(
    name="UserReadAllSchema",
    model={
        "success": Boolean(default=True),
        "data": Nested(user_read_base_schema, as_list=True),
    },
    strict=True,
)

# User Update Schema
user_update_schema: Model | OrderedModel = ns_user.inherit(
    "UserUpdateSchema",
    user_base_schema,
    {
        "first_name": String(required=True),
        "last_name": String(required=True),
        "username": String(required=True),
        "email": String(required=True),
        "role_id": Integer(required=True),
    },
)

user_login_schema = ns_user.model(
    "UserLoginSchema",
    {"email": String(required=True), "password": String(required=True)},
    strict=True,
)

user_login = ns_user.model(
    "UserLogin",
    {
        "first_name": String(),
        "last_name": String(),
        "username": String(),
        "email": String(),
        "role_id": Integer(),
        "token": String(),
    },
)

user_login_response = ns_user.model(
    "UserLoginResponse",
    {
        "status": String(description="ok|nok"),
        "object": Nested(user_login, skip_none=True, allow_null=True),
        "errors": List(String),
    },
)
