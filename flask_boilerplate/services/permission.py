"""
Permission Service

Description:
    - This module contains permission service.

"""

from flask_boilerplate.repositories.permission import PermissionRepository

from .base import BaseService


class PermissionService(BaseService):
    """
    Role Service

    Description:
        - This is used to interact with role repository.

    """

    def __init__(self) -> None:
        """
        Role Service Constructor

        Description:
            - Initializes Role Service object

        """

        super().__init__(PermissionRepository)
