# -*- coding: utf-8 -*-
"""
Role Repository

Description:
    - This module contains role repository.

"""

from flask_boilerplate.models.role import RolesTable

from .base import BaseRepository


class RoleRepository(BaseRepository):
    """
    Role Repository

    Description:
        - This is used to interact with role table.

    """

    def __init__(self) -> None:
        """
        Role Repository Constructor

        Description:
            - This is used to initialize role repository.

        """

        super().__init__(RolesTable)
