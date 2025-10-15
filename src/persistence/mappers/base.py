from typing import Generic, TypeVar

from pydantic import BaseModel as PydanticBaseModel

from persistence.models.base import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
EntityType = TypeVar("EntityType", bound=PydanticBaseModel)


class BaseMapper(Generic[ModelType, EntityType]):
    model_type: type[ModelType]
    entity_type: type[EntityType]

    @classmethod
    def to_model(cls, entity: EntityType) -> ModelType:
        return cls.model_type(**entity.model_dump())

    @classmethod
    def to_entity(cls, model: ModelType) -> EntityType:
        return cls.entity_type.model_validate(model, from_attributes=True)
