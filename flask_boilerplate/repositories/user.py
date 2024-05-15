"""
User Repository

Description:
    - This module contains user repository.

"""

from typing import Any
from sqlalchemy import select
from sqlalchemy.engine.result import Result
from sqlalchemy.sql.selectable import Select

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
        # user = UserTable.query.filter(email == email).first()
        query: Select = select(self.model).where(self.model.email == email)
        user: Result[Any] = (
            db.session.execute(statement=query).scalars().first()
        )

        is_valid_user = pbkdf2_sha256.verify(passowrd, user.password)
        if is_valid_user:
            return user

        raise Exception
