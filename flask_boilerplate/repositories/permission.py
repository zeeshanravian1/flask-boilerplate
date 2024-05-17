"""
Role Repository

Description:
    - This module contains role repository.

"""

from flask_boilerplate.models.permission import PermissionTable

from .base import BaseRepository


class PermissionRepository(BaseRepository):
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

        super().__init__(PermissionTable)
