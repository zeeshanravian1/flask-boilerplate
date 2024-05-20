"""
User Repository

Description:
    - This module contains user repository.

"""

from passlib.hash import pbkdf2_sha256

from flask_boilerplate.database.base import db
from flask_boilerplate.models.user import UserTable

from .base import BaseRepository


class UserRepository(BaseRepository[UserTable]):
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

        super().__init__(UserTable)

    def create(self, entity) -> UserTable:
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

    def get_validate_user(self, email, passowrd) -> UserTable | None:
        user: UserTable | None = (
            db.session.query(UserTable)
            .filter(UserTable.email == email)
            .first()
        )
        if user:
            is_valid_user: bool = pbkdf2_sha256.verify(passowrd, user.password)
            if is_valid_user:
                return user

        return None
