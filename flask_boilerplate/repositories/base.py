"""
Base Repository

Description:
    - This module contains shared repository used by all repositories.

"""

from typing import Any, Sequence

from flask_boilerplate.database.base import db


class BaseRepository:
    """
    Base Repository

    Description:
        - This is base repository for all repositories.

    Attributes:
        - `model (Model)`: Model object. **(Required)**

    """

    def __init__(self, model) -> None:
        """
        Base Repository Constructor

        Description:
            - This is used to initialize base repository.

        Args:
            - `model (Model)`: Model object. **(Required)**

        Returns:
            - `None`

        """

        self.model: Any = model

    def create(self, entity):
        """
        Create Entity

        Description:
            - This is used to create entity.

        Args:
            - `entity (self.model)`: Entity object. **(Required)**

        Returns:
            - `entity (Model)`: Entity object.

        """

        db_instance = self.model(**entity)

        db.session.add(db_instance)
        db.session.commit()
        db.session.refresh(db_instance)

        return db_instance

    def read_by_id(self, entity_id) -> Any | None:
        """
        Read Entity by ID

        Description:
            - This is used to read entity by ID.

        Args:
            - `entity_id` (int): Entity ID. **(Required)**

        Returns:
            - `entity` (Model): Entity object.

        """

        return db.session.query(self.model).get(ident=entity_id)

    def read_by_name(self, entity_column, entity_name) -> Any | None:
        """
        Read Entity by Name

        Description:
            - This is used to read entity by name.

        Args:
            - `entity_column` (str): Entity column. **(Required)**
            - `entity_name` (str): Entity name. **(Required)**

        Returns:
            - `entity` (Model): Entity object.

        """

        return (
            db.session.query(self.model)
            .filter_by(**{entity_column: entity_name})
            .first()
        )

    def read_all(self) -> Sequence[Any]:
        """
        Read All Entities

        Description:
            - This is used to read all entities.

        Args:
            - `page`: Page number. **(Optional)**
            - `limit`: Limit number. **(Optional)**

        Returns:
            - `entities`: List of entity objects.

        """

        return db.session.query(self.model).all()

    def update(self, entity_id, entity) -> Any | bool:
        """
        Update Entity

        Description:
            - This is used to update entity.

        Args:
            - `entity_id` (int): Entity ID. **(Required)**
            - `entity (self.model)`: Entity object. **(Required)**

        Returns:
            - `entity` (Model): Entity object.

        """

        db_instance = self.read_by_id(entity_id)

        if not db_instance:
            return False

        for key, value in entity.items():
            setattr(db_instance, key, value)

        db.session.commit()
        db.session.refresh(db_instance)

        return db_instance

    def delete(self, entity_id) -> bool:
        """
        Delete Entity

        Description:
            - This is used to delete entity.

        Args:
            - `entity_id` (int): Entity ID. **(Required)**

        Returns:
            - `None`

        """

        db_instance = db.session.query(self.model).get(ident=entity_id)

        if not db_instance:
            return False

        db.session.delete(db_instance)
        db.session.commit()

        return True
