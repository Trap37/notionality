import enum

from .base_models import TypedObject


class Color(enum.StrEnum):
    DEFAULT = "default"
    GRAY = "gray"
    BROWN = "brown"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    PINK = "pink"
    RED = "red"


class RichTextObject(TypedObject):
    ...



# TODO: Might need to be moved
class TextObject(RichTextObject, type='text'):
    ...
# TODO: Hardcode all RichText objects
