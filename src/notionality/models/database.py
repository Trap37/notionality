from typing import Optional
from typing import Optional

from .data_record import PublicDataRecord

from .database_properties import PropertyObject
from .rich_text import RichTextObject


class Database(PublicDataRecord, object='database'):
    title: list[RichTextObject]
    description: Optional[list[RichTextObject]]
    icon: Optional[FileObject | EmojiObject]
    cover: Optional[ExternalFile]  # Type of FileObject
    # TODO: Probably should make a custom obj
    properties: dict[str, PropertyObject]
    is_inline: bool

    @property
    def Title(self):  # TODO: Return the title of this database as plain text
        raise NotImplementedError()
