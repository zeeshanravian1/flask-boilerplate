# -*- coding: utf-8 -*-
"""
Role Model

Description:
    - This file contains model for role table.

"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from flask_boilerplate.database.base import BaseTable


class RolesTable(BaseTable):
    """
    Roles Table

    Description:
        - This table is used to create roles in database.

    """

    role_name: Mapped[str] = mapped_column(String(2_55), unique=True)
    role_description: Mapped[str] = mapped_column(String(2_55), nullable=True)
