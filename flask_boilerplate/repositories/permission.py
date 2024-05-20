"""
Permission Repository

Description:
    - This module contains permission repository.

"""

from flask_boilerplate.models.permission import PermissionTable

from .base import BaseRepository


class PermissionRepository(BaseRepository[PermissionTable]):
    """
    Permission Repository

    Description:
        - This is used to interact with permission table.

    """

    def __init__(self) -> None:
        """
        Permission Repository Constructor

        Description:
            - This is used to initialize permission repository.

        """

        super().__init__(PermissionTable)
