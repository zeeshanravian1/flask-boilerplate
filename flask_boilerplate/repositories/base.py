# -*- coding: utf-8 -*-
"""
Base Repository

Description:
    - This module contains shared repository used by all repositories.

"""

from typing import Any, Sequence

from sqlalchemy import delete, select, update
from sqlalchemy.engine.result import Result
from sqlalchemy.sql.dml import Delete, Update
from sqlalchemy.sql.selectable import Select

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

        record = self.model(**entity)

        db.session.add(record)
        db.session.commit()
        db.session.refresh(record)

        return entity

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

        query: Select = select(self.model).where(self.model.id == entity_id)
        entity: Result[Any] = db.session.execute(statement=query)

        return entity.scalars().first()

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

        query: Select = select(self.model).where(
            getattr(self.model, entity_column) == entity_name
        )
        entity: Result[Any] = db.session.execute(statement=query)

        return entity.scalars().first()

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

        query: Select = select(self.model)
        entities: Result[Any] = db.session.execute(statement=query)

        return entities.scalars().all()

    def update(self, entity_id, entity) -> Any | None:
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

        query: Update = (
            update(self.model).where(self.model.id == entity_id).values(entity)
        )
        db.session.execute(statement=query)
        db.session.commit()

        return entity

    def delete(self, entity_id) -> None:
        """
        Delete Entity

        Description:
            - This is used to delete entity.

        Args:
            - `entity_id` (int): Entity ID. **(Required)**

        Returns:
            - `None`

        """

        query: Delete = delete(self.model).where(self.model.id == entity_id)
        db.session.execute(statement=query)
        db.session.commit()
