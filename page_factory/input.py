import allure
import re
from selenium.webdriver import Keys
from page_factory.component import Component


class Input(Component):
    @property
    def type_of(self) -> str:
        return "input"

    def type(self, value: str, **kwargs) -> None:
        with allure.step(f'Ввод значения "{value}" в поле "{self.name}"'):
            element = self.get_element(**kwargs)
            element.type(value)

    def fill(self, value: str, **kwargs) -> None:
        with allure.step(f'Ввести в поле "{self.name}" значение "{value}"'):
            element = self.get_element(**kwargs)
            element.fill(value)

    def clear(self, **kwargs) -> None:
        with allure.step(f'Очистка поля "{self.name}"'):
            element = self.get_element(**kwargs)
            element.clear()

    def upload_passport_photos(self, path: str, **kwargs) -> None:
        with allure.step(f'Загрузить файл в поле "{self.name}"'):
            input_photo = self.get_element(**kwargs)
            _path = "{path} \n {path} \n {path}".format(path=path)
            input_photo.upload_file(_path)

    def select_first_variant(self, **kwargs):
        with allure.step(f"Выбрать первый вариант из выпадающего меню адреса"):
            element = self.get_element(**kwargs)
            list_name: str | None = self.extract_list_name(self._locator)
            script = (
                f"setTimeout(() => {{const addressUl = document.querySelector('#{list_name}');"
                'addressRegCity.style = "overflow: visible;visibility:visible;";},0);'
            )
            element._page.execute_script(script)
            element.type(Keys.ENTER)

    def extract_list_name(self, list_name: str) -> str | None:
        """Получить список подсказок адресов для XPath"""
        pattern = r"'(.*?)'"
        result = re.search(pattern, list_name)
        if result:
            value = result.group(1)
            return value
        return None

    def enter_asp(self, asp: str, **kwargs) -> None:
        with allure.step(f'Ввести ASP код "{asp}"'):
            elements: list = self.get_elements(**kwargs)._list
            _asp: list = list(asp)
            for i, element in enumerate(elements):
                element.fill(_asp[i])
