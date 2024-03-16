from page_factory.component import Component


class Label(Component):
    @property
    def type_of(self) -> str:
        return "label"
