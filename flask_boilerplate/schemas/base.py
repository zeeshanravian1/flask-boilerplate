# -*- coding: utf-8 -*-
"""
Base Read Validation Schemas

Description:
    - This module contains base read schemas used by API.

"""

from marshmallow import Schema, fields, validate

from flask_boilerplate.constants.base import (
    CREATED_AT,
    ID,
    LIMIT,
    PAGE,
    TOTAL_PAGES,
    TOTAL_RECORDS,
    UPDATED_AT,
)


class BaseReadSchema(Schema):
    """
    Base Read Schema

    Description:
        - This schema is used to validate base data returned by API.

    """

    id = fields.Int(required=True, validate=validate.Range(min=1), example=ID)
    created_at = fields.DateTime(required=True, example=CREATED_AT)
    updated_at = fields.DateTime(example=UPDATED_AT)

    class Meta:
        """
        Ordered Meta

        Description:
            - This is used to keep schema ordered.

        """

        ordered = True


class BasePaginationReadSchema(Schema):
    """
    Base Pagination Read Schema

    Description:
        - This schema is used to validate base pagination data returned by API.

    """

    total_records = fields.Int(
        required=True, validate=validate.Range(min=0), example=TOTAL_RECORDS
    )
    total_pages = fields.Int(
        required=True, validate=validate.Range(min=0), example=TOTAL_PAGES
    )
    page = fields.Int(
        required=True, validate=validate.Range(min=1), example=PAGE
    )
    limit = fields.Int(
        required=True, validate=validate.Range(min=0), example=LIMIT
    )
    records = fields.List(fields.Nested(BaseReadSchema), example=[])

    class Meta:
        """
        Ordered Meta

        Description:
            - This is used to keep schema ordered.

        """

        ordered = True
