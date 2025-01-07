from ...data_records import PublicDataRecord


class Page(PublicDataRecord, object='page'):
    icon: 'ExternalFile | Emoji'
    cover: 'ExternalFile'
    # TODO: Might make a custom obj or type this somehow
    properties: dict[str, PropertyValue]

    def __getitem__(self, name):
        prop = self.properties.get(name)

        # TODO: Maybe add a new @property to create new properties if doesn't exist istead of raising error
        if prop is None:
            raise AttributeError(f'No such property: {name}')

        return prop

    def __setitem__(self, name, value):
        if value is None:
            self.properties.pop(name, None)

        # TODO: Might be better to do this check differently
        # TODO: Could also handle updating values differently instead of overwriting?
        elif isinstance(value, PropertyValue):
            self.properties[name] = value

        else:  # TODO: Change error message to one I like more
            raise ValueError(f'Unable to set {name} :: unsupported value type')

    @property
    def Title(self):  # TODO: Return the title of this page as a string
        raise NotImplementedError()


# Page Properties
class PageProperty(NotionObject):
    id: str
    type: Literal[
        'checkbox', 'created_by', 'created_time', 'date', 'email', 'files',
        'formula', 'last_edited_by', 'last_edited_time', 'multi_select',
        'number', 'people', 'phone_number', 'relation', 'rollup', 'rich_text',
        'select', 'status', 'title', 'url', 'unique_id', 'verification']

# TODO: Hardcode all subclasses
