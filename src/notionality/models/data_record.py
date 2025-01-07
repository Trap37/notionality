from datetime import datetime
from uuid import UUID

from .base_models import NotionObject

from .user import User
from .refs_TEMP import ParentRef


class DataRecord(NotionObject):
    id: UUID = None

    created_time: datetime
    created_by: User

    last_edited_time: datetime
    last_edited_by: User

    parent: ParentRef
    _has_children: bool

    archived: bool
    in_trash: bool  # TODO: Maybe delete


class PublicDataRecord(DataRecord):
    url: str
    public_url: str
