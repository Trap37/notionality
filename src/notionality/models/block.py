from abc import ABC, abstractmethod
from typing import Any, Optional

from notionality.models.emoji import EmojiObject
from notionality.models.file import FileObject
from notionality.models.parent import ParentRef
from notionality.models.refs_TEMP import BlockRef
from notionality.models.rich_text import RichTextObject

from .base_models import GenericObject, TypedObject

from .data_record import DataRecord
from .utils import CodingLanguage, FullColor


# TODO: Check all the optional attributes agaist the API reference to see if they actually are
# TODO: Check if _NestedData attributes are able to not exist. If they have to exist, rewrite some code checking if it does
class Block(DataRecord, TypedObject, object='block'):
    ...


# TODO: May or may not keep
class UnsupportedBlock(Block, type='unsupported'):
    class _NestedData(GenericObject):
        pass

    unsupported: Optional[_NestedData] = None


class TextBlock(Block, ABC):
    @property
    def __text__(self):
        return self('rich_text')

    @property
    def PlainText(self):
        content = self.__text__

        return None if content is None else content


class WithChildrenMixin:
    @property
    def __children__(self):
        return self('children')

    def __iadd__(self, block):
        self.append(block)
        return self

    def append(self, block):
        if block is None:
            raise ValueError('block cannot be None')

        nested = self()

        if nested.children is None:
            nested.children = []

        nested.children.append(block)

        self._has_children = True


# TODO: Reorder these to be in alphabetical order like the API reference
class Paragraph(TextBlock, WithChildrenMixin, type='paragraph'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        children: Optional[list[Block]] = None
        color: FullColor = FullColor.DEFAULT

    paragraph: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class Heading1(TextBlock, type='heading_1'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        color: FullColor = FullColor.DEFAULT

    heading_1: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class Heading2(TextBlock, type='heading_2'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        color: FullColor = FullColor.DEFAULT

    heading_2: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class Heading3(TextBlock, type='heading_3'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        color: FullColor = FullColor.DEFAULT

    heading_3: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class Quote(TextBlock, WithChildrenMixin, type='quote'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        children: Optional[list[Block]] = None
        color: FullColor = FullColor.DEFAULT

    quote: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class Code(TextBlock, type='code'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        caption: list[RichTextObject] = []
        language: CodingLanguage = CodingLanguage.PLAIN_TEXT

    code: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class Callout(TextBlock, WithChildrenMixin, type='callout'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        children: Optional[list[Block]] = None
        icon: Optional[FileObject | EmojiObject] = None
        color: FullColor = FullColor.DEFAULT

    callout: _NestedData = _NestedData()


class BulletedListItem(TextBlock, WithChildrenMixin, type='bulleted_list_item'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        children: Optional[list[Block]] = None
        color: FullColor = FullColor.DEFAULT

    bulleted_list_item: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class NumberedListItem(TextBlock, WithChildrenMixin, type='numbered_list_item'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        children: Optional[list[Block]] = None
        color: FullColor = FullColor.DEFAULT

    numbered_list_item: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class ToDo(TextBlock, WithChildrenMixin, type='to_do'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        checked: bool = False
        children: Optional[list[Block]] = None
        color: FullColor = FullColor.DEFAULT

    to_do: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def IsChecked(self):
        return self.to_do.checked if self.to_do else None

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class Toggle(TextBlock, WithChildrenMixin, type='toggle'):
    class _NestedData(GenericObject):
        rich_text: list[RichTextObject] = []
        children: Optional[list[Block]] = None
        color: FullColor = FullColor.DEFAULT

    toggle: _NestedData = _NestedData()


class Divider(Block, type='divider'):
    divider: Any = {}

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class TableOfContents(Block, type='table_of_contents'):
    class _NestedData(GenericObject):
        color: FullColor = FullColor.DEFAULT

    paragraph: _NestedData = _NestedData()


class Breadcrumb(Block, type='breadcrumb'):
    class _NestedData(GenericObject):
        pass

    breadcrumb: _NestedData = _NestedData()


class Embed(Block, type='embed'):
    class _NestedData(GenericObject):
        # TODO: Try and find out if there's a reason this one isn't optional
        url: str = None

    embed: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def URL(self):
        return self.embed.url
    # TODO: Complete

    @property
    def Markdown(self):
        ...


class Bookmark(Block, type='bookmark'):
    class _NestedData(GenericObject):
        url: str = None
        # TODO: Find out why this is set to None instead of a list like some other attributes
        caption: Optional[list[RichTextObject]] = None

    bookmark: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def URL(self): return self.bookmark.url

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class LinkPreview(Block, type='link_preview'):
    class _NestedData(GenericObject):
        url: str = None

    link_preview: _NestedData = _NestedData()

    # TODO: Complete
    @property
    def URL(self):
        return self.link_preview.url

    # TODO: Complete
    @property
    def Markdown(self):
        ...


class Equation(Block, type='equation'):
    class _NestedData(GenericObject):
        expression: str = None

    equation: _NestedData = _NestedData()


class File(Block, type='file'):
    file: FileObject = None


class Image(Block, type='image'):
    image: FileObject = None


class Video(Block, type='video'):
    video: FileObject = None


class PDF(Block, type='pdf'):
    pdf: FileObject = None


class ChildPage(Block, type='child_page'):
    class _NestedData(GenericObject):
        title: str = None

    child_page: _NestedData = _NestedData()


class ChildDatabase(Block, type='child_database'):
    class _NestedData(GenericObject):
        title: str = None

    child_database: _NestedData = _NestedData()


class Column(Block, WithChildrenMixin, type='column'):
    class _NestedData(GenericObject):
        # TODO: Read API reference snippet below
        # note that children will not be populated when getting this block
        # https://developers.notion.com/changelog/column-list-and-column-support
        children: Optional[list[Block]] = None

    column: _NestedData = _NestedData()


class ColumnList(Block, WithChildrenMixin, type='column_list'):
    class _NestedData(GenericObject):
        # TODO: Read API reference snippet below
        # note that children will not be populated when getting this block
        # https://developers.notion.com/changelog/column-list-and-column-support
        children: Optional[list[Column]] = None

    column_list: _NestedData = _NestedData()


# TODO: Maybe inherit from List?
class TableRow(Block, type='table_row'):
    class _NestedData(GenericObject):
        cells: list[list[RichTextObject]] = None

        def __getitem__(self, col):
            if col > len(self.cells):
                raise IndexError()

            return self.cells[col]

    table_row: _NestedData = _NestedData()

    def __getitem__(self, cell_num):
        return self.table_row[cell_num]

    def append(self, text):
        if self.table_row.cells is None:
            self.table_row.cells = []

        if isinstance(text, list):
            self.table_row.cells.append(text)
        elif isinstance(text, RichTextObject):
            self.table_row.cells.append([text])
        else:
            raise NotImplementedError()
            # TODO: Implement __compose__ replacement here
            rtf = TextObject[text]
            self.table_row.cells.append([rtf])

    @property
    def Width(self):
        return len(self.table_row.cells) if self.table_row.cells else 0


class Table(Block, WithChildrenMixin, type='table'):
    class _NestedData(GenericObject):
        table_width: int = 0
        has_column_header: bool = False
        has_row_header: bool = False

        # note that children will not be populated when getting this block
        # https://developers.notion.com/reference/block#table-blocks
        children: Optional[list[TableRow]] = []

    table: _NestedData = _NestedData()

    def append(self, block: TableRow):
        # XXX need to review whether this is applicable during update...  may need
        # to raise an error if the block has already been created on the server

        if not isinstance(block, TableRow):
            raise ValueError('Only TableRow may be appended to Table blocks.')

        if self.Width == 0:
            self.table.table_width = block.Width
        elif self.Width != block.Width:
            raise ValueError('Number of cells in row must match table')

        # NOTE: This would be fixed if cells is set to a list instead of None by default
        self.table.children.append(block)

    @property
    def Width(self):
        return self.table.table_width


class LinkToPage(Block, type='link_to_page'):
    link_to_page: ParentRef


class SyncedBlock(Block, WithChildrenMixin, type='synced_block'):
    class _NestedData(GenericObject):
        synced_from: Optional[BlockRef] = None
        children: Optional[list[Block]] = None

    synced_block: _NestedData = _NestedData()

    @property
    def IsOriginal(self):
        '''Determine if this block represents the original content.

        If this method returns `False`, the block represents the sync'ed block.
        '''
        return self.synced_block.synced_from is None


class Template(Block, WithChildrenMixin, type='template'):
    class _NestedData(GenericObject):
        rich_text: Optional[list[RichTextObject]] = None
        children: Optional[list[Block]] = None

    template: _NestedData = _NestedData()
