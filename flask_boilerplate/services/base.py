# -*- coding: utf-8 -*-
"""
Base Services

Description:
    - This module contains shared service used by all services.

"""

from typing import Any


class BaseService:
    """
    Base Service

    Description:
        - This is base service for all services.

    Attributes:
        - `repository (BaseRepository)`: Repository object. **(Required)**

    """

    def __init__(self, repository) -> None:
        """
        Base Service Constructor

        Description:
            - Initializes the Service object

        Args:
            - `repository (BaseRepository)`: Repository object. **(Required)**

        Returns:
            - `None`

        """

        self.repository: Any = repository()

    def create(self, entity) -> Any:
        """
        Create Entity

        Description:
            - This is used to create entity.

        Args:
            - `entity (self.repository.model)`: Entity object. **(Required)**

        Returns:
            - `entity (Model)`: Entity object.

        """

        return self.repository.create(entity=entity)

    def read_by_id(self, entity_id) -> Any | None:
        """
        Read Entity By ID

        Description:
            - This is used to read entity by ID.

        Args:
            - `entity_id (int)`: Entity ID. **(Required)**

        Returns:
            - `entity (Model)`: Entity object.

        """

        return self.repository.read_by_id(entity_id=entity_id)

    def read_by_name(self, entity_column, entity_name) -> Any | None:
        """
        Read Entity By Name

        Description:
            - This is used to read entity by name.

        Args:
            - `entity_column (str)`: Entity column. **(Required)**
            - `entity_name (str)`: Entity name. **(Required)**

        Returns:
            - `entity (Model)`: Entity object.

        """

        return self.repository.read_by_name(
            entity_column=entity_column, entity_name=entity_name
        )

    def read_all(self) -> Any:
        """
        Read All Entities

        Description:
            - This is used to read all entities.

        Returns:
            - `entities (List[Model])`: List of entity objects.

        """

        return self.repository.read_all()

    def update(self, entity_id, entity) -> Any | None:
        """
        Update Entity

        Description:
            - This is used to update entity.

        Args:
            - `entity_id (int)`: Entity ID. **(Required)**
            - `entity (self.repository.model)`: Entity object. **(Required)**

        Returns:
            - `entity (Model)`: Entity object.

        """

        return self.repository.update(entity_id=entity_id, entity=entity)

    def delete(self, entity_id) -> None:
        """
        Delete Entity

        Description:
            - This is used to delete entity.

        Args:
            - `entity_id (int)`: Entity ID. **(Required)**

        Returns:
            - `None`

        """

        self.repository.delete(entity_id=entity_id)
