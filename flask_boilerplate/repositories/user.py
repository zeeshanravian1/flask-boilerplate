"""
User Repository

Description:
    - This module contains user repository.

"""

from passlib.hash import pbkdf2_sha256

from flask_boilerplate.models.user import UserTable

from .base import BaseRepository


class UserRepository(BaseRepository):
    """
    User Repository

    Description:
        - This is used to interact with user table.

    """

    def __init__(self) -> None:
        """
        User Repository Constructor

        Description:
            - This is used to initialize user repository.

        """

        super().__init__(UserTable)

    def create(self, entity):
        """
        Create Entity

        Description:
            - This is used to create entity.

        Args:
            - `entity (dict)`: Entity object. **(Required)**

        Returns:
            - `entity (Model)`: Entity object.

        """

        entity["password"] = pbkdf2_sha256.hash(entity["password"])

        return super().create(entity)
