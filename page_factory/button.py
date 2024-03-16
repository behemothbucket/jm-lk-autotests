import allure
from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return "button"

    def type(self, value: str, **kwargs):
        with allure.step(f'Ввод значения "{value}" в кнопку "{self.name}"'):
            element = self.get_element(**kwargs)
            element.type(value)
