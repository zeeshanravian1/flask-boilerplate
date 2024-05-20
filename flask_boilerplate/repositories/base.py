"""
Base Repository

Description:
    - This module contains shared repository used by all repositories.

"""

from typing import Generic, Type, TypeVar

from flask_boilerplate.database.base import BaseTable, db

Model = TypeVar("Model", bound=BaseTable)


class BaseRepository(Generic[Model]):
    """
    Base Repository

    Description:
        - This is base repository for all repositories.

    Attributes:
        - `model (Model)`: Model object. **(Required)**

    """

    def __init__(self, model: Type[Model]) -> None:
        """
        Base Repository Constructor

        Description:
            - This is used to initialize base repository.

        Args:
            - `model (Model)`: Model object. **(Required)**

        Returns:
            - `None`

        """

        self.model: type[Model] = model

    def create(self, entity) -> Model:
        """
        Create Entity

        Description:
            - This is used to create entity.

        Args:
            - `entity (self.model)`: Entity object. **(Required)**

        Returns:
            - `entity (Model)`: Entity object.

        """

        db_instance: Model = self.model(**entity)

        db.session.add(instance=db_instance)
        db.session.commit()
        db.session.refresh(instance=db_instance)

        return db_instance

    def create_multiple(self, entities) -> list[Model]:
        """
        Create Multiple Entities

        Description:
            - This is used to create multiple entities.

        Args:
            - `entities (List[self.model])`: List of entity objects.
            **(Required)**

        Returns:
            - `entities (List[Model])`: List of entity objects.

        """

        db_instances: list[Model] = [
            self.model(**entity) for entity in entities
        ]

        db.session.add_all(instances=db_instances)
        db.session.commit()
        db.session.refresh(instance=db_instances)

        return db_instances

    def read_by_id(self, entity_id) -> Model | None:
        """
        Read Entity by ID

        Description:
            - This is used to read entity by ID.

        Args:
            - `entity_id` (int): Entity ID. **(Required)**

        Returns:
            - `entity` (Model): Entity object.

        """

        return db.session.get(entity=self.model, ident=entity_id)

    def read_by_column(self, entity_column, entity_value) -> Model | None:
        """
        Read Entity by Column

        Description:
            - This is used to read entity by column.

        Args:
            - `entity_column` (str): Entity column. **(Required)**
            - `entity_value` (str): Entity value. **(Required)**

        Returns:
            - `entity` (Model): Entity object.

        """

        return (
            db.session.query(self.model)
            .filter_by(**{entity_column: entity_value})
            .first()
        )

    def read_all(self) -> list[Model]:
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

    def update(self, entity_id, entity) -> Model | bool:
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

        db_instance: Model | None = self.read_by_id(entity_id=entity_id)

        if not db_instance:
            return False

        for key, value in entity.items():
            setattr(db_instance, key, value)

        db.session.commit()
        db.session.refresh(instance=db_instance)

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

        db_instance: Model | None = self.read_by_id(entity_id=entity_id)

        if not db_instance:
            return False

        db.session.delete(instance=db_instance)
        db.session.commit()

        return True
