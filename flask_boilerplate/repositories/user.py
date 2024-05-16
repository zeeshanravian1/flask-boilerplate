"""
User Repository

Description:
    - This module contains user repository.

"""

from passlib.hash import pbkdf2_sha256

from flask_boilerplate.models.user import UserTable
from flask_boilerplate.database.base import db

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

    def get_validate_user(self, email, passowrd):
        user = db.session.query(UserTable).filter(email == email).first()
        is_valid_user = pbkdf2_sha256.verify(passowrd, user.password)
        if is_valid_user:
            return user

        raise Exception
