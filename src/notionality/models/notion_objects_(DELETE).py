import dataclasses as dc
import datetime
from typing import Literal, Optional, TypeAlias
import enum
from uuid import UUID

from .models.base_models import NotionObject, TypedObject


class TextColor(enum.StrEnum):
    BLUE = 'blue'
    BLUE_BACKGROUND = 'blue_background'
    BROWN = 'brown'
    BROWN_BACKGROUND = 'brown_background'
    DEFAULT = 'default'
    GRAY = 'gray'
    GRAY_BACKGROUND = 'gray_background'
    GREEN = 'green'
    GREEN_BACKGROUND = 'green_background'
    ORANGE = 'orange'
    ORANGE_BACKGROUND = 'orange_background'
    YELLOW = 'yellow'
    YELLOW_BACKGROUND = 'yellow_background'
    PINK = 'pink'
    PINK_BACKGROUND = 'pink_background'
    PURPLE = 'purple'
    PURPLE_BACKGROUND = 'purple_background'
    RED = 'red'
    RED_BACKGROUND = 'red_background'


@dc.dataclass
class Annotation:
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: TextColor


@dc.dataclass
class RichText(NotionObject):
    type: Literal['text', 'mention', 'equation']
    annotations: Annotation
    plain_text: str
    href: Optional[URL]


@dc.dataclass
class DatabaseProperty(NotionObject):
    id: str
    name: str
    description: str
    type: Literal['checkbox', 'created_by', 'created_time', 'date', 'email',
                  'files', 'formula', 'last_edited_by', 'last_edited_time',
                  'multi_select', 'number', 'people', 'phone_number', 'relation',
                  'rich_text', 'rollup', 'select', 'status', 'title', 'url']


@dc.dataclass
class Parent(NotionObject):
    type: Literal['database_id', 'page_id', 'workspace', 'block_id']


@dc.dataclass
class Comment(NotionObject):
    object: Literal['comment']
    id: UUID
    parent: 'Parent'
    discussion_id: UUID
    created_time: DATETIME
    created_by: 'PartialUser'
    last_edited_time: DATETIME
    rich_text: 'RichText'


@dc.dataclass
class UnfurlAttribute(NotionObject):
    id: str
    name: str
    type: Literal['inline', 'embed']


@dc.dataclass
class File(NotionObject):
    type: Literal['external', 'file']


@dc.dataclass
class ExternalFile(File):
    ...


class Emoji(NotionObject):
    type: Literal['emoji', 'custom_emoji']
