import allure
from page_factory.component import Component


class Div(Component):
    @property
    def type_of(self) -> str:
        return "div"
