import enum
from typing import Optional

from .base_models import GenericObject, NotionObject


class UserType(enum.StrEnum):
    PERSON = 'person'
    BOT = 'bot'

# TODO: class PartialUser?


class User(NotionObject, object='user'):
    type: Optional[UserType]
    name: Optional[str]
    avatar_url: Optional[str]

    # def model_validate(cls, obj): Attempt to parse the given object data into the correct `User` type


class Person(User):
    class _NestedData(GenericObject):
        email: str

    person: _NestedData

    def __str__(self):
        return f"[@{self.name}]"


class Bot(User):
    class _NestedData(GenericObject):
        ...

    bot: _NestedData

    def __str__(self):
        return f"[%{self.name}]"
