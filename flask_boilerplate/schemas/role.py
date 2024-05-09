"""
Role Validation Schemas

Description:
    - This file contains all role schemas used by API.

"""

from marshmallow import Schema, fields, validate

from flask_boilerplate.constants.role import ROLE_DESCRIPTION, ROLE_NAME

from .base import BasePaginationReadSchema, BaseReadSchema


class RoleBaseSchema(Schema):
    """
    Role Base Schema

    Description:
        - This schema is used to validate role base data.

    """

    role_name = fields.Str(
        validate=validate.Length(min=1, max=2_55), example=ROLE_NAME
    )
    role_description = fields.Str(
        validate=validate.Length(min=1, max=2_55), example=ROLE_DESCRIPTION
    )


class RoleCreateSchema(RoleBaseSchema):
    """
    Role Create Schema

    Description:
        - This schema is used to validate role creation data passed to API.

    """

    role_name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=2_55),
        example=ROLE_NAME,
    )


# Role Read Schema
class RoleReadSchema(RoleCreateSchema, BaseReadSchema):
    """
    Role Read Schema

    Description:
        - This schema is used to validate role data returned by API.

    """


class RolePaginationReadSchema(BasePaginationReadSchema):
    """
    Role Pagination Read Schema

    Description:
        - This schema is used to validate role pagination data returned by API.

    """

    roles = fields.Nested(RoleReadSchema, many=True)


class RoleUpdateSchema(RoleCreateSchema):
    """
    Role Update Schema

    Description:
        - This schema is used to validate role update data passed to API.

    """


class RolePartialUpdateSchema(RoleBaseSchema):
    """
    Role Partial Update Schema

    Description:
        - This schema is used to validate role partial update data passed to
        API.

    """
