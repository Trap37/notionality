from pydantic import BaseModel, field_serializer
from typing import Optional
from uuid import UUID

TYPESMAP = '__notionality_typemap__'


def serialize_to_api(data):  # TODO: Finish
    ...


class GenericObject(BaseModel):
    ...
    # def __setattr__(self, name, value): ...  # TODO: Finish

    @classmethod
    def _set_field_default(cls, name, default=None):
        setattr(cls, name, default)
        # TODO: Might need to change the __model_fields__ values aswell
    # def refresh(__notionality_self__, **data): #NOTE: Maybe include
    # def dict(self, **kwargs): ...  # NOTE: Finish


class NotionObject(GenericObject):
    object: str
    id: Optional[UUID] = None

    def __init_subclass__(cls, *, object=None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        if object is not None:
            cls._set_field_default('object', object)

    # @validator("object", always=True, pre=False)
    # def _verify_object_matches_expected(cls, val): #NOTE Might Need


class TypedObject(GenericObject):
    type: str

    def __init_subclass__(cls, *, type=None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        type_name = cls.__name__ if type is None else type

        cls._register_type(type_name)

    # TODO: Maybe make it add new values aswell?
    def __call__(self, field=None):
        type = getattr(self, 'type', None)

        if type is None:
            raise AttributeError('type not specified')

        nested = getattr(self, type)

        if field is not None:
            nested = getattr(nested, field)

        return nested

    # TODO: Maybe define __get_pydantic_core_schema__ which is equivalent to __get_validators__
    # TODO: Maybe define model_validate(cls, obj): to help decide what object to instantiate

    @classmethod
    def _register_type(cls, name):
        cls._set_field_default('type', name)

        if not hasattr(cls, TYPESMAP):
            setattr(cls, TYPESMAP, {})

        if name in getattr(cls, TYPESMAP):
            raise ValueError(f'Duplicate subtype for class - {name} :: {cls}')

        getattr(cls, TYPESMAP)[name] = cls

    # TODO: Need to define _register_type(cls, name): if overriding model_validate or using __get_pydantic_core_schema__
