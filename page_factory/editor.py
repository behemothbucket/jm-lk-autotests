import allure

from page_factory.textarea import Textarea


class Editor(Textarea):
    @property
    def type_of(self) -> str:
        return "editor"

    def clear(self):
        with allure.step(f'Очистка элемента {self.type_of} с именем "{self.name}"'):
            self._page.execute_script("window.editor.setValue('');")

    def type(self, value: str, **kwargs):
        with allure.step(
            f'Ввод значения "{value}" в {self.type_of} с именем "{self.name}"'
        ):
            self._page.execute_script(f"window.editor.setValue(arguments[0]);", value)
