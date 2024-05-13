"""
User Service

Description:
    - This module contains user service.

"""

from flask_boilerplate.repositories.user import UserRepository

from .base import BaseService


class UserService(BaseService):
    """
    User Service

    Description:
        - This is used to interact with user repository.

    """

    def __init__(self) -> None:
        """
        User Service Constructor

        Description:
            - Initializes User Service object

        """

        super().__init__(UserRepository)
