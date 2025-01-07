import enum

from uuid import UUID
from typing import Any, Optional, Self

from .base_models import GenericObject, TypedObject

from .rich_text import Color


class Function(enum.StrEnum):
    AVERAGE = 'average'
    CHECKED = 'checked'
    COUNT_PER_GROUP = 'count_per_group'
    COUNT = 'count'
    COUNT_VALUES = 'count_values'
    DATE_RANGE = 'date_range'
    EARLIEST_DATE = 'earliest_date'
    EMPTY = 'empty'
    LATEST_DATE = 'latest_date'
    MAX = 'max'
    MEDIAN = 'median'
    MIN = 'min'
    NOT_EMPTY = 'not_empty'
    PERCENT_CHECKED = 'percent_checked'
    PERCENT_EMPTY = 'percent_empty'
    PERCENT_NOT_EMPTY = 'percent_not_empty'
    PERCENT_PER_GROUP = 'percent_per_group'
    PERCENT_UNCHECKED = 'percent_unchecked'
    RANGE = 'range'
    UNCHECKED = 'unchecked'
    UNIQUE = 'unique'
    SHOW_ORIGINAL = 'show_original'
    SHOW_UNIQUE = 'show_unique'
    SUM = 'sum'


class NumberFormat(enum.StrEnum):
    ARGENTINE_PESO = 'argentine_peso'
    BAHT = 'baht'
    AUSTRALIAN_DOLLAR = 'australian_dollar'
    CANADIAN_DOLLAR = 'canadian_dollar'
    CHILEAN_PESO = 'chilean_peso'
    COLOMBIAN_PESO = 'colombian_peso'
    DANISH_KRONE = 'danish_krone'
    DIRHAM = 'dirham'
    DOLLAR = 'dollar'
    EURO = 'euro'
    FORINT = 'forint'
    FRANC = 'franc'
    HONG_KONG_DOLLAR = 'hong_kong_dollar'
    KORUNA = 'koruna'
    KRONA = 'krona'
    LEU = 'leu'
    LIRA = 'lira'
    MEXICAN_PESO = 'mexican_peso'
    NEW_TAIWAN_DOLLAR = 'new_taiwan_dollar'
    NEW_ZEALAND_DOLLAR = 'new_zealand_dollar'
    NORWEGIAN_KRONE = 'norwegian_krone'
    NUMBER = 'number'
    NUMBER_WITH_COMMAS = 'number_with_commas'
    PERCENT = 'percent'
    PHILIPPINE_PESO = 'philippine_peso'
    POUND = 'pound'
    PERUVIAN_SOL = 'peruvian_sol'
    RAND = 'rand'
    REAL = 'real'
    RINGGIT = 'ringgit'
    RIYAL = 'riyal'
    RUBLE = 'ruble'
    RUPEE = 'rupee'
    RUPIAH = 'rupiah'
    SHEKEL = 'shekel'
    SINGAPORE_DOLLAR = 'singapore_dollar'
    URUGUAYAN_PESO = 'uruguayan_peso'
    YEN = 'yen'
    YUAN = 'yuan'
    WON = 'won'
    ZLOTY = 'zloty'


class PropertyObject(TypedObject):  # TODO: Might rename to DatabaseProperty
    id: str
    name: str
    description: Optional[str]  # TODO: Double check this is optional


class Checkbox(PropertyObject, type='checkbox'):
    checkbox: Any = {}


class CreatedBy(PropertyObject, type='created_by'):
    created_by: Any = {}


class CreatedTime(PropertyObject, type='created_time'):
    created_time: Any = {}


class Date(PropertyObject, type='date'):
    date: Any = {}


class Email(PropertyObject, type='email'):
    email: Any = {}


class Files(PropertyObject, type='files'):
    files: Any = {}


class Formula(PropertyObject, type='formula'):
    class _NestedData(GenericObject):
        expression: str  # TODO: https://www.notion.com/help/formulas

    # TODO: Might need to instantiate this. It's like that in notional. Check rest of file if you do
    formula: _NestedData


class LastEditedBy(PropertyObject, type='last_edited_by'):
    last_edited_by: Any = {}


class LastEditedTime(PropertyObject, type='last_edited_time'):
    last_edited_time: Any = {}


class SelectOption(GenericObject):
    id: str
    name: str
    # TODO: Check if this can be something other than predefined colors
    color: str = Color.DEFAULT

    # TODO: Might need to fix this. May also not be needed
    @classmethod
    def from_list(cls, options: list[Any]) -> list[Self]:
        return [cls(**option) for option in options] if options else [cls()]


class MultiSelect(PropertyObject, type='multi_select'):
    class _NestedData(GenericObject):
        options: list[SelectOption]

    # TODO: Check that this actually becomes a list of objects
    multi_select: _NestedData


class Number(PropertyObject, type='number'):
    class _NestedData(GenericObject):
        format: NumberFormat = NumberFormat.NUMBER

        # TODO: Might add this for better error messages. See: https://github.com/pydantic/pydantic/issues/355
        # @pydantic.field_validator('format', mode='before')
        # @classmethod
        # def validate_enum_field(cls, field: str):
        #     return NumberFormat(field)

    number: _NestedData


class People(PropertyObject, type='people'):
    people: Any = {}


class PhoneNumber(PropertyObject, type='phone_number'):
    phone_number: Any = {}


# TODO: Check out those other types of relations in notional
class Relation(PropertyObject, type='relation'):
    class _NestedData(GenericObject):
        database_id: UUID
        synced_property_id: str
        synced_property_name: str

    relation: _NestedData


class RichText(PropertyObject, type='rich_text'):
    rich_text: Any = {}


class Rollup(PropertyObject, type='rollup'):
    class _NestedData(GenericObject):
        function: Function

        # TODO: Check if these values are optional
        relation_property_id: str
        relation_property_name: str

        rollup_property_id: str
        rollup_property_name: str

    rollup: _NestedData


class Select(PropertyObject, type='select'):
    class _NestedData(GenericObject):
        options: list[SelectOption]

    select: _NestedData


class StatusGroup(Select):
    options_ids: list[UUID]


class Status(PropertyObject, type='status'):
    class _NestedData(GenericObject):
        options: list[SelectOption]
        groups: list[StatusGroup]

    status: _NestedData


class Title(PropertyObject, type='title'):
    title: Any = {}


class Url(PropertyObject, type='url'):
    url: Any = {}
